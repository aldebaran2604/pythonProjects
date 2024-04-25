import sqlite3

connection = sqlite3.connect("database/sqlite/firstdb.db")


#connection.execute(
#    """
#    CREATE TABLE users (id INTEGER primary key, name VARCHAR(50))
#    """
#)

#connection.execute(
#    """
#    INSERT INTO users(id, name) VALUES(3, 'X')
#    """
#)

cursor = connection.execute("SELECT * FROM users")

listUsers = cursor.fetchall()

for x in listUsers:
  print(x[1])

#connection.commit()

connection.close()