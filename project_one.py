import mysql.connector

import maskpass
passwd1 = maskpass.askpass(prompt="What is your MySQL password: ", mask="*")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = passwd1,
    database = "Project_One"
)

mycursor = mydb.cursor()

#creating tables
#mycursor.execute("CREATE TABLE Customers (ID int PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(255), Address VARCHAR(255), Phone VARCHAR(50))") 

#
mycursor.execute("ALTER Games ADD Price DECIMAL")