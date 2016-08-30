FROM postgres

ENV POSTGRES_USER XWing
ENV POSTGRES_PASSWORD YWing

ENV POSTGRES_DB db

VOLUME /var/lib/postgresql/data

RUN ["mkdir", "-p", "/docker-entrypoint-initdb.d"]
ADD docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
