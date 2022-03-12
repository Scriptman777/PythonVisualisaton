import mysql.connector

# Create function to use for reading data
def read_db(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# This script is an example and will not run without the specific MySQL database

# Create a connection object
connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Marketing")

# Create a query string
query = "SELECT * FROM MARKETING_DATA WHERE gender = 'F';"

# Read results from database - returns a tuple
result = read_db(query)

print(result)

# Example 2 with cursor

# Get cursor from connection
cursor = connection.cursor()

# Create query with parameters to be filled in later (from user input for example)
query = "SELECT * FROM MARKETING_DATA WHERE gender = %s OR has_card = %s;"

# Execute query with tuple of parameters
cursor.execute(query, ("M",0))

# Get list of all rows returned by query 
rows = cursor.fetchall()

print(rows)