import psycopg2
import csv
from datetime import datetime

conn = psycopg2.connect(
    dbname="testdb",  
    user="postgres",  
    password="password", 
    host="localhost",  
    port="5432"  
)

cursor = conn.cursor()


query = """
    SELECT
        c.first_name || ' ' || c.last_name AS full_name,
        cr.credit_number
    FROM
        CLIENT c
    JOIN RELATION r ON c.id = r.client
    JOIN CREDIT cr ON r.credit = cr.id
    WHERE
        cr.balance > 1000;
"""
cursor.execute(query)

rows = cursor.fetchall()

date_today = datetime.now().strftime("%d.%m.%Y")

filename = f'report_{date_today}.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Full Name', 'Credit Number'])  
    csvwriter.writerows(rows)  

cursor.close()
conn.close()

print(f"Данные успешно сохранены в файл {filename}")
