release: python3 manage.py makemigrations && python3 manage.py migrate
ps:scale web=1
web: gunicorn api.wsgi