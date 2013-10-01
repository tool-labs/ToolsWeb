# -*- coding: utf-8 -*-

import flask
import jinja2
import os.path
import oursql

def connect_to_labs(database, host):
    default_file = os.path.expanduser('~/replica.my.cnf')
    if not os.path.isfile(default_file):
        raise Exception('Database access not configured for this account!')
    
    return oursql.connect(host=host, db=database,
                          read_default_file=default_file)

def connect_to_wiki(lang):
    wiki = lang + 'wiki'
    return connect_to_labs(database=wiki + '_p',
                           host=wiki + '.labsdb')

def create_app(name):
    app = flask.Flask(name)

    app.jinja_loader = jinja2.ChoiceLoader([
        jinja2.PackageLoader(name),
        jinja2.PackageLoader('toolsweb'),
    ])

    return app

