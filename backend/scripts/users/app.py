import mysql.connector
import csv

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="HOST",  # Remove 'mysql://' prefix
    user="USERNAME",  # Your MySQL username
    password="PASSWORD",  # Your MySQL password
    database="DATABASE",  # Your MySQL database
    port=PORT  # Your MySQL port
)

cursor = connection.cursor()

# Open your CSV file
with open('../users.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        cursor.execute("INSERT INTO users (user_id, username, email,password, role, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)

# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()
