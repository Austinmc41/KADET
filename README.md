# Team JIC 354 - KADET
Application to automate the process of creating schedules for Emory's large number of med students.

# Release Notes

## 0.8 -2021-04-23

### Added
- Frontend react application

### Fixed
- added endpoints for accepting client request to run algoritm on backend
instead of using frontend, which would be poor separation of concerns.

### Known Issues
- 
# Install Guide

## Prerequisites
- Windows/Mac Computer with installation privileges

## Dependencies
- Docker
- Python3
- Django
  - django-rest-framework
  - django-cors-headers
- React
  - react
  - react-router-dom
  - react-dom
  - reactstrap
  - react-bootstrap
  - bootstrap
  - axios
## BACKEND ONLY:
## Docker Compose 1: container to run django app with gunicorn.
## Docker Compose 2: container to listen to  gunircorn container with nginx at port 80.
Both containers will have access to the static file and the shared volume.

- Python3
- Django
  - django-rest-framework
  - django-cors-headers
- React
  - react
  - react-router-dom
  - react-dom
  - reactstrap
  - react-bootstrap
  - bootstrap
  - axios


## Download Instructions
- run from terminal in mac git clone https://github.com/Austinmc41/KADET.git on your desktop
- run from Windows powershell git clone https://github.com/Austinmc41/KADET.git on your desktop

## Installation
- Install Python version >=3
- Django Dependencies
  - pip install django
  - pip install django-rest-framework 
  - pip install django-cors-headers

## Run Instructions

- cd into project folder KADET
- in /bin activate source with command: source activate
- cd into /backend enter command: python3 manage.py runserver 
- cd into /frontend enter command: npm start 
- navigate to localhost:3000 in browser link should show from command line


## Troubleshooting


