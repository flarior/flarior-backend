#!/usr/bin/env python
from flask import Flask
from flask.ext.script import Manager, Server
import os
from datetime import datetime


app = Flask(__name__)
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True
    )
)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    current_time = datetime.now()
    livereload_path = os.path.abspath('../flarior-frontend/app/livereload.txt')
    with open(livereload_path, 'w+') as livereload:
        livereload.write(str(current_time))
    manager.run()
