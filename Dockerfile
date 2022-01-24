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

ENTRYPOINT [ "gunicorn", "--workers=4", "-b", "127.0.0.1:5005", "--name=tele-schocken_server", "app:create_app()" ]
