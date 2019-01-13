# Project description

Python project is located in pytest_project location. Second part contains docker files which install dependencies and run tests.

## pytest_project 
- __Pages__ - pages related classes 
- __Tests__:
    - __integration__ - integration test for updating device. Created using Tavern.
    - __ui__ - user interface test basing on pytest and selenium.
    - __conftest__ - basic pytest configuration file.
- __requirements.txt__ - python dependencies installed via pip.

## docker files 
- __Dockerfile__ - defines docker image with pytest_project.
- __docker-compose.yml__ - defines:
    - image's dependencies (in this case selenium chrome),
    - ports on which selenium is listening,
    - command to run automated tests.

In order to run all tests navigate to project's root directory and execute "__docker-compose up__".