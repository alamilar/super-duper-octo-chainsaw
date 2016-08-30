#!/usr/bin/env bash

docker-compose rm $(docker-compose ps -q)

docker rmi -f $(docker images -q)

docker stop $(docker ps -aq)

docker rm -f $(docker ps -aq)
