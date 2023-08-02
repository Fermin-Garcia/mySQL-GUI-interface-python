'''
General Scratch pad, typically cleared after troubleshooting is complete.


'''
import mysql.connector
import env

cnx =mysql.connector.connect(user=env.username, password=env.password, host=env.host_name,
                                           database=env.database)
cursor = cnx.cursor()

query = 'select * from employees_login;'

cursor.execute(query)
for n in cursor:
    print(n)

cursor.close()
cnx.close()

def send_query(self, query):
    self.cursor.execute(query)
    self.cursor.close()
    self.cnx.close()

    if cursor == None:
        pass
    else:
        return cursor
