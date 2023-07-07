# Installation Guide For Dev Server
Step 1 - get a new environment for python
python3 -m venv venv

Step 2 - activate the enviornment
For Linux:
source venv/bin/activate

Step 3 - install the dependencies
python -m pip install -r requirements.txt

Step 4 - launch the dev server
python manage.py runserver localhost:8000

View the web app by using the link localhost:8000