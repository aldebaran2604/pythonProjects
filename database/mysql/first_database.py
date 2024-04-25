import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "adminsecurity",
    password = "4XcSB}&TGWePe73^",
    database = "securityadministrator"
)

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM temp")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

connection.close()