--Creating users and granting them rights to access db

BEGIN;

CREATE USER reader WITH PASSWORD 'reader';
GRANT SELECT ON events TO reader;

CREATE USER writer WITH PASSWORD 'writer';
GRANT INSERT ON events TO writer;

CREATE USER cTester WITH PASSWORD 'cTest';

COMMIT;
