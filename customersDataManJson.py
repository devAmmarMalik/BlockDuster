import json
import jsonFileHandler
#import writeJsonHandler

# reading from json file and populating data object

data = jsonFileHandler.readJsonFile('customers.json')

# initializing var to calculate last customer id
lastCustID = 0

# extracting and printing fields from data from json file

for i in data :
    print(f"Customer ID : {i['customerID']}", end = " -->")
    print(f" {i['customerName']}", end = ", ")
    print(f"{i['customerAddress']}, {i['customerCity']}, {i['customerState']}", end = " -->")
    print(f" {i['customerPhone']}\n")
    lastCustID = int(i['customerID'])  # storing last customer id in variable

action = input("Enter a number for the action : add customers - 1 , edit customers - 2, delete customers - 3 : ")

if action == "1" :
    #initializing a dictionary to store the new customer data
    newCust = { "customerID":"", 
                "customerName": "", 
                "customerAddress": "", 
                "customerCity": "", 
                "customerState": "",
                "customerPhone": ""
                }


    # getting new customer details for adding new customers

    custName = input("\nEnter new customer name: ")
    custAddress = input("Enter street address: ")
    custCity = input("Enter city: ")
    custState = input("Enter State: ")
    custPhone = input("Enter phone: ")


    # populating the new customer dictionary with user inputs

    newCust['customerID'] = str(lastCustID + 1)
    newCust['customerName'] = custName
    newCust['customerAddress'] = custAddress
    newCust['customerCity'] = custCity
    newCust['customerState'] = custState
    newCust['customerPhone'] = custPhone


    # calling funcion to write the new record in json file
    if jsonFileHandler.writeJsonFile(newCust, "customers.json") :
        print("Successfully added new customer!!")

        

elif action == "2" :
    #edit customer details

    editCust = {"customerAddress" : "",
                "customerCity" : "",
                "customerState" : "",
                "customerPhone" : ""
                }
    
    editName = input("\nEnter customer name for updating: ")

    editCust["customerAddress"] = input("Enter new address (press enter - no changes): ")
    editCust["customerCity"] = input("Enter City (press enter - no changes): ")
    editCust["customerState"] = input("Enter State (press enter - no changes): ")
    editCust["customerPhone"] = input("Enter new phone (press enter - no changes) : ")

    if not any(editCust.values()):
        print(f"\nNo changes given for {editName}!!!\n")
        quit()

    editStatus = jsonFileHandler.editJsonFile(editName, editCust, "customers.json")

    if editStatus == 0 :
        print(f"\nSuccefully updated {editName}'s details!!")
    elif editStatus == 1 :
        print(f"\n{editName} not found in datafile!!\n")
    

elif action == "3" :
    # delete a customer
    delCustomer = input("\nEnter customer to be removed: ")

    if jsonFileHandler.delJsonFile(delCustomer, "customers.json"):
        print(f"\nSuccessfully deleted {delCustomer} from Customers datafile!!\n")
    else :
        print(f"\n{delCustomer} not found!!\n")
