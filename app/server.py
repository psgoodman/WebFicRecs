import os
import sqlite3
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='psgoodman',
    PASSWORD='horrifically insecure'
))
app.config.from_envvar('WEBFICRECS_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    reader = csv.reader(open('rec_data.tsv', 'r'), delimiter='  ')
    for row in reader:
        to_db = []
        for i in range(row.len()):
            to_db[i] = unicode(row[i], "utf8")
        db.cursor().execute("INSERT INTO fics (id, title, url, synopsis, rating, " \
            "length, author, complete, mood, tvtropes) VALUES (?, ?, ?, ?, ?, " \
            "?, ?, ?, ?, ?);", to_db)
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


