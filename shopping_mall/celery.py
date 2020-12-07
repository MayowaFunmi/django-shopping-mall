import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_mall.settings')
app = Celery('shopping_mall')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
