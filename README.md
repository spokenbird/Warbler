# Warbler
### Twitter clone w/ Python3 and Flask
    Built with
    - Jinja
    - WTForms
    - SQLAlchemy
    - Bcrypt w/ Sessions for Auth


![Image](/static/images/warbler_screen.png?raw=true)

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

Visit localhost:5000 !

## For tests
```
$ FLASK_ENV=production python -m unittest <name-of-python-file>
OR
$ FLASK_ENV=production python -m unittest
```