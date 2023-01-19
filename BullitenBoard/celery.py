import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BullitenBoard.settings')

app = Celery('BullitenBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'week_mails': {
        'task': 'Board.tasks.celery_week_mails',
        'schedule': crontab(minute='*/3'),
        'args': (),
    },
}