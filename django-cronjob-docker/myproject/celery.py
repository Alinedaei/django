# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# ﺎﺴﻣ ﭖﺭﻭﮋﻫ ﻭ ﻢﺴﯾﺭ ﻑﺎﯿﻟ ﺖﻨﻈﯿﻣﺎﺗ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# ﺎﯿﺟﺍﺩ ﯽﮐ ﻦﻣﻮﻨﻫ ﺍﺯ ﮎﻼﺳ Celery
celery_app = Celery('myproject')

# Load configuration from Django settings
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# ﺎﺘﺻﺎﻟ ﺐﻫ Redis (ﻢﯾ<200c>ﺗﻭﺎﻨﯾﺩ ﻢﻗﺍﺪﯾﺭ ﺥﻭﺩ ﺭﺍ ﺏﺭ ﺎﺳﺎﺳ ﻦﯾﺍﺯ ﺖﻨﻈﯿﻣ ﮏﻨﯾﺩ)
celery_app.conf.broker_url = 'redis://redis:6379/0'

# Load tasks from all registered apps
celery_app.autodiscover_tasks()

