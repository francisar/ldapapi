#!/bin/bash
HOST=127.0.0.1
PORT=8888
SOCKET=/var/run/django.lock
MAXREQUESTS=0
MAXSPARE=5
MINSPARE=2
MAXCHILDREN=5
DAEMONIZE=True
PIDFILE=/var/run/django.pid
DEBUG=True
WORKDIR=/data/nginx/djangoproject/ldapapi
OUTLOG=log/outlog.log
ERRLOG=log/errlog.log
echo $HOST
python manage.py runfcgi host=$HOST port=$PORT  maxrequests=$MAXREQUESTS maxspare=$MAXSPARE minspare=$MINSPARE maxchildren=$MAXCHILDREN daemonize=$DAEMONIZE pidfile=$PIDFILE debug=$DEBUG outlog=$OUTLOG errlog=$ERRLOG workdir=$WORKDIR
