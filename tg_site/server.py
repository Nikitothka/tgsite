from waitress import serve
from tg_site.wsgi import application

if __name__ == '__main__':
    serve(app=application, host='localhost', port='8080', threads=10)