#It is where the identity of each person gets stored in a individual categories
class Address_per:#All of the information of the User will be describe and divided per person
    def __init__(self, U_fname,U_lname,U_add,U_contactnum):
        self.U_FirstName = U_fname 
        self.U_LastName = U_lname
        self.U_Address = U_add
        self.U_ContactNumber = U_contactnum

#The main list of this entire code
Address_Book_Main=[]

#To ask the user their respective information
def User_add_contact():
    User_fname=input("First Name: ")
    User_lname=input("Last Name: ")
    User_address=input("Address: ")
    User_contact_number= input("Contact Number: ")
    #Then this will add the user information to the instance of the class 
    Address_Book_Main.append(Address_per(User_fname,User_lname,User_address,User_contact_number))

#For the user to view all the contacts
def User_view_contact():
    if Address_Book_Main:
        for UserNum, userInput in enumerate(Address_Book_Main):#Enumerate- It shows the index or element
            print("_________________________")
            print(f"You are Number: {UserNum}")#To show the index of the User
            print(userInput.U_FirstName)
            print(userInput.U_LastName)
            print(userInput.U_Address)
            print(userInput.U_ContactNumber)
            print("_________________________")
    else:
        #If no contacts are added yet
        print("No User Detected!!!")

#For the user to edit the specific contact
def User_edit_contact():
    while True:
        User_view_contact()#It shows first the contacts so that the user know what to edit
        #Since the user already know the index of each contact they will know what to edit
        User_EntryNumber_edit= int(input("Input the number you want to edit? "))
        #So the user can choose what category they want to edit
        user_Change_Attributes= int(input("\n[1]First Name\n[2]Last Name\n[3]Address\n[4]Contact Number\nWhat you want to change? "))
        #If-Else Function for the categories
        if user_Change_Attributes == 1:
            Address_Book_Main[User_EntryNumber_edit].U_FirstName =input("Input new First Name: ") 
        elif user_Change_Attributes == 2:
            Address_Book_Main[User_EntryNumber_edit].U_LastName =input("Input new Last Name: ")
        elif user_Change_Attributes == 3:
            Address_Book_Main[User_EntryNumber_edit].U_Address =input("Input new Address: ")
        elif user_Change_Attributes ==4:
            Address_Book_Main[User_EntryNumber_edit].U_ContactNumber =input("Input new Contact Number: ")
        User_view_contact()
        break
        
#For the user to delete the specific contact 
def User_delete_contact():
    while True:
        User_view_contact()#It shows first the contacts so the user will know the input number to delete
        User_EntryNumber_delete = int(input("Input number you want to delete: "))
        Address_Book_Main.pop(User_EntryNumber_delete)#Pop- Delete the entire person and their information
        print("--User Deleted---")
        User_view_contact()#So it will update the remaining contacts
        break

#For the user to search for the contact by sort
def User_search_address_book():
    #This is to sort the contact by first name, last name, address, and contact number
    User_search = input("\n[a]First Name\n[b]Last Name\n[c]Address\n[d]Contact Number\nHow you would like to search a person? ")
    
    #If the user picks the first name
    if User_search =="a":
        Search_FirstName= input("What is the First Name? ")
        for User in Address_Book_Main:
            if User.U_FirstName.lower() == Search_FirstName.lower():
                print(f"First Name: {User.U_FirstName}\nLast Name: {User.U_LastName}\nAddress: {User.U_Address}\nContactNumber: {User.U_ContactNumber}")
    
    #If the user picks the last name
    elif User_search =="b":
        Search_LastName= input("What is the Last Name? ")
        for User in Address_Book_Main:
            if User.U_LastName.lower() == Search_LastName.lower():
                print(f"First Name: {User.U_FirstName}\nLast Name: {User.U_LastName}\nAddress: {User.U_Address}\nContactNumber: {User.U_ContactNumber}")

    #If the user picks the address
    elif User_search =="c":
        Search_Address= input("What is the Address? ")
        for User in Address_Book_Main:
            if User.U_Address.lower() == Search_Address.lower():
                print(f"First Name: {User.U_FirstName}\nLast Name: {User.U_LastName}\nAddress: {User.U_Address}\nContactNumber: {User.U_ContactNumber}")

    #If the user picks the contactnumber
    elif User_search =="d":
        Search_ContactNumber= input("What is the Contact Number? ")
        for User in Address_Book_Main:
            if User.U_ContactNumber.lower() == Search_ContactNumber.lower():
                print(f"First Name: {User.U_FirstName}\nLast Name: {User.U_LastName}\nAddress: {User.U_Address}\nContactNumber: {User.U_ContactNumber}")   

    
    else:
        #If the program doesnt find matches on what you want to search
        print("User doesn't exist")

    return

#This is the code for the User to pick choices on what they want to do in the address book
def function_address():
    while True:
        if len(Address_Book_Main) < 50: #This line of code is to limit the responses to up to 50 persons only
            print("--------------------------------------Address Book--------------------------------------")
            Address_book_source= input("\n1-Add Contact\n2-Edit Contact\n3-Delete Contact\n4-View Contact\n5-Search Address Book\n6-Exit\nWhat would you like to do?")
            if Address_book_source =="1":
                User_add_contact()
            elif Address_book_source =="2":
                User_edit_contact()
            elif Address_book_source =="3":
                User_delete_contact()
            elif Address_book_source=="4":
                User_view_contact()
            elif Address_book_source =="5":
                User_search_address_book()
            elif Address_book_source =="6":
                break
            else:
                #If the user press a button that is not indicated or called
                print("Invalid Action!!!")
        else:
            #If it reached the limit of responses 
            print("Maximum Limit has been reached")
            #If it reach the limit you can delete a contact 
            User_Delete=input("Do you want to lessen the number of students? Yes or No: ").lower()
            if User_Delete == "yes":
                User_delete_contact()
            else:
                break

function_address()