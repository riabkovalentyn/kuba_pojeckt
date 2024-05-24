import psycopg2
import requests
import json
import time


local_pgdb = 'weather_db'
hostname = '100.112.228.21'
port = '5432'
user = 'user-name'
password = 'strong-password'
def weatherdatawrite(city, temperature, windspeed, wtype):
    query = "INSERT INTO public.weather (weather_city, weather_temperature, weather_windspeed, weather_type) VALUES ('"+city+"'::character varying, '"+str(temperature)+"'::numeric, '"+str(windspeed)+"'::numeric, '"+str(wtype)+"'::character varying)"
    try:
        # Establish the connection
        connection = psycopg2.connect(
            dbname=local_pgdb,
            user=user,
            password=password,
            host=hostname,
            port=port
        )
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.execute('SELECT * FROM public.weather ORDER BY weather_id ASC')
        connection.commit()
        print(cursor.fetchall())
    finally:
        cursor.close()
        
        
def dowloadweatherdata():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.5244&longitude=13.4105&current=temperature_2m,weather_code,wind_speed_10m'
    r = requests.get(url)
    data = json.loads(r.content)
    r.close()
    datareturnlist = [data['current']['temperature_2m'], data['current']['wind_speed_10m'], data['current']['weather_code'] ]
    return datareturnlist



while True:
    data = dowloadweatherdata()
    weatherdatawrite('Berlin', data[0], data[1], data[2])
    time.sleep(600)
