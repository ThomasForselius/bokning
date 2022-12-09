release: python manage.py makemigrations && python manage.py migrate
ps:scale web=1
web: gunicorn api.wsgi