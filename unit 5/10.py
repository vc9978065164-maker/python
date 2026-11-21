
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")

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
cur.execute("DELETE FROM student")
cur.execute("INSERT INTO student VALUES(1,'Amit',85)")
cur.execute("INSERT INTO student VALUES(2,'Rahul',90)")
cur.execute("INSERT INTO student VALUES(3,'Neha',95)")

con.commit()

# Fetch one record
cur.execute("SELECT * FROM student")
print("Fetch One:")
print(cur.fetchone())

# Fetch two records
cur.execute("SELECT * FROM student")
print("Fetch Many:")
print(cur.fetchmany(2))

# Fetch all records
cur.execute("SELECT * FROM student")
print("Fetch All:")
print(cur.fetchall())

con.close()
