# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform TODO: Use env file.
try:
    conn = mariadb.connect(
        user="user",
        password="pa55word",
        host="192.0.2.1",
        port=3306,
        database="employees"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()