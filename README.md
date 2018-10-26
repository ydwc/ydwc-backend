# YDWC Members Database

This is a thin programmatic layer between the Postgres Database and the user. It will expose an API which can be used to add members to the database and query existing members.

To get set up with this repo:

1) Install virtualenv wrapper:
```
    pip install virtualenvwrapper
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv ydwc-members -p python
```

2) Install the dependencies
    `pip install -t lib -r requirements.txt`

3) Run the app locally
    `FLASK_APP=main.py FLASK_DEBUG=1 flask run`


To deploy changes to production:
1) Create a working branch where you make your changes. When you merge the
branch into master, it will automatically be deployed (there are no tests
at the moment :p)

