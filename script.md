# Scripts

## django

```bash
python manage.py runserver # run the server
python manage.py makemigrations <app-name>
python manage.py migrate

python manage.py startapp <app-name> # create the app inside django project
```

```bash
python manage.py createsuperuser # create supper user

# export pip packages
pip freeze > requirements.txt
```

## i18n

```bash
django-admin makemessages -l <language code>
django-admin compilemessages
```
