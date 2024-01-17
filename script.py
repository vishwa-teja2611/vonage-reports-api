import psycopg2
import json

# Replace these values with your database credentials
dbname = "call_logs"
user = "postgres"
password = ""
host = "localhost"

# Replace these values with your JSON file path and table/column names
json_file_path = "output.json"
table_name = "call_logs"
json_column_name = "json_column"

# Read JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = conn.cursor()

# Insert JSON data into the table
cursor.execute(f"INSERT INTO {table_name} ({json_column_name}) VALUES (%s)", (json.dumps(json_data),))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
