# !/usr/bin/env python3
import sys

from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))

import app

application = app.app
'''
cat /etc/supervisor/conf.d/todo.conf

[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:3000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
'''