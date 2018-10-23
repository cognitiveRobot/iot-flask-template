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
```

### Installing

Follow the steps below to get a development env up and running in a ubuntu(linux)

1. Go to your project folder
```
$ cd <path-to-the-folder>/iot-flask-template
```
2. Create a Virtual Environment
```
$ python3 -m venv v-iot
```
3. Activate the Virtual Environment
```
$ souce v-iot/bin/activate
```
4. Upgrade the pip
```
$ pip install --upgrade pip
```
5. Install all python packages
```
$ pip install -r requirments.txt
```
If everything goes well up to now, then you would be able to quickly run the app.
```
$ python app.py
```
If all good so far, then follow next to know how to integrate the database for this app. If not, they raise an issue, I will reply asap.

## Intregating the MySQL Database

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Zulfikar Hossain** - *Initial work* - [CognitiveRobot](https://github.com/CognitiveRobot)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Brad Traversy](https://github.com/bradtraversy/myflaskapp)
