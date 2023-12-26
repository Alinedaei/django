# gunicorn_config.py
workers = 4
bind = "0.0.0.0:8000"
chdir = "/root/django/django/myproject/myproject"
module = "myproject.wsgi:application"

