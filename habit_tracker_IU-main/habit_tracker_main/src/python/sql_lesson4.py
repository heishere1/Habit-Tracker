# Import the built-in 'sqlite3' library to work with SQLite databases      in Python
import sqlite3

conn = sqlite3.connect("shelter.db")

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS dogs (
id INTEGER PRIMARY KEY, -- Unique ID assigned to each dog
(auto-incremented)
name TEXT, -- Name of the dog (e.g., Bella)
breed TEXT, -- Dog's breed (e.g., Labrador)
color TEXT, -- Color of the dog (e.g., golden)
sex TEXT, -- Dog's sex (e.g., Male or Female)
intake_date TEXT -- Date the dog arrived at the
shelter)
''')
# 
cursor.execute('''
CREATE TABLE IF NOT EXISTS vaccinations (
id INTEGER PRIMARY KEY, -- Unique ID for the vaccine record
dog_id INTEGER, -- ID of the dog that received the
vaccine
vaccine_name TEXT, -- Name of the vaccine (e.g.,
Rabies)
date_given TEXT, -- Date when the vaccine was
administered
FOREIGN KEY(dog_id) REFERENCES dogs(id) -- Links dog_id to the ID
in the dogs table
)
''')
# ----------------------------------------------
# CREATE TABLE: adoptions
# ----------------------------------------------
# This table tracks which dogs have been adopted and by whom
cursor.execute('''
CREATE TABLE IF NOT EXISTS adoptions (
id INTEGER PRIMARY KEY, -- Unique ID for the adoption record
dog_id INTEGER, -- ID of the adopted dog
adopter_name TEXT, -- Name of the person who adopted
the dog
adoption_date TEXT, -- Date when the adoption took place
FOREIGN KEY(dog_id) REFERENCES dogs(id) -- Link dog_id to the
'dogs' table
)
''')
# ----------------------------------------------
# CREATE TABLE: staff
# ----------------------------------------------
# This table holds information about shelter staff members
cursor.execute('''
CREATE TABLE IF NOT EXISTS staff (

id INTEGER PRIMARY KEY, -- Unique ID for each staff member
name TEXT, -- Staff member's name
role TEXT, -- Their job role (e.g., Vet,
Cleaner)
email TEXT -- Contact email
)
''')
# ----------------------------------------------
# INSERT SAMPLE DATA INTO TABLES
# ----------------------------------------------
# Insert a new dog named Bella into the 'dogs' table
# The question marks (?) are placeholders for the values
cursor.execute("""INSERT INTO dogs (name, breed, color, sex, intake_date) VALUES (?, ?, ?, ?, ?)""",
("Bella", "Labrador", "Golden", "Female", "2024-05-01"))
# Add a vaccine record for Bella (assuming Bella has ID = 1)
cursor.execute("INSERT INTO vaccinations (dog_id, vaccine_name,date_given) VALUES (?, ?, ?)",
(1, "Rabies", "2024-05-02"))
# Record that Bella has been adopted by a person named Emily Johnson
cursor.execute("INSERT INTO adoptions (dog_id, adopter_name,adoption_date) VALUES (?, ?, ?)",
(1, "Emily Johnson", "2024-05-10"))
# Add a staff member named Dr. Green to the 'staff' table
cursor.execute("INSERT INTO staff (name, role, email) VALUES (?, ?,?)",
("Dr. Green", "Vet", "dr.green@shelter.org"))
# ----------------------------------------------
# SAVE CHANGES AND CLOSE CONNECTION
# ----------------------------------------------
# Commit all the changes to the database file (write everything to disk)
conn.commit()
# Close the connection to free up resources
conn.close()


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
