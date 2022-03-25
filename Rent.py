# Python 3
# coding: utf-8
__author__ = "Per-Scholas Cohort-5"
__copyright__ = "Copyright 2022, Customer main menu"
__credits__ = ["Ricardo,Tim,Ammar,Zee,Bakal,Anju,Rupa"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

import os, BlockDusterColors, json, datetime, RentalData

from datetime import date

today = date.today()
oneRecord = {
    "VideoID" : "",
    "CustomerID" : "",
    "IssueDate" : "",
    "ReturnDate" : ""
}

filename = os.getcwd() + "/Rental.json"
fileData = []

def getCustomer():
    import CustomerIDX
    recNumber = -1
    customerID = 0
    objCustomer = CustomerIDX.Customer("customers.json")
    cCustomerName = input("     Customer name to rent : ")
    showCustomer, recNumber, customerID = objCustomer.searchCustomer(cCustomerName, "customers.json")
    if len(showCustomer) > 0 :
        print("Customer Name : ", showCustomer["customerName"])
        print("      Address : ", showCustomer["customerAddress"])
        print("         City : ", showCustomer["customerCity"])
        print("        state : ", showCustomer["customerState"])
        print(" Phone Number : ", showCustomer["customerPhone"])
    else:
        print("*** Customer not found ***")

    return (customerID)

def RentalMainMenu() :
    os.system('clear')  # Clear the terminal before starting the program so everything is clear
    print('''        _
                    ( \
         __         _)_\_
        ' \;---.-._S_____2_
          /   / /_/       (______
       __(  _;-'    =    =|____._'.__
      /   _/     _  @\ _(@(      '--.\
      (_ /      /\  _   =( ) ___     \\
        /      /\ \_ '.___'-.___~.    '\
  snd  /      /\ \__'--') '-.__c` \    |
      |     .'  )___'--'/  /`)     \   /
      |    |'-|    _|--'\_(_/       '.'
      |    |   \_  -\
       \   |     \ /`)
        '._/      (_/
    ------------------------ MOVIES RENTAL ------------------------
    ''')

    print(''' 
    ################################################################
    #   Movies Rental - Choose one of the options from below      #
    ----------------------------------------------------------------
    #    1-New Rental | 2-View Rental | 3-Return | 4-Main Menu    #         
    ################################################################
    ''')

    if len(fileData) == 0:
        RentalData.ReadRental(fileData,filename)

    selection = 0
    while selection != "4" :
        selection=input(BlockDusterColors.colorFormat.CBLUE + "     Rental selection.......:" + BlockDusterColors.colorFormat.ENDC)
        if selection == '1' :
            # So fileData has a collection of the entire file. Get the input from the user and save it to the 
            # dictionary variable above
            oneRecord["VideoID"] = 1
            oneRecord["CustomerID"] = getCustomer()
            oneRecord["IssueDate"] = today.strftime('%m/%d/%Y')
            RentalData.AddARental(oneRecord, fileData, filename)
            input("Record saved successfully")
            os.system('clear')
            return 0
        elif selection == '2' :
            print("Edit a customer")
        elif selection == '3' :
            print("Delete a customer")
        elif selection == '4' :
            os.system('clear')
            return 
        else :
            print("invalid option")