from tkinter import *
import csv
from tkinter import messagebox
from tkinter import ttk

#The Package for the window
Address_Book_GUI = Tk()
#The main List for this entire code
Address_Book_Main=[]
#Main Title for the GUI
Label(Address_Book_GUI, text="ADDRESS BOOK", font=("Helvetica", 18, "bold"), fg="white", bg="cyan3").pack(padx=10, pady=10)

#The choices in sorting the List
sortUser = [
            "First Name",
            "Last Name",
            "Address",
            "Contact"
        ]

#To read and extract the files from the CSV
def readCSV_USER():
    global header
    with open('AddressBookData.csv') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            Address_Book_Main.append(row)
    Display_User_Box()		

#To add the data or information in the CSV
def writeCSV_USER(addList):
    with open('AddressBookData.csv','w',newline='') as csv_file:
        writeobj = csv.writer(csv_file,delimiter=',')
        writeobj.writerow(header)
        for row in addList:
            writeobj.writerow(row)

#The format of the window
def Address_Book_Format():
    Address_Book_GUI.geometry('600x330')
    Address_Book_GUI.config(bg ="cyan3")
    Address_Book_GUI.resizable(0,0)
    Address_Book_GUI.title("Address Book")
Address_Book_Format()

#Where the User's information gets stored
def Address_Book_Class():
    global U_FirstName, U_LastName, U_Address, U_ContactNumber
    U_FirstName = StringVar()
    U_LastName= StringVar()
    U_Address= StringVar()
    U_ContactNumber= StringVar()
Address_Book_Class()

#Where the user can input their information
def Address_Book_Titles():
    Label(Address_Book_GUI, text= "First Name:", font= "Helvetica 14 bold", bg= "cyan3", foreground="white" ).place(x=73, y= 80)
    Entry(Address_Book_GUI, textvariable = U_FirstName, font= "Arial 12", bg= "cadetblue4", foreground="white").place(x= 190, y=85)
    Label(Address_Book_GUI, text= "Last Name:", font= "Helvetica 14 bold", bg= "cyan3", foreground="white" ).place(x=75, y= 110)
    Entry(Address_Book_GUI, textvariable = U_LastName, font= "Arial 12", bg= "cadetblue4", foreground="white").place(x= 190, y=115)
    Label(Address_Book_GUI, text= "Address:", font= "Helvetica 14 bold", bg= "cyan3", foreground="white" ).place(x=93, y= 140)
    Entry(Address_Book_GUI, textvariable = U_Address, font= "Arial 12", bg= "cadetblue4", foreground="white").place(x= 190, y=145)
    Label(Address_Book_GUI, text= "Contact Number:", font= "Helvetica 14 bold", bg= "cyan3", foreground="white" ).place(x=20, y= 172)
    Entry(Address_Book_GUI, textvariable = U_ContactNumber, font= "Arial 12", bg= "cadetblue4", foreground="white").place(x= 190, y=177)
Address_Book_Titles()

#The format and the code for the combobox
def userSearchDropdownFormat():
    global searchUser
    searchUser= ttk.Combobox(Address_Book_GUI, value = sortUser, height=10, width= 10, font= "Helvetica 10")
    searchUser.current(0)
    searchUser.place(x=500, y=50)
userSearchDropdownFormat()

#The format and the code fpr the searchbar
def userSearchBoxFormat():
    global userEntrySearch
    userEntrySearch = Entry(Address_Book_GUI, font="Helvetica 10", width= 16 )
    userEntrySearch.place(x=380, y=50)
userSearchBoxFormat()

#This code to display the information of the user to the listbox 
def Address_Book_List():#The format for the listbox
    global main_box_Store_USER
    main_Store_USER= Frame(Address_Book_GUI)
    main_Store_USER.place(x=380, y= 80)
    scroll_Store=Scrollbar(main_Store_USER, orient= VERTICAL)#To add scroll function
    #The code for the listbox
    main_box_Store_USER = Listbox(main_Store_USER, yscrollcommand= scroll_Store.set, height=14, width=27, font="Helvetica 10 bold", background= "cadetblue4", foreground= "white")
    scroll_Store.config (command=main_box_Store_USER.yview)
    scroll_Store.pack(side=RIGHT, fill=Y)
    main_box_Store_USER.pack(side=LEFT,  fill=BOTH, expand=1)
Address_Book_List()

