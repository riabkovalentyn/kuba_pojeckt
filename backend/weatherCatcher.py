import psycopg2
import requests
import time
import json
import datetime


local_pgdb = 'weather_db'
hostname = '100.112.228.21'
port = '5432'
user = 'user-name'
password = 'strong-password'

cities = [
    {"name": "Baker Island", "lat": 0.1936, "lon": -176.476},
    {"name": "Alofi", "lat": -19.0595, "lon": -169.9187},
    {"name": "Honolulu", "lat": 21.3069, "lon": -157.8583},
    {"name": "Papeete", "lat": -17.5516, "lon": -149.5585},
    {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"name": "Chihuahua", "lat": 28.632, "lon": -106.0691},
    {"name": "Guatemala City", "lat": 14.6349, "lon": -90.5069},
    {"name": "Bogotá", "lat": 4.711, "lon": -74.0721},
    {"name": "Caracas", "lat": 10.4806, "lon": -66.9036},
    {"name": "Buenos Aires", "lat": -34.6037, "lon": -58.3816},
    {"name": "Grytviken", "lat": -54.2811, "lon": -36.5092},
    {"name": "Praia", "lat": 14.933, "lon": -23.5133},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Cairo", "lat": 30.0444, "lon": 31.2357},
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
    {"name": "Baku", "lat": 40.4093, "lon": 49.8671},
    {"name": "Islamabad", "lat": 33.6844, "lon": 73.0479},
    {"name": "Nur-Sultan", "lat": 51.1694, "lon": 71.4491},
    {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018},
    {"name": "Beijing", "lat": 39.9042, "lon": 116.4074},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "Brisbane", "lat": -27.4698, "lon": 153.0251},
    {"name": "Honiara", "lat": -9.4456, "lon": 159.9729},
    {"name": "Suva", "lat": -18.1248, "lon": 178.4501},
    {"name": "Nukualofa", "lat": -21.1394, "lon": -175.2048},
    {"name": "Kiritimati", "lat": 1.8709, "lon": -157.363},
]


def weather_data_write(city, temperature, windspeed, wtype, wdate):
    query = "INSERT INTO public.weather (weather_city, weather_temperature, weather_windspeed, weather_type, weather_date) VALUES ('"+city+"'::character varying, '"+str(temperature)+"'::numeric, '"+str(windspeed)+"'::numeric, '"+str(wtype)+"'::character varying)+"+str(wdate)+"::date);"'"
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
        cursor.execute(query, (city, temperature, windspeed, wtype, wdate))
        cursor.execute('SELECT * FROM public.weather ORDER BY weather_id ASC')
        connection.commit()
        print(cursor.fetchall())
    finally:
        cursor.close()
        connection.close()
        
        
def download_weather_data(lat, lon):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m'
    r = requests.get(url)
    data = json.loads(r.content)
    r.close()
    datareturnlist = [data['current']['temperature_2m'], data['current']['weather_code'], data['current']['wind_speed_10m']]
    return datareturnlist


while True:
    for city in cities:
        data = download_weather_data(city['lat'], city['lon'])
        weather_data_write(city['name'], data[0], data[1], data[2])
        time.sleep(25)

