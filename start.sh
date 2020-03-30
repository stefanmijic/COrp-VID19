#/bin/bash

# apply missing migrations if neccessary
python corp/manage.py migrate

# get the data
# You have to load them in this order or you break stuff
python corp/manage.py loaddata countries.json
python corp/manage.py loaddata states.json
python corp/manage.py loaddata universities.json
python corp/manage.py loaddata measures.json
python corp/manage.py loaddata implemented.json
python corp/manage.py loaddata corporations.json

# start our server
python corp/manage.py runserver 0.0.0.0:8000
