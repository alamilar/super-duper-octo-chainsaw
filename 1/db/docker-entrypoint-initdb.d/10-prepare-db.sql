--Creating events table

BEGIN;

CREATE TABLE events (
  timestamp       timestamp,
  type            varchar(1),
  payload         text
);

COMMIT;
