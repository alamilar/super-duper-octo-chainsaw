#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD='cTest' psql -h "$host" -U "ctester" -d db -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
