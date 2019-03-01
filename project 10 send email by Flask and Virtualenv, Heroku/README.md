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
 
 