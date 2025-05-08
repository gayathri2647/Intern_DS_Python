import sqlite3
import pandas as pd
df = pd.read_csv('student_habits_performance.csv')  
conn = sqlite3.connect('Academic.db')
cursor = conn.cursor()
df.to_sql('academic', conn, if_exists='replace', index=False)
cursor.execute("SELECT * FROM academic LIMIT 5")
print(cursor.fetchall())
conn.close()
