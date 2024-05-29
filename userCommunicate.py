import psycopg2
import requests
import time
import json


local_pgdb = 'weather_db'
hostname = '100.112.228.21'
port = '5432'
user = 'user-name'
password = 'strong-password'
def userdatawrite(usermail, password, ucity, ucelsius):
    query = "INSERT INTO public.users (user_mail, user_password, user_city, user_isCelsius) VALUES ('"+usermail+"'::text, '"+password+"'::text, '"+ucity+"'::character varying, '"+ucelsius+"'::boolean)"
    try:
        connection = psycopg2.connect(
            dbname=local_pgdb,
            user=user,
            password=password,
            host=hostname,
            port=port
        )
        cursor = connection.cursor()
        cursor.execute(query, (usermail, password, ucity, ucelsius))
        cursor.execute('SELECT * FROM public.users ORDER BY user_id ASC')
        connection.commit()
        print(cursor.fetchall())
    finally:
        cursor.close()
        connection.close()

while True:
    print("Welcome to the Weather Data Collector!")
    choice = input("Please choose an option: (1) Login, (2) Register, (3) Exit\n")

    if choice == "1":
        usermail = input("Enter your mail: ")
        password = input("Enter your password: ")
        user_id = login_user(mail, password)
        if user_id:
            for city in cities:
                data = downloadweatherdata(city['lat'], city['lon'])
                weatherdatawrite(user_id, city['name'], data[0], data[1], data[2])
            time.sleep(600)
    elif choice == "2":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        register_user(username, password)
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")