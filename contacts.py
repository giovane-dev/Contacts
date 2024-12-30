import mysql.connector as MySql
conn=MySql.connect(
    host= 'localhost',
    user='root',
    password='your database password',
    database='your database name',
    port=4000
)
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
               ID INT PRIMARY KEY,
               Name VARCHAR (255),
               Phone VARCHAR(20)
               )''')

cursor.execute('SELECT ID FROM contacts')
id_check = [row[0] for row in cursor.fetchall()]

while True:
    print("1 - Insert contact")
    print("2 - Update contact")
    print("3 - Show contact")
    print("4 - Show contacts")
    print("5 - Delete contact")
    print("0 - Exit")
    try:
        option = int(input("Choose an option: "))
        if option == 0:
            break
        elif option == 1:
            id= int(input("Enter id:"))
            if id in id_check:
                print('===============================')
                print("ID already exists")            
                print('===============================')
            else:    
                name = input("Enter the Name: ")
                phone = input("Enter the Phone: ")
                if len(phone) <= 11 and phone.isdigit():
                    cursor.execute(f"INSERT INTO contacts (ID,Name,Phone) VALUES ({id},'{name}',{phone})" )
                    conn.commit()
                    print('===============================')
                    print("Contact inserted successfully")
                    print('===============================')
                else:
                    print('===============================')
                    print("Invalid phone number")
                    print('===============================')
                    
        elif option ==2:
            id = int(input("Enter id:"))
            if id in id_check:
                print("1 - Update Name\n2 - Update Phone number")
                opt = int(input("Choose an option: "))
                if opt == 1:
                    name = input("Enter the Name: ")
                    cursor.execute(f"UPDATE contacts SET Name = '{name}' WHERE ID = {id}")
                    conn.commit()
                    print('===============================')
                    print("Contact updated successfully")
                    print('===============================')
                elif opt == 2:
                    phone = input("Enter the Phone number: ")
                    if len(phone) <= 11 and phone.isdigit():
                        cursor.execute(f"UPDATE contacts SET Phone = {phone} WHERE ID = {id}")
                        conn.commit()
                        print('===============================')
                        print("Contact updated successfully")
                        print('===============================')
                    else:
                        print('===============================')
                        print("Invalid phone number")
                        print('===============================')
                else:
                    print('===============================')
                    print("Invalid option")
                    print('===============================')

            else:
                print('===============================')
                print("ID does not exist")
                print('===============================')
        elif option == 3:
            id = int(input("Enter id:"))
            if id in id_check:
                cursor.execute(f"SELECT Name FROM contacts WHERE ID = {id}")
                name = cursor.fetchone()[0]
                print('===============================')
                print(f"This id belong to {name}")
                print('===============================')
            else:
                print('===============================')
                print("ID does not exist")
                print('===============================')
        elif option == 4:
            cursor.execute('SELECT * FROM contacts')
            contacts = cursor.fetchall()
            print('===============================')
            for contact in contacts:
                print(contact)
            print('===============================')    
        elif option == 5:
            id = int(input("Enter id:"))
            if id in id_check:
                cursor.execute(f"DELETE FROM contacts WHERE ID = {id}")
                conn.commit()
                print('===============================')
                print("Contact deleted successfully")
                print('===============================')
            else:
                print('===============================')
                print("ID does not exist")
                print('===============================')
        else:
            print('===============================')
            print("Invalid option")
            print('===============================')
    except ValueError:
        print('===============================')
        print("Invalid input")
        print('===============================')

            

