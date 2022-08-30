import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_site.settings')

app = Celery('suai_serv')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone='UTC'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()