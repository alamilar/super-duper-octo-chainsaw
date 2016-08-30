#!/usr/bin/env bash

docker-compose rm $(docker-compose ps -q)

docker rmi $(docker images -q)

docker stop $(docker ps -aq)

docker rm $(docker ps -aq)
