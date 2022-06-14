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
#mycursor.execute("CREATE TABLE Games (GameID int PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(255), Platform VARCHAR(255), Price VARCHAR(50))") 

#Adding a column to a table
#mycursor.execute("ALTER Games ADD Price DECIMAL")

#Inserting values into a table
#mycursor.execute("INSERT INTO Customers (name, address, phone) VALUES ('Anthony Taylor', '193 Coffey Creek Suite 064 Port David DE 38909', '700-409-7604')")

# mycursor.execute("INSERT INTO Orders (Game, Customer, Price) VALUES ('Mega-Man', 'David Nagel', 5.00)")
# mycursor.execute("INSERT INTO Customers (Name, Address, Phone) VALUES ('David Nagel', '441 Margaret Loop Whiteland GA 11670', '374-343-7974')")
#mycursor.execute("INSERT INTO Games (Title, Platform, Price) VALUES ('Mega-Man', 'Playstation', '4.99')")
#mydb.commit()



# for x in mycursor:
#     print(x)



# def addGame():
#     mycursor.execute("INSERT INTO Games (Title, Platform, Price) VALUES ('Mega-Man', 'Playstation', 5.00)")


# def addCustomer():
#     print("Please input Customer information:")
#     mycursor.execute("INSERT INTO Customers (Name, Address, Phone) VALUES ('David Nagel', '441 Margaret Loop Whiteland GA 11670', '374-343-7974')") 

# def addOrder():
#     mycursor.execute("INSERT INTO Orders (Game, Customer, Price) VALUES ('Mega-Man', 'David Nagel', 5.00)")



def viewGames():
    allGames =  mycursor.execute("SELECT Title, Price FROM Games ORDER BY Title ASC")
    for allGames in mycursor:
        print(allGames)

#viewGames()

def startup():
    while True:
        print("Welcome to Nick's online game store!")
        print('Please input an option from the menu!')
        print('\t1. View current game selection')
        print('\t2. Place an order')
        print('\t3. View customer info')
        print('\t4. Add a game')
        print('\t5. Exit')
        break
    while True:
        try:
            sel = int(input("\nSelection: "))  
        except ValueError:
            print(ValueError)
            print("Not valid input")
        if sel > 5:
            print("Not a valid input")
        else:
            break
    if sel == 1:
        print("Our current selection of games")
        viewGames()
    

    


startup()

