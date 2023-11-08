import mysql.connector

# Define the connection parameters
db_config = {
    "host": "localhost",  # Replace with the server's address
    "user": "root",  # Replace with your MySQL username
    "password": "",  # Replace with your MySQL password
    "database": "crud python",  # Replace with the name of your database
}

# Create a connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Perform CRUD operations as needed
# Example: Insert operation (Create)
insert_query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
values = (value1, value2)
cursor.execute(insert_query, values)

# Commit the changes for INSERT, UPDATE, DELETE operations
conn.commit()

# Example: Read operation
select_query = "SELECT * FROM mytable"
cursor.execute(select_query)
data = cursor.fetchall()
for row in data:
    print(row)

# Example: Update operation
update_query = "UPDATE mytable SET column1 = %s WHERE column2 = %s"
values = (new_value, target_value)
cursor.execute(update_query, values)
conn.commit()

# Example: Delete operation
delete_query = "DELETE FROM mytable WHERE column1 = %s"
value_to_delete = (value_to_delete,)
cursor.execute(delete_query, value_to_delete)
conn.commit()

# Close the connection
cursor.close()
conn.close()
