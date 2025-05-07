import sqlite3

# Connect to the shelter.db file
conn = sqlite3.connect('shelter.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Example: Show all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Example: Query data from a specific table (replace 'your_table_name' with actual table name)
# cursor.execute("SELECT * FROM your_table_name LIMIT 5;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# Close the connection
conn.close()
