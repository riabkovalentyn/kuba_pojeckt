FROM django:latest
RUN apt-get update && apt-get install -y python-pip
RUN pip3 install django
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]