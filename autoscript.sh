#!/bin/sh

# First, it ensures that the database exists (if not, it creates an empty one with the models)
env/bin/python manage.py migrate
env/bin/python manage.py makemigration

# Then, it runs the Django server
env/bin/python manage.py runserver