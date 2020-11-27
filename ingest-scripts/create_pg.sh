#!/bin/bash

docker run --name dbt_trial -p 5432:5432 \
       -e POSTGRES_USER=bbradshaw -e POSTGRES_PASSWORD=pw \
       -e POSTGRES_DB=flights -d postgres:12.2

# Note now that the postgres instance has been created, you can
# enter the psql prompt by doing `docker exec -it [container_name] psql -U [postgres_user]`
