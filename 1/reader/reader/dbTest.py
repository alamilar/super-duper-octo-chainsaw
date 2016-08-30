#!/usr/bin/env python

import sys
import psycopg2

from time import sleep


print 'Hello from reader!'

while True:
    try:
        conn = psycopg2.connect("dbname='db' user='reader' host='db' password='reader'")
        conn.close()
        sys.exit(1)
    except:
        print 'Waiting for Postgres to kick in...'
        sleep(2)
