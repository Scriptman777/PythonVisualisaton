import mysql.connector

# This script is an example and will not run without the specific MySQL database

# Create a connection object
connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Test")

# Create a query string
query = "SELECT column FROM table WHERE condition = '1';"

# Read results from database - returns a tuple
result = read_db(query)



# Example 2 with cursor

# Get cursor from connection
cursor = connection.cursor()

# Create query with parameters to be filled in later (from user input for example)
query = "SELECT column FROM table WHERE condition = %s OR condition2 = %s;"

# Execute query with tuple of parameters
cursor.execute(query, (1,2))

# Get list of all rows returned by query 
rows = cursor.fetchall()