#This returns the index that User selected from the listbox
def main_Index_User():
    if len(main_box_Store_USER.curselection())==0:
        #To show an error, when the user click the buttons without input
        messagebox.showerror("Error", "Please Select the User first")
    else:
        return int(main_box_Store_USER.curselection()[0])

#This function is to add a contact
def User_add_contact():
    if len(Address_Book_Main) <50:#This is to limit the entries to up to 50 persons only
        if U_FirstName.get() and U_LastName.get() and U_Address.get() and U_ContactNumber.get():
            #This is to add what the User input to the object or "StringVar()" 
            Address_Book_Main.append([U_FirstName.get(),U_LastName.get(), U_Address.get(), U_ContactNumber.get()])
            messagebox.showinfo("Successful","The Contact has been Added")
            writeCSV_USER(Address_Book_Main)
            user_Refresh()
        else:
            messagebox.showerror("Error", "Invalid Entry \nPlease complete all the Entry \nType (N/A) if none")
    else:
        messagebox.showerror("Error", "Maximum Limit has been reached")
    Display_User_Box()

#This function is to edit the contact
def User_edit_contact():
    if U_FirstName.get() and U_LastName.get() and U_Address.get() and U_ContactNumber.get():
        #Selecting the list of information of a certain person, then equating it to the current value of the entries
        Address_Book_Main[main_Index_User()] = [U_FirstName.get(),U_LastName.get(), U_Address.get(), U_ContactNumber.get()]
        messagebox.showinfo("Successful", "The Contact has been Edited")
        writeCSV_USER(Address_Book_Main)
        user_Refresh()
        
    else:
        messagebox.showerror("Error","Please Choose the User you want to edit")	
    Display_User_Box()

#This function is to delete the contact
def User_delete_contact():
    #This line of code will delete a certain person or their entire information to the list
    del Address_Book_Main[main_Index_User()]
    writeCSV_USER(Address_Book_Main)	
    Display_User_Box()
    messagebox.showinfo("Successful","The Contact has been Deleted")
    
#This function is to view the contact
def User_view_contact():
    #This will get the information from the list
    User_First_Name,User_Last_Name,User_Address,User_ContactNumber = Address_Book_Main[main_Index_User()]
    #Then this code will set the information to the entry box
    U_FirstName.set(User_First_Name)
    U_LastName.set(User_Last_Name)
    U_Address.set(User_Address)
    U_ContactNumber.set(User_ContactNumber)

#This function is to refresh all what is stored in the Entry Box
def user_Refresh():
    U_FirstName.set("")
    U_LastName.set("")
    U_Address.set("")
    U_ContactNumber.set("")

#This function is to exit the program
def User_exit_contact():
    Address_Book_GUI.destroy()

#This is the code to store what is in the List Box
def Display_User_Box() :
    Address_Book_Main.sort()
    main_box_Store_USER.delete(0,END)
    for firstname,lastname,address,contactnumber in Address_Book_Main :
        main_box_Store_USER.insert (END,firstname)

#This is the code when you choose in the combobox it stores in the List Box
    def userSort_CHOICE(dropDownChoice):
        main_box_Store_USER.delete(0,END)
        for firstname,lastname,address,contactnumber in Address_Book_Main : 
            
            if searchUser.get()== "First Name":
                #If the User choose the Firstname it will only store all the Firstname in the ListBox
                main_box_Store_USER.insert (END,firstname)
                
            elif searchUser.get()== "Last Name":
                #If the User choose the Lastname it will only store all the Lastname in the ListBox
                main_box_Store_USER.insert (END,lastname)
                
            elif searchUser.get()== "Address":
                #If the User choose the Address it will only store all the Address in the ListBox
                main_box_Store_USER.insert (END,address)
                
            elif searchUser.get()== "Contact":
                #If the User choose the Contact Number it will only store the Contact Number in the ListBox
                main_box_Store_USER.insert (END,contactnumber)
    
    
    #This link of code will filter the listbox according to their categories
    searchUser.bind("<<ComboboxSelected>>",userSort_CHOICE)#This is a built in tkinter

Display_User_Box()

