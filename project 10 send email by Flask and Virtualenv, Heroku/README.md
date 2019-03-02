### Application that sends email using Python for backend and Html for frontend.

It also uses virtualenv and is hosted by Heroku.

---
In order to make the virtual environment inside the website root folder, we run this:
```
python -m venv virtual
```

the boilerplate will be made inside a new folder called virtual, inside the root folder.

For Flask to work, we need to have two more folders:

1- static
2- templates

We will add our html files inside templates, and css and js inside static folder.

- for the css link we can add 
```
../static/main.css
```
 in the beginning of the css url. it means go one level up and then go to static folder.
 
 
- For installing Flask, we have to navigate to:
```
virtual/Scripts
```
Then we run:
```
pip install flask
```

Then we need to make a python file in the root. we call it app.py

For having PostgreSQL connected we need to install 2 libraries while we are still in virtual environment:

1) psycopg2
2) flask-SQLAlchemy

When we want to create the table and all fields, we won't run the whole app, because we made the name of the python file app.py not main.py. we can run python in the console and create all objects like this:
```
>>> from app import db
    db_create_all()
```

After running this, we will have the table made in PostgreSQL.

