from tg_site.celery import app
from .channel_lister import channel_lister
from .models import Channel
from django.db import transaction


@app.task(name='run_parser')
def run_parser():
    sid = transaction.savepoint()
    try:
        print('STARTED')
        channels=channel_lister()
        Channel.objects.all().delete()
        for channel in channels:
            ch_instance = Channel.objects.create(name=channel)
        transaction.savepoint_commit(sid)
        return "Success"
    except Exception as e:
        transaction.savepoint_rollback(sid)
        return "Failure"
