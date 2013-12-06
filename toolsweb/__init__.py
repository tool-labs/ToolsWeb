# -*- coding: utf-8 -*-

import flask
import jinja2
import os.path
import oursql

def connect_to_database(database, host):
    default_file = os.path.expanduser('~/replica.my.cnf')
    if not os.path.isfile(default_file):
        raise Exception('Database access not configured for this account!')
    
    return oursql.connect(host=host, db=database,
                          read_default_file=default_file)

def connect_to_labsdb(project):
    return connect_to_database(database=project + '_p',
                               host=project + '.labsdb')

def create_app(name, template_package=None, template_path=None):
    app = flask.Flask(name)

    app_loader = app.jinja_loader
    if template_package is not None:
        app_loader = jinja2.PackageLoader(template_package)
    elif template_path is not None:
        app_loader = jinja2.FileSystemLoader(template_path)
    
    app.jinja_loader = jinja2.ChoiceLoader([
        app_loader,
        jinja2.PackageLoader('toolsweb'),
    ])

    return app

