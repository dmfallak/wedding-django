FROM python:2
ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 8080
RUN unset -v PYTHONPATH
RUN pip2 install Django -t /app
COPY . /app
CMD [ "/usr/bin/python2", "./manage.py", "runserver", "0.0.0.0:8080", "--noreload" ]
