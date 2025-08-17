FROM python:3.12.7

#install SSH client
RUN apt-get update && apt-get install -y openssh-client

#set environmental variables
ENV PYTHONUNBUFFERED 1

#set working directory
WORKDIR /app

#copy requirements.txt file
COPY requirements.txt /app/requirements.txt

#install python dependencies
RUN pip install -r requirements.txt

#copy the application to the working directory
COPY . /app/

#start the SSH tunnel
CMD python manage.py runserver 0.0.0.0:8000
