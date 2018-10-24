# flask-app-template

Template to build an Internet of Things application using Flask and MySQL.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python
Virtual Environment
MySQL
Your IDE
```

### Installing

Follow the steps below to get a development env up and running in a ubuntu(linux)

1. Go to your main project folder.
```
$ cd <path-to-the-folder>
```
2. git clone the repository.
```
$ git clone git@github.com:cognitiveRobot/iot-flask-template.git
```
3. Create a Virtual Environment
```
$ python3 -m venv v-iot
```
4. Activate the Virtual Environment
```
$ souce v-iot/bin/activate
```
5. Upgrade the pip
```
$ pip install --upgrade pip
```
6. Install all python packages
```
$ pip install -r requirments.txt
```
7. If everything goes well up to now, then you would be able to quickly run the app.
```
$ python app.py
```
If all good so far, then follow next to know how to integrate the database for this app. If not, they raise an issue, I will reply asap.

## Intregating the MySQL Database

Considering you have installed MySQL in your system. Follow the steps below to integrate a MySQL database to store user details.

1. Create a table named users in your database as follows.

  ```
mysql> describe users;
+---------------+--------------+------+-----+-------------------+----------------+
| Field         | Type         | Null | Key | Default           | Extra          |
+---------------+--------------+------+-----+-------------------+----------------+
| id            | int(11)      | NO   | PRI | NULL              | auto_increment |
| name          | varchar(100) | YES  |     | NULL              |                |
| email         | varchar(100) | YES  |     | NULL              |                |
| username      | varchar(30)  | YES  |     | NULL              |                |
| password      | varchar(100) | YES  |     | NULL              |                |
| register_date | timestamp    | NO   |     | CURRENT_TIMESTAMP |                |
+---------------+--------------+------+-----+-------------------+----------------+
  ```
2. Create database.py file in the project root director (i.e. app.py and database.py will sit in the same folder) and save the following content.
```
def dbusers():
    db_users = {
            'id':1,
            'user':'<ur_mysql_username>',
            'password':'<ur_username's_password>',
            'db':'<your_database>',
            'host':'localhost',
            'cursor':'DictCursor'
    }
    return db_users
    ```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Comming soon.

## Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - For Server Side Program
* [Flask](https://maven.apache.org/) - For Webapp Framework
* [MySQL](https://rometools.github.io/rome/) - For Database
* [Materialize](https://materializecss.com) - For Front End

## Contributing

Make the pull request.

## Versioning

See the [See the tags](https://github.com/cognitiveRobot/iot-flask-template/commits/master)

## Authors

* **Zulfikar Hossain** - *Initial work* - [CognitiveRobot](https://github.com/CognitiveRobot)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Brad Traversy](https://github.com/bradtraversy/myflaskapp) - For the initial code.
* [Billie Thompson](https://gist.github.com/PurpleBooth) - For the this readme file template.
