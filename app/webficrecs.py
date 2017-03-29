import os
import sqlite3
import csv
import click
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'webficrecs.db'),
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
    reader = csv.reader(open('rec_data.tsv', 'r'), delimiter='\t')
    for row in reader:
        to_db = []
        for i in range(len(row)):
            to_db.append(unicode(row[i], "utf8"))
        db.cursor().execute("INSERT INTO fics (id, title, url, synopsis, rating, " \
            "comments, length, author, complete, mood, tvtropes) VALUES (?, ?, "\
            "?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
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

@app.route('/')
def show_entries():
    return render_template('show_entries.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/data')
def data():
    db = get_db()
    cur = db.execute('SELECT title, url, synopsis, rating, comments, length, ' \
        'author, complete, mood, tvtropes FROM fics ORDER BY id ASC')
    entries = cur.fetchall()
    dic = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in entries]
    # json_output = json.dumps(dic)
    return jsonify(dic)
