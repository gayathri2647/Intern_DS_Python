import pandas as pd
import mysql.connector
from mysql.connector import Error

df = pd.read_csv('student_habits_performance.csv')

try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',                        
        database='studentdb'   
    )

    if connection.is_connected():
        cursor = connection.cursor()
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO habits (student_id, age, gender)
                VALUES (%s, %s, %s)
            """, (row['student_id'], row['age'], row['gender']))

        connection.commit()
        print("Data inserted successfully into 'habits' table.")

except Error as e: 
    print("Error while connecting to MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")    