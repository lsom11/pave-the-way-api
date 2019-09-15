# Pave the way API

## Local running

### Download Virtual Env

`python3 -m pip install --user virtualenv`

### Create Virtual Env

`python3 -m venv env`

### Activate venv

`source env/bin/activate`

### Install packages

`pip install -r requirements.txt`

### Run app

`python3 run.py`

## Docker running

### Build the image

`docker build -t pave_the_way_image .`

### Run the image

`docker run --name pave-the-way-api -it -p 5050:5000 -d pave_the_way_image`

## Patterns used

Our api implements the builder pattern, as we use varius scrapers and AutoML to create a payload to send to the user

## Work 2

This API contains slack integration (slack folder), a CRUD to create a user (user folder) and an integration test for our search endpoint (search folder)
