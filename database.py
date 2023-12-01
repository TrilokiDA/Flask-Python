import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")
# conn.close()

c = conn.cursor()
c.execute('DELETE FROM students')
print('We have deleted', c.rowcount, 'records from the table.')
conn.commit()
conn.close()

# conn.execute("INSERT INTO students (name,addr,city,pin)VALUES ('hi','u','p','789456')")
# conn.commit()
# print("Records created successfully")
# conn.close()

# cursor = conn.execute("SELECT * from students")
# for row in cursor:
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print(row[3])
#
# print("Operation done successfully")
# conn.close()


# nm = 'triloki'
# addr = "Ban"
# city = "galore"
# pin = "123456"
# query = "INSERT INTO students (name,addr,city,pin) VALUES (?, ?, ?, ?)"
# data = [nm,addr,city,pin]
# cursor = conn.cursor()
# cursor.execute(query, data)
# conn.commit()

# Get the number of rows affected
# rows_affected = cursor.rowcount

# Verify result using the SQL SELECT query
# cursor.execute("SELECT * FROM students")
# results = cursor.fetchall()
# print(results)

# delete

# Close the cursor and connection
# cursor.close()
# conn.close()