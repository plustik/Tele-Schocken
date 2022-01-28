# syntax=docker/dockerfile:1
FROM docker.io/python:bullseye AS pybase_img

EXPOSE 5005

WORKDIR /usr/src/tele-schocken

# Install Gunicorn server
RUN pip install gunicorn

# Install python requirements:
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY ./backend .


ENV TELESCHOCKEN_CONFIG_FILE=/etc/tele-schocken/tele-schocken.cfg

ENTRYPOINT [ "gunicorn", "--access-logfile", "/var/tele-schocken/access.log", "--error-logfile", "/var/tele-schocken/error.log", "--workers=1", "--threads", "4", "-b", "0.0.0.0:5005", "--name=tele-schocken_server", "teleschocken:app" ]
