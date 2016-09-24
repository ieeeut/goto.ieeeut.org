#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

from flask import Flask,redirect
from flask import render_template

app = Flask(__name__)
app.secret_key = 'ieee_ut_harambe'

@app.route('/', methods=['GET', 'POST'])
def Home():
  return redirect('http://goto.kirmani.io')

@app.route('/<shortlink_query>')
def RedirectShortLink(shortlink_query=None):
  return redirect('http://goto.kirmani.io' + shortlink_query)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 33507))
  app.debug = True;
  app.run(host='0.0.0.0', port=port)
