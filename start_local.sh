#/bin/bash

# apply missing migrations if neccessary
python3 corp/manage.py migrate

# get the data
# You have to load them in this order or you break stuff
python3 corp/manage.py loaddata countries.json
python3 corp/manage.py loaddata states.json
python3 corp/manage.py loaddata universities.json
python3 corp/manage.py loaddata measures.json
python3 corp/manage.py loaddata implemented.json

# start our server
python3 corp/manage.py runserver
