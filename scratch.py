'''
General Scratch pad, typically cleared after troubleshooting is complete.


'''
import mysql.connector
import env

cnx = mysql.connector.connect(user=env.username, password=env.password, host=env.host_name,
                                           database=env.database)
cursor =cnx.cursor()
query = 'select * from employees_login'
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
cnx.close
for i in results:
    print(i)

self.emp_no_entry.get()

