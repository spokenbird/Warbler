# Warbler
### Python3 w/Flask Twitter clone

## To start

git clone in preferred folder && cd into project
```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
Create the database (this project uses PostgreSQL)
```
(venv) $ createdb warbler
(venv) $ python seed.py
```
Start the server w/ ```flask run```
