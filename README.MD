# BE NC NEWS

The FOMO Back End repository is a RESTful API built using Python and the framework Flask.

The hosted version can be viewed [here] (https://fomo-api.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this project, the following dependencies will need to be installed:

| Dependency    | Version |
| ------------- | ------- |
| aniso8601     |  8.0.0  |
| attrs         |  19.3.0 |
| Click         |  7.0    |
| Flask         |  1.1.1  |
| Flask-Cors    |  3.0.8  |
| Flask-JWT     |  0.3.2  |
| Flask-JWT-    |         |
|  Extended     |  3.24.1 |
| Flask-RESTful |  0.3.7  |
| Flask-        |         |
| SQLAlchemy    |  2.4.1  |
| gunicorn      |  20.0.4 |
| importlib-    |         |
| metadata      |  1.4.0  |
| itsdangerous  |  1.1.0  |
| Jinja2        |  2.10.3 |
| MarkupSafe    |  1.1.1  |
| more-itertools|  8.1.0  |
| packaging     |  20.0   |
| passlib       |  1.7.2  |
| pluggy        |  0.13.1 |
| psycopg2      |  2.8.4  |
| py            |  1.8.1  |
| PyJWT         |  1.7.1  |
| pyparsing     |  2.4.6  |
| pytest        |  5.3.2  |
| pytz          |  2019.3 |
| six           |  1.13.0 |
| SQLAlchemy    |  1.3.12 |
| wcwidth       |  0.1.8  |
| Werkzeug      |  0.16.0 |
| zipp          |  0.6.0  |

### Installing

This section details the steps to get the development environment up and running. 


Step 1: Clone the repository with the command: 

```
$ git clone https://github.com/Baileex/BE-FOMO.git
```

Step 2: Open the repository in your preferred code editor e.g VSCode, Atom etc

Step 3: Navigate into the cloned repository and create a virtual environment:


```
virtualenv venv
```

Step 4: activate the virtual environment

On Mac OS
```
source venv/bin/activate
```

Step 5: Install dependencies using the following command:

```
pip install -r requirements.txt
```

<!-- ## Running the tests

To test the endpoints locally and ensure that everything has been configured correctly use the command:

```
$ npm t
``` -->

### Endpoints

The table below outlines the purpose of each test category:



Endpoint                           | Request | Tests                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /api                               | GET     | Ensures that a JSON detailing the available endpoints and the requirements within each in served upon receiving a request.                                                                                                                                                                                                                              |
| /api/topics                        | GET     | Ensures that all topics are served. These are served as an array of each topic.                                                                                                                                                                                                                                                                         |
| /api/topics                        | POST    | Ensures that a new topic may be posted. An error is returned if the slug is less than 3 characters in length or a description is not provided.                                                                                                                                                                                                          |
| /api/users                         | GET     | Ensures that all users are served. These are served as an array of users.                                                                                                                                                                                                                                                                               |
| /api/users                         | POST    | Ensures that a new user may be posted. An error is returned if the username is less than 3 characters in length, or insufficient details are provided.                                                                                                                                                                                                  |
| /api/users/:username               | GET     | Ensures that details of the requested user are served. An error is returned if the requested user does not exist.                                                                                                                                                                                                                                       |
| /api/articles                      | GET     | Ensures that all articles are served in an array. Also ensures that the 6 valid queries (sort-by, order, author, topic, limit and page) function as intended, returning an error if an invalid value is provided, or a page requested that does not exist.                                                                                              |
| /api/articles                      | POST    | Ensures that a new article may be posted. An error is returned if either the topic or user posting the article do not exist.                                                                                                                                                                                                                           |
| /api/articles/:article_id          | GET     | Ensures that the correct article is displayed. An error is returned if the requested article ID does not exist or a non-integer is entered.                                                                                                                                                                                                             |
| /api/articles/:article_id          | PATCH   | Ensures that the requested changes are made to the article's vote property, serving the updated article. If additional keys are provided, they are ignored and an error is returned if a non-integer is entered as the value of inc_votes.                                                                                                              |
| /api/articles/:article_id          | DELETE  | Ensures that the specified article is deleted, along with any associated comments. An error is returned if the article ID does not exist or a non-integer is entered.                                                                                                                                                                                   |
| /api/articles/:article_id/comments | GET     | Ensures that all comments from the specified article are served. An error is returned if the requested article ID does not exist or a non-integer is entered. Also ensures that the 4 valid queries (sort-by, order, limit and page) function as intended, returning an error if an invalid value is provided, or a page requested that does not exist. |
| /api/articles/:article_id/comments | POST    | Ensures that a new comment is posted to the specified article, serving the complete new comment. Ensures an error is returned if an invalid or non-existent article ID is entered. Also ensures that an error is returned if insufficient data is received in the body of the request                                                                   |
| /api/comments/:comment_id          | PATCH   | Ensures that the requested changes are made to the comment's vote property, serving the updated comment. Ensures that if additional keys are provided, they are ignored and that an error is returned if a non-integer is entered as the value of inc_votes.                                                                                            |
| /api/comments/:comment_id          | DELETE  | Ensures the specified comment is deleted and that an error is returned if the specified comment does not exist or a non-integer is entered                                                                                                                                                                                                              |

## Deployment

Providing you have accurately followed the above steps, the repository will be ready for deployment to a live system using a production database e.g. Heroku.

## Acknowledgments

* Northcoders Team for assistance and insight.
 
