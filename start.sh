#!/bin/bash
source setenv.sh
nohup /usr/bin/python manage.py runserver 0.0.0.0:8080 --noreload&
