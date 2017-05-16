# Assignment 2 - Kanban Board

In this second assignment, you will write an API for a
[`Kanban Board`](https://leankit.com/learn/kanban/kanban-board/) to be used by
a single person to manage tasks they have yet `todo`, tasks that are `in
progress`, and tasks that are `done`.  This application has a front-end web
app that will be useful as both a debugging tool, as well as a visualization
of how your API contributes to a successful product that a user can interact

![Kanban Board View](board.png)

## Learning Objectives

This assignment, unlike the first assignment, involves the complete application-
layer backend development experience.  The skills honed in this project are those
you'd use day-to-day when developing any backend supporting an app, be it web
or mobile.  As a result, it involves several tools / technologies / concepts:

* `Python` as a language and `Flask` as a framework
* [`JSON`](http://www.json.org/) as a means of sending and receiving data
* `HTTP` requests / responses
* `MySQL` system configuration and usage
* `SQL-esque` data-modeling
* [`ORM`](http://flask-sqlalchemy.pocoo.org/2.1/) usage and data-modeling
* [`Object Serialization`](http://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* `SQL` querying
* Writing an `API` to fit a specification given by front-end

## Table of Contents

* [Academic Integrity and Collaboration](#academic-integrity-and-collaboration)
* [System Configuration](#system-configuration)
* [Database Creation](#database-creation)
* [Organization](#organization)
* [Front-end](#front-end)
* [Expected Functionality](#expected-functionality)
* [Suggestions](#suggestions)
* [Testing Your Code](#testing-your-code)
* [Project Submission](#project-submission)

## Academic Integrity and Collaboration

#### Academic Integrity

Note that these projects should be completed **individually**. As a result, all University-standard AI guidelines should be followed.

#### Code Attribution and Collaboration

One of the reasons we chose `Flask` as an initial backend framework for students to use is because of its phenomenal support online. Looking up framework documentation and adapting the docs' sample code to suite your own needs in something we expect and want you to do, as it allows you to explore and increase your self-sufficiency regarding backend development. However, if you find code in a `StackOverflow` post or in an open source Github repository, then you should cite it accordingly. See the [project submission](#project-submission) section for guidelines as to where to include those citations.

## System Configuration

The initial [**4** steps](https://github.com/Cornell-PoBE/A1/blob/master/README.md#system-configuration)
from `A1` are required in order to interact with this project.  

In addition to the above steps, we expect you to have `MySQL` installed.  
A guide to do so can be found [here](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing).  
In addition, you should be able to access your `MySQL` system's terminal via the command-line
easily.  We recommend setting up your `$PATH` in order for you to access the `mysql` console.
To do so, add the following line to your `.bashrc`, `.zshrc`, or whatever other shell you
might use (these configuration files are found at your `root user directory: ~`):

````bash
export PATH="/path/to/my/mysql/bin_folder/bin:$PATH"
````
As an example, I'm on a `Mac` and my `MySQL` bin is located at the following path:

````bash
/usr/local/mysql-5.7.17-macos10.12-x86_64/bin
````

In addition, we we expect your backend to parameterized with [`environment variables`](https://en.wikipedia.org/wiki/Environment_variable) so that we can run the
code on our systems with these variables set to our own environment's configurations.  In
order to make dealing with environment variables easier, we recommend you install
[`autoenv`](https://github.com/kennethreitz/autoenv).  `autoenv` allows for environment
variable loading on `cd-ing` into the base directory of the project.  You can declare
environment variables in a `.env` file of the following format:

````bash
export APP_SETTINGS=config.DevelopmentConfig
export DB_NAME=pobe_a2_db
...
````

On `cd-ing` into your project directory, you can ensure that these variables are, in fact,
loaded into your environment by running the following argument, with `VARIABLE_NAME` replaced
with a variable you're setting in your `.env` file:

````bash
echo $VARIABLE_NAME
````

## Database Creation

`MySQL` will give you an initial, temporary password that you use to sign into the
console for the first time:

````bash
mysql -u root -p <temporary-password>
````
Once in you can create a user account outside of `root` that you use to manage all your
local databases:

````bash
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
````

You can provide that user account full access via the following commands:

````bash
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
````

Once you have this user setup, quit the console and reenter with this user:

````bash
quit
mysql -u newuser -p password
````

Create a database with this user via the following command:

````bash
CREATE DATABASE pobe_a2_db;
````

You have successfully created a `MySQL` user account and database!

## Organization

The following describes the initial file-structure of the directory `./src`:

````bash
.
├── app
│   ├── __init__.py
│   ├── base.py
│   ├── constants.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── bundle.js
│   └── templates
│       ├── 404.html
│       └── index.html
├── config.py
├── manage.py
├── requirements.txt
└── run.py
````

Below consists of brief discussions of each one of the above files:

#### config.py

This file defines configurations for the `Flask` app to run with.  These configurations
specify things like the number of threads the app runs with, whether `DEBUG` mode is on,
etc.  In addition, this file grabs environment variables in order to establish the `DB_URL`,
a.k.a. the `URL` your application uses to interact with the database.  On looking at this file,
you'll see it accesses the following environment variables: `DB_USERNAME`, `DB_PASSWORD`,
`DB_HOST`, and `DB_NAME`.  These correspond to your user account name and password that you
used to create the database in the [`Database Creation`](#database-creation) section,
the `IP` you're running the database on (should be `localhost` if you're developing locally
for this project, which you should be), and the name of the database, "pobe_a2_db", or whatever
you chose to name your database.  

This file articulates the main environment variables you MUST have in order to run the app
in the first place: all the database-related variables, plus a variable specifying
which configuration you're running the app in.  We recommend you run the app the
`DevelopmentConfig` when you work on it, so you can see debugging information and such.  As
a result, your `.env` file should look like the following, at the minimum:

````bash
export APP_SETTINGS=config.DevelopmentConfig
export DB_USERNAME=your_username
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_NAME=pobe_a2_db
````

#### manage.py

This file provides you with a command-line interface for performing changes to your
database as your application evolves.  We expect you to leverage
[`flask-sqlalchemy`](http://flask-sqlalchemy.pocoo.org/2.1/)
during this project, meaning you'll be able to describe your database tables as `Python
classes`.  As you define your `classes`, your actual database should reflect the schema
you design.  To ensure this happens, you can run "migrations" to change the database.  
Each migration stores metadata in a `./src/migrations` directory.  The below commands
enumerate the workflow of the migrating the database using `manage.py`:

````bash
# Initialize migrations - only needs to be done initially
python manage.py db init
# Create a migration
python manage.py db migrate
# Apply it to the DB
python manage.py db upgrade
````

#### requirements.txt

This file outlines the initial module dependencies of the app. To install
these, run `pip install -r requirements.txt`. If you pip install a module
during the duration of your project, be sure to `pip freeze > requirements.txt`
to add the new module to the requirements.txt file, **or else we won't be
able to run your project.**

#### run.py

This file is the script used to run your `Flask` app.  You can run your app
via the following:

````bash
python run.py
````

#### app/static

This directory contains the front-end `JavaScript` / `CSS`.  You do not need
to touch this directory or its contents.

#### app/templates

This directory contains the front-end `HTML`.  You do not need to touch this
directory or its contents.

#### app/__init__.py

This file bootstraps the app / database.  The only part of this file you should
be concerned with is the commented-out code in the middle of the file:

````python
# Import + Register Blueprints
# Workflow is as follows:
# from app.blue import blue as blue
# app.register_blueprint(blue)
````

What does this mean?  We encourage you to define your app functionality in a
[`Flask Blueprint`](http://flask.pocoo.org/docs/0.12/blueprints/).  Once you
write that blueprint, you can import it and register it with the `Flask` application
instance using the above, commented-out code.  

#### app/constants.py

This is an empty file where you can keep app-wide constants.

#### app/base.py

This file defines an abstract `SQLAlchemy` model.  We expect all your `SQLAlchemy`
models to extend this base, abstract class.  

## Front-end

[`Here`]() is a link to a publicly-available instance of the front-end, so you can
explore its capabilities.  

## Expected Functionality

#### Create a Board
**Request:** `POST /kanban/boards?title={board_title}`
**Response:**

````javascript
{
  "success": true,
  "data": {
    "board": {
      "board_elements": [],
      "created_at": "2017-05-15T22:43:32+00:00",
      "id": 1,
      "title": "My Awesome Board",
      "updated_at": "2017-05-15T22:43:32+00:00"
    }
  }
}
````

#### Delete a Board
**Request:** `DELETE /kanban/boards?id={board_id}`
**Response:**

````javascript
{
  "success": true
}
````

#### Get Boards
**Request:** `GET /kanban/boards`
**Response:**

````javascript
{
  "success": true,
  "data": {
    "created_at": "2017-05-15T22:43:32+00:00",
    "id": 1,
    "title": "My Awesome Board",
    "updated_at": "2017-05-15T22:43:32+00:00",
    "todo_count": 1,
    "inprogress_count": 3,
    "done_count": 5
  }
}
````

#### Get Board By ID

**Request:** `GET /kanban/boards/{board_id}`
**Response:**

````javascript
{
  "success": true,
  "data": {
    "board": {
      "created_at": "2017-05-15T22:43:32+00:00",
      "id": 1,
      "title": "My Awesome Board",
      "updated_at": "2017-05-15T22:43:32+00:00",
      "todo": [
        // todo board_elements, see structure below
      ],
      "inprogress": [
        // inprogress board_elements, see structure below
      ],
      "done": [
        // done board_elements, see structure below
      ]
    }
  }
}
````