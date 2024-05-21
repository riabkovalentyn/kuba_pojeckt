import psycopg2

local_pgdb = 'weather_db'
hostname = '100.112.228.21'
port = '5432'
user = 'user-name'
password = 'strong-password'

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
    cursor.execute("INSERT INTO public.weather (weather_city, weather_temperature, weather_windspeed, weather_type) VALUES ('Kolin'::character varying, '13.211'::numeric, '35.15'::numeric, 'Windy'::character varying)")
    cursor.execute('SELECT * FROM public.weather ORDER BY weather_id ASC')
    connection.commit()
    print(cursor.fetchall())
finally:
    cursor.close()
