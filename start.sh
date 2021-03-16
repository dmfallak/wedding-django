#!/bin/bash
nohup docker run --env-file env.list -p 8080:8080 wedding-django > nohup.out &