#This is the code for the search bar and search function
def User_search_contact():
    global searchChecker
   
    def userFillSearch(N_search):#This code will get the User choice then it will fill it in the searchbar
        userEntrySearch.delete(0,END)
        userEntrySearch.insert(0,main_box_Store_USER.get(ACTIVE))#Auto fill the search bar

    def searchChecker():#If the user types in the search box this code will find similar entry in the list box
        userInput = userEntrySearch.get()#It will get the information from the search bar
        searchSorter = searchUser.get()#This will sort the category 
        for userSearchChoice in range(len(Address_Book_Main)):
            if searchSorter == sortUser[0]:#If the user choose to find in the Firstname
                #This line of code finds all the possible results for the category Firstname
                if userInput != "" and userInput.lower() in (Address_Book_Main[userSearchChoice][0]).lower():
                    #It will select the index of the element that match what the user is finding
                    main_box_Store_USER.select_set(userSearchChoice)
                else: 
                    #If it doesnt match what the user is finding it will not be chosen and highlighted
                    main_box_Store_USER.selection_clear(userSearchChoice, END)
            elif searchSorter == sortUser[1]:#If the user choose to find in the Lastname
                #This line of code finds all the possible results for the category Lastname
                if userInput != "" and userInput.lower() in (Address_Book_Main[userSearchChoice][1]).lower():
                    main_box_Store_USER.select_set(userSearchChoice)
                else:
                    main_box_Store_USER.selection_clear(userSearchChoice, END)
            elif searchSorter == sortUser[2]:#If the user choose to find in the Address
                #This line of code finds all the possible results for the category Address
                if  userInput != "" and userInput.lower() in (Address_Book_Main[userSearchChoice][2]).lower():
                    main_box_Store_USER.select_set(userSearchChoice)
                else:
                    main_box_Store_USER.selection_clear(userSearchChoice, END)
                    
            elif searchSorter == sortUser[3]:#If the user choose to find in the Contact Number
                #This line of code finds all the possible results for the category Contact Number
                if userInput != "" and userInput.lower() in (Address_Book_Main[userSearchChoice][3]).lower():
                    main_box_Store_USER.select_set(userSearchChoice)
                else:
                    main_box_Store_USER.selection_clear(userSearchChoice, END)
    
    #This code is to show an error if it doesn't find any results that the user is finding

        if searchSorter == sortUser[0] and not len(main_box_Store_USER.curselection()):
             messagebox.showerror("Error", "The User's First Name doesn't Exist")
        elif searchSorter == sortUser[1] and not len(main_box_Store_USER.curselection()):
             messagebox.showerror("Error", "The User's Last Name doesn't Exist")
        elif searchSorter == sortUser[2] and not len(main_box_Store_USER.curselection()):
             messagebox.showerror("Error", "The User's Address doesn't Exist")
        elif searchSorter == sortUser[3] and not len(main_box_Store_USER.curselection()):
             messagebox.showerror("Error", "The User's Contact Number doesn't Exist")

    #If the user select from the listbox, this code will store what the user select to the search box
    main_box_Store_USER.bind("<<ListboxSelect>>", userFillSearch)
    
    
User_search_contact()

#This is what makes the buttons visible and responsinble in calling their respective functions
def Address_bookButtons():
    Button(Address_Book_GUI,text= "Add", font='Calibri 14 bold',bg='turquoise4',foreground="white", command = User_add_contact).place(x= 65, y=220)
    Button(Address_Book_GUI,text= "Edit", font='Calibri 14 bold',bg='turquoise4',foreground="white" ,command = User_edit_contact).place(x= 115, y=220)
    Button(Address_Book_GUI,text= "Delete", font='Calibri 14 bold',bg='turquoise4',foreground="white" ,command = User_delete_contact).place(x= 165, y=220)
    Button(Address_Book_GUI,text= "View", font='Calibri 14 bold',bg='turquoise4',foreground="white", command = User_view_contact).place(x= 240, y=220)
    Button(Address_Book_GUI,text="Search", font='Calibri 14 bold',bg='turquoise4',foreground="white", command = searchChecker).place(x= 300, y=220)
    Button(Address_Book_GUI,text= "Refresh", font='Calibri 14 bold',bg='turquoise4',foreground="white", command = user_Refresh).place(x= 240, y=270)
    Button(Address_Book_GUI,text= "Exit", font='Calibri 14 bold',bg='red',foreground="white", command = User_exit_contact).place(x= 323, y=270)
    
Address_bookButtons()
readCSV_USER()#To display what is inserted from the CSV to the GUI 
Address_Book_GUI.mainloop()#Continous display of the output window and run the Tkinter
