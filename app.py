# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:23:59 2024

@author: carlo
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Heroku!'

if __name__ == '__main__':
    app.run(debug=True)

