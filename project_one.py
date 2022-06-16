import mysql.connector

#import maskpass
#passwd1 = maskpass.askpass(prompt="What is your MySQL password: ", mask="*")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "ButCanYouGuessThis#1", #passwd1,
    database = "Project_One"
)

mycursor = mydb.cursor()



#creating tables
#mycursor.execute("CREATE TABLE Orders (OrderID int PRIMARY KEY AUTO_INCREMENT, GameID int, FOREIGN KEY(GameID) References Games(GameID), CustomerID int, FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)") 

#Adding a column to a table
#mycursor.execute("ALTER Games ADD Price DECIMAL")

#Inserting values into a table
#mycursor.execute("INSERT INTO Customers (name, address, phone) VALUES ('Anthony Taylor', '193 Coffey Creek Suite 064 Port David DE 38909', '700-409-7604')")

#mycursor.execute("INSERT INTO Orders (Game, Customer, Price) VALUES ('Mega-Man', 'David Nagel', 5.00)")
# mycursor.execute("INSERT INTO Customers (Name, Address, Phone) VALUES ('Anthony Taylor', '441 Oakridge Lane', '847-273-9839')")
# mycursor.execute("INSERT INTO Games (Title, Platform, Price) VALUES ('Final Fantasy XIV', 'PC', '59.99')")
#mydb.commit()




def customerInfo():
    cusName = str(input('Please enter your full name: '))
    cusAddress = str(input('Please enter your address: '))
    cusPhone = str(input('Please enter your number: '))
    

    mycursor.execute("INSERT INTO Customers (Name, Address, Phone) VALUES (%s, %s, %s)", (cusName, cusAddress, cusPhone))
    mydb.commit()
    cusInfo = mycursor.execute("SELECT * FROM Customers ORDER BY CustomerID DESC LIMIT 1")
    print("Here is your customer information, please remember your ID number")
    for cusInfo in mycursor:
        print(cusInfo)
    
    


def addOrder():
    gameID = int(input("Please enter the ID of the game you wish to order: "))
    cusID = int(input("Please enter your customer ID: "))
    mycursor.execute("INSERT INTO Orders (GameID, CustomerID) VALUES (%s, %s)",(gameID, cusID))
    mydb.commit()
    
    gameOrder = mycursor.execute(f"SELECT Title, Platform, Price FROM Games WHERE GameID = {gameID}")
    for gameOrder in mycursor:
        print("Your order for:",gameOrder, "has been placed!")




def viewGames():
    allGames =  mycursor.execute("SELECT * FROM Games ORDER BY Title ASC")
    for allGames in mycursor:
        print(allGames)

def viewOrder():
    cusOrderID = int(input("Please enter your Customer ID number: "))
    myOrder =  mycursor.execute(f"SELECT * FROM Orders WHERE CustomerID = {cusOrderID}")
    for myOrder in mycursor:
        print("Here is your Order ID, ID of purchased game, and Customer ID:",myOrder)


def cancelOrder():
    OrderID = int(input("Please enter the Order ID of the purchase you wish to cancel: "))
    deleteOrder =  mycursor.execute(f"DELETE FROM Orders WHERE OrderID = {OrderID}")
    mydb.commit()
    print("The order has been canceled")



def startup():
    while True:
        print("Welcome to Nick's online game store!")
        print('Please input an option from the menu!')
        print('\t1. View current game selection')
        print('\t2. Add customer info')
        print('\t3. Place an order')
        print('\t4. View order')
        print('\t5. Cancel an order')
        print('\t6. Exit')
        break   
    while True:
        try:
            sel = int(input("\nSelection: "))  
        except ValueError:
            print(ValueError)
            print("Not valid input")
        if sel > 6:
            print("Not a valid input")
        else:
            break
    while True:
        if sel == 1:
            print("Our current selection of games")
            viewGames()
            print("Would you like to make another selection?")
            print('\t2. Place an order')
            print('\t3. View customer info')
            print('\t4. Add a game')
            print('\t5. Exit')
            sel = int(input("\nSelection: "))    
        elif sel == 2:
            print("Please enter your customer information")
            customerInfo()
            print("Would you like to make another selection?")
            print('\t1. View current game selection')
            print('\t3. Place an order')
            print('\t4. View order')
            print('\t5. Cancel an order')
            print('\t6. Exit')
            sel = int(input("\nSelection: ")) 
        
        elif sel == 3:
            addOrder()
            print('\t1. View current game selection')
            print('\t2. Add customer info')
            print('\t4. View order')
            print('\t5. Cancel an order')
            print('\t6. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 4:
            viewOrder()
            print('\t1. View current game selection')
            print('\t2. Add customer info')
            print('\t3. Place an order')
            print('\t5. Cancel an order')
            print('\t6. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 5:
            cancelOrder()
            print('\t1. View current game selection')
            print('\t2. Add customer info')
            print('\t3. Place an order')
            print('\t4. View order')
            print('\t6. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 6:
            quit()
        else:
            print("Not a valid input")

        


    
startup()

