#!/usr/bin/env python

import sys
import json

import psycopg2
try:
    conn = psycopg2.connect("dbname='db' user='reader' host='db2' password='reader'")
except:
    print 'I am unable to connect to the database'
    sys.exit(1)


from flask import Flask
app = Flask(__name__)

@app.route('/stats')
def stats():
    cur = conn.cursor()
    cur.execute('SELECT type, count(*) FROM events GROUP BY type')
    rows = cur.fetchall()
    cur.close()
    return json.dumps(dict(map(lambda x: (x[0], int(x[1])), rows)))

@app.route('/stats/<logType>')
def statOfSpecificType(logType):
    cur = conn.cursor()
    cur.execute('SELECT timestamp FROM events WHERE type = %s ORDER BY timestamp DESC LIMIT 1', logType)
    rows = cur.fetchall()
    cur.close()
    result = {'type' : logType, 'timestamp' : str(rows[0][0])}
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
