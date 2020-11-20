import sqlite3
import csv

connection = sqlite3.connect("BadgeWatch_DB.db")
cursor = connection.cursor()

with open('2015_2020_CIP_Cases_Cleaned.csv', 'r') as PoliceFile:
    no_records = 0 
    for row in PoliceFile:
        values = row.split(",")
        values[8] = values[8].replace('\n', '')
        print(values)
        cursor.execute("INSERT INTO PoliceCases VALUES (?,?,?,?,?,?,?,?,?)", values)
    
        connection.commit()
        no_records += 1

        print("\n{} Police records transfered".format(no_records))

connection.close()