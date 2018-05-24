#!/usr/bin/env python3

import pymysql.cursors
from datetime import datetime
import os, sys, time
import Adafruit_DHT as dht

sensor = 22
pin = 4
pin2 = 18

humidity, temperature = dht.read_retry(sensor, pin)
if (humidity is not None) and (temperature is not None):
        nowtime = datetime.strftime(datetime.now(), "%Y-%d-%m %H:%M:%S")
        temperature = float(temperature)
        humidity = float(humidity)
        temperature = round(temperature,1)
        humidity = round(humidity,1)

#        print(nowtime + "\t" + temperature + "C\t" + humidity +"%")
        print(temperature)
        print(humidity)

humidity2, temperature2 = dht.read_retry(sensor, pin2)
if (humidity2 is not None) and (temperature2 is not None):
        nowtime = datetime.strftime(datetime.now(), "%Y-%d-%m %H:%M:%S")
        temperature2 = float(temperature2)
        humidity2 = float(humidity2)
        temperature2 = round(temperature2,1)
        humidity2 = round(humidity2,1)

#        print(nowtime + "\t" + temperature + "C\t" + humidity +"%")
        print(temperature2)
        print(humidity2)

# Подключиться к базе данных.
connection = pymysql.connect(host='192.168.1.46',
                             user='psp2',
                             password='9546595465mysql2',
                             db='climat',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# print("connect successful!!")

sql = """
        INSERT  INTO sens1 VALUES (%s, %s, %s, %s)
      """

sql2 = """
        INSERT  INTO sens2 VALUES (%s, %s, %s, %s)
      """

#Первый датчик
val_0 = None
val_1 = None
val_2 = temperature
val_3 = humidity

data_employee = (val_0, val_1, val_2, val_3)

print(data_employee)

# Инициализируем курсор
cursor=connection.cursor()

# Выполнем запрос с данными
cursor.execute(sql, data_employee)

# Это - сохранить транзакцию о добавлении записи!!!!!!!!
connection.commit()

#Второй датчик
val_0 = None
val_1 = None
val_2 = temperature2
val_3 = humidity2

data_employee = (val_0, val_1, val_2, val_3)

print(data_employee)

# Инициализируем курсор
cursor=connection.cursor()

# Выполнем запрос с данными
cursor.execute(sql2, data_employee)

# Это - сохранить транзакцию о добавлении записи!!!!!!!!
connection.commit()



#Закрыть соединение
connection.close()
