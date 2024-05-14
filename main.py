import psycopg2

conn = psycopg2.connect("dbname=weather_db user=rabkovalen@gmail.com password=Panzer58 host=localhost port=5432")

cur = conn.cursor()

cur.execute('INSERT INTO users ( user_id, user_mail, user_password, user_city, user_isCelsius )'
             'VALUES (%s, %s, %s, %s, %s)',  ) #need to add value inputs

conn.commit()

cur.close()
conn.close()
