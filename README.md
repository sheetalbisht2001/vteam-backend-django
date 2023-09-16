# Install Dependencies

```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip freeze > requirements.txt
pip install -r requirements.txt
```


# Start Server

```bash
python manage.py runserver
```

# turn models into tables (migration)

```bash
python manage.py makemigration
python manage.py migrate
```