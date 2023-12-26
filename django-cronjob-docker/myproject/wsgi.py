# myproject/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from myproject.celery import celery_app
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
application.add_files(os.path.join(os.path.dirname(__file__), 'staticfiles'))
application.add_files(os.path.join(os.path.dirname(__file__), 'media'), prefix='media')

