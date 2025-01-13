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
with open('productimages.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    #product_id,name,description,price,stock,category_id,created_at,updated_at
    #image_id,product_id,image_url
    #1,1,https://kodnest-docs.b-cdn.net/salessavvy/COSTOMER%20IMAGES/shirt1.png
    for row in csv_reader:
        cursor.execute("INSERT INTO productimages (image_id, product_id, image_url) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))

# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()

