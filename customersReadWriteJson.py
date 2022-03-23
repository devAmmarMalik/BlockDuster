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


#initializing a dictionary to store the new customer data
newCust = { "customerID":"", 
            "customerName": "", 
            "customerAddress": "", 
            "customerCity": "", 
            "customerState": "",
            "customerPhone": ""
            }


# getting new customer details for adding new customers

custName = input("Enter new customer name: ")
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
