# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# تنظیمات Django را به Celery بگویید
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')

# استفاده از تنظیمات Django برای تنظیمات Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# خطوط زیر برای اتصال به Redis هستند. اگر از بروکر دیگری استفاده می‌کنید، تنظیمات را مطابق با بروکر خود تغییر دهید.
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'

# اجرای تسک‌ها در هنگام استارت Celery
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

