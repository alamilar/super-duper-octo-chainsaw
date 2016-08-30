#!/usr/bin/env bash

#change directory to project root
cd ..

#swap configuration to proxy to reader2 version and reload
cp -f proxyDir/haproxy.cfg.2 proxyDir/haproxy.cfg
docker kill -s HUP proxy

#rebuild reader1
docker-compose stop reader31
docker-compose build reader31
docker-compose up -d --no-deps reader31

#swap configuration to proxy to reader1
cp -f proxyDir/haproxy.cfg.1 proxyDir/haproxy.cfg
docker kill -s HUP proxy

#rebuild reader2
docker-compose stop reader32
docker-compose build reader32
docker-compose up -d --no-deps reader32

#swap configuration to balanceload configuration
cp -f proxyDir/haproxy.cfg.both proxyDir/haproxy.cfg
docker kill -s HUP proxy
