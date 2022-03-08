import multiprocessing

wsgi_app="app:app"
bind="localhost:5000"
workers=4
reload=True