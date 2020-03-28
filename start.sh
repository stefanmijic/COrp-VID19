#/bin/bash

# apply missing migrations if neccessary
python corp/manage.py migrate

# get the data
python corp/manage.py loaddata states.json
python corp/manage.py loaddata universities.json

# start our server
python corp/manage.py runserver 0.0.0.0:8000

