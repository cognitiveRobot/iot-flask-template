from flask import Flask, render_template, request, redirect, url_for, logging, session, flash
from wtforms import Form, StringField, PasswordField, validators
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps

from database import dbusers
from devices import Devices

app = Flask(__name__)
app.debug=True

devices = Devices()
db_users = dbusers() # Hiding database info from others

# Config MySQL
app.config['MYSQL_HOST'] = db_users['host']
app.config['MYSQL_USER'] = db_users['user']
app.config['MYSQL_PASSWORD'] = db_users['password']
app.config['MYSQL_DB'] = db_users['db']
app.config['MYSQL_CURSORCLASS'] = db_users['cursor']
mysql = MySQL(app)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# About Route/Page
@app.route('/about')
def about():
    return render_template('about.html')

#Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')


# db = AppDatabase(app)
# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # cur = db.get_cur()
        # db.insert(cur, form.name.data, form.email.data, form.username.data, sha256_crypt.encrypt(str(form.password.data)))

        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()


        flash('Successful. You are registered. You may login.', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute SQL
        result = cur.execute('SELECT * FROM users WHERE username= %s', [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Password
            if sha256_crypt.verify(password_candidate, password):
                #Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are logged in.', 'success')

                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)

        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user looged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized! Please login.', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout Route
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You successfully logged out', 'success')
    return redirect(url_for('login'))

# Dashboard Route
@app.route('/dashboard')
@is_logged_in
def dashboard():
    print("Dashboard")
    # Retriving data from database will go here
    # First will have to get the data from the database and then send to the view
    return render_template('dashboard.html', devices=devices)

# Device Control Route
@app.route('/device/<string:id>/<string:action>/')
@is_logged_in
def device_control(id, action):
    for index in range(len(devices)):
        if devices[index]['id'] == int(id):
            # Update status
            devices[index]['status'] = action
            # Turn on/off the device
            #Change the pin
            print(devices[index]['pin'])
            flash('Successful!! ' + devices[index]['name'] + ' updated', 'success')

    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key = 'verySecret#123'
    app.run()
