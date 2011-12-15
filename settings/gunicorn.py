bind = "unix:/usr/local/gunicorn/gunicorn.sock"
pidfile = "/usr/local/gunicorn/gunicorn.pid"

#worker_class = 'eventlet'

workers = 6
timeout = 300
max_requests = 333

#preload_app = True