# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

ARG UID

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install python-dev libpq-dev

WORKDIR /app
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./entrypoint.sh /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd -ms /bin/bash -u ${UID} appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# ENTRYPOINT [ "entrypoint.sh" ]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
