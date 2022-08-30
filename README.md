## TO RUN DEFAULT CELERY WORKER windows
celery -A tg_site worker -l info -P gevent
## TO LAUNCH PERIODIC WORKER windows
python.exe -m celery -A tg_site beat --loglevel=info
## TO LAUNCH REDIS SERVER (windows port!)
redis-server --port 6379
## TO LAUNCH SERVER (waitress wsgi server)
>waitress wsgi server
>>production ready but better to launch gunicorn
>
python server.py &