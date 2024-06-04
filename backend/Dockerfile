FROM python:3.11-alpine
RUN mkdir /app
COPY weatherCatcher.py /app/weatherCatcher.py
RUN pip install psycopg2-binary
RUN pip install requests
ENTRYPOINT python /app/weatherCatcher.py