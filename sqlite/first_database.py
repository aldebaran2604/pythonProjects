import sqlite3

connection = sqlite3.connect("sqlite/firstdb.db")


#connection.execute(
#    """
#    CREATE TABLE users (id INTEGER primary key, name VARCHAR(50))
#    """
#)

connection.execute(
    """
    INSERT INTO USERS(id, name) VALUES(3, 'X')
    """
)


connection.commit()

connection.close()