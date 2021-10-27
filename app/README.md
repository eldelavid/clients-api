# Clients-api
Python app with flask, gunicorn and SQLalchemy to connecto to postgresql database.

## Prerequisities
In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

To run image:
```shell
docker run -p 5000:5000 --env-file database.conf clients-api
```
#### Environment Variables

Create file database.conf with following variables:

* `POSTGRES_USER` - PostgrSQL user.
* `POSTGRES_PASSWORD` - Postgres password.
* `POSTGRES_HOST` - Host where postgresql is running.
* `POSTGRES_DB` - Database name.
* `POSTGRES_PORT` - Database port.
