import mysql.connector
from env import username, password, host_name, database
def get_conx():
    cnx = mysql.connector.connect(user=username, password=password, host=host_name, database=database)

    return cnx

def query_database(query):
    # Obtain a connection
    cnx = get_conx()

    # Create a new cursor
    cursor = cnx.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    return results

# Test the function
query = "SELECT * FROM employees_login"
print(query_database(query))