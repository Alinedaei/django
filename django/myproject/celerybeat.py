from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Optional: Define periodic tasks
app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'your_project.tasks.my_periodic_task',
        'schedule': crontab(minute=0, hour=0),
    },
}

app.conf.timezone = 'UTC'

