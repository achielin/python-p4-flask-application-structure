#!/usr/bin/env python3

from flask import Flask

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'
