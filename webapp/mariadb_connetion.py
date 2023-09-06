import mysql.connector

dbconfig= { 'host' : '127.0.0.1',
            'user' : 'vsearch',
            'password' : 'password',
            'database' : 'vsearchlogDB', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """ insert into log 
           (phrase, letters, ip, browser_string, results)
           values
           ('hitch-hiker', 'aeiou', '127.0.0.1', 'Safari', 'set()');"""
cursor.execute(_SQL)
conn.commit()
_SQL = 'SELECT * FROM log;'
cursor.execute(_SQL)
for row in cursor.fetchall():
   print(row)

cursor.close()
conn.close()

