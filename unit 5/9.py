
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")

# Create cursor
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cur.execute("INSERT INTO student VALUES(1,'Amit',85)")
cur.execute("INSERT INTO student VALUES(2,'Rahul',90)")

# Execute SQL query
cur.execute("SELECT * FROM student")

# Display records
for row in cur.fetchall():
    print(row)

# Save changes
con.commit()

# Close connection
con.close()
