#!/usr/bin/env python

import sys
from datetime import datetime
import random
from loremipsum import get_sentences
from time import sleep

import psycopg2
try:
    conn = psycopg2.connect("dbname='db' user='writer' host='db' password='writer'")
except:
    print 'I am unable to connect to the database'
    sys.exit(1)


def main():
  cur = conn.cursor()
  while True:
    cur.execute('INSERT INTO events (timestamp, type, payload) VALUES (%s, %s, %s)', (
      datetime.now(),
      random.choice(['A', 'B', 'C', 'X', 'Y', 'Z']),
      ' '.join(get_sentences(5))
    ))
    conn.commit()
    sleep(1)


if __name__ == '__main__':
    main()
