
## **Task**

Design and develop an API for a user survey system.


## **Functionality for the system administrator:**

- authorization in the system (registration is not required)
- adding/changing/ deleting polls. Survey attributes: name, start date, end date, description. 
- After creation, the "start date" field of the survey cannot be changed
- add/edit/delete questions in the survey. Question Attributes: question text, question type (answer in text, answer with a choice of one option, answer with a choice of several options)

## **Functionality for system users:**

- getting a list of active polls
- passing the survey: surveys can be conducted anonymously, a numeric ID is transmitted to the API as a user ID, which stores the user's answers to questions; one user can participate in any number of surveys
- receiving surveys completed by the user with details on the answers (what is selected) by the unique user ID

## **The result of the task:**

- application source code in github (only on github, public repository)
- instructions for deploying the application (in docker or locally)
- API documentation

## **Use the following technologies:**
- Django 2.2.10, 
- Django REST framework.

## **Conditions**

Estimated time to complete the test task:
- - 3-4 hours, the time is not strictly marked.
- You can start the test task at any time convenient for you.

The current test task has only a general description of the requirements, the specific details of the implementation are at the discretion of the developer.

# SurveySystem Tutorial
**Backend Dependencies/Packages
Create a virtualenv for Python 3
1.Head over to the terminal and run:**
```
virtualenv env 
```
**Replace env wih the actual name you want to give your Python virtual environment.
2.Activate the virtualenv**
```
source env/bin/activate
```

<h3>First we need to install all libraries
</h3>

```
!pip install -r requirements.txt
```
<h3> Start docker container</h3>

```
docker-compose up --build
```
#<h3> Link to HEROKU</h3> 

#<h3> Test Postman</h3>  

# create, list, update, delete

# Api Root
"quiz": "http://surveysystem-kiri.herokuapp.com/en-ru/api/v1/quiz/",
"choice": "http://surveysystem-kiri.herokuapp.com/en-ru/api/v1/choice/",
"user_answer": "http://surveysystem-kiri.herokuapp.com/en-ru/api/v1/user_answer/",
"question": "http://surveysystem-kiri.herokuapp.com/en-ru/api/v1/question/",
"get_user_answer": "http://surveysystem-kiri.herokuapp.com/en-ru/api/v1/get_user_answer/"

