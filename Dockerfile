FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookstore


RUN pip install pipenv
COPY Pipfile Pipfile.lock /bookstore/
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /bookstore/ 
# EXPOSE 8001
# CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8001",]
