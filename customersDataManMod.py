import json
import jsonFileHandler


# reading from json file and populating data object
def displayCustomers() :
    data = jsonFileHandler.readJsonFile('customers.json')

    # initializing var to calculate last customer id
    #lastCustID = 0

    # extracting and printing fields from data from json file

    for i in data :
        print(f"Customer ID : {i['customerID']}", end = " -->")
        print(f" {i['customerName']}", end = ", ")
        print(f"{i['customerAddress']}, {i['customerCity']}, {i['customerState']}", end = " -->")
        print(f" {i['customerPhone']}\n")
     #   lastCustID = int(i['customerID'])  # storing last customer id in variable

    
def searchCustomers() :

    displayCustomers()
    custDetails = { 
                    'customerID' : "",
                    'customerName' : "",
                    'customerAddress' : "",
                    'customerCity' : "",
                    'customerState' : "",
                    'customerPhone' : ""
                    }
    
    st = 1

    searchCust = input("Enter search customer name: ")
    st, custDetails = jsonFileHandler.searchJsonFile(searchCust, "customers.json")
    
    if st >= 0:
        print("\nCUSTOMER found :)")
        print(f"Customer ID : {custDetails['customerID']}", end = " -->")
        print(f" {custDetails['customerName']}", end = ", ")
        print(f"{custDetails['customerAddress']}, {custDetails['customerCity']}, {custDetails['customerState']}", end = " -->")
        print(f" {custDetails['customerPhone']}\n")
    else :
        print(f"\n{searchCust} not found!!")



def addCustomers() :
    
    #initializing a dictionary to store the new customer data
    newCust = { "customerID":"", 
                "customerName": "", 
                "customerAddress": "", 
                "customerCity": "", 
                "customerState": "",
                "customerPhone": ""
                }


    # getting new customer details for adding new customers
    # populating the new customer dictionary with user inputs

    newCust['customerName'] = input("\nEnter new customer name: ")
    newCust['customerAddress'] = input("Enter street address: ")
    newCust['customerCity'] = input("Enter city: ")
    newCust['customerState'] = input("Enter State: ")
    newCust['customerPhone'] = input("Enter phone: ")

    #print(newCust)

    # calling funcion to write the new record in json file
    if jsonFileHandler.addJsonFile(newCust, "customers.json") :
        print("Successfully added new customer!!")
    
    #print(newCust['customerID'])

        
def editCustomers() :
    #edit customer details
    editCust = {"customerName" : "",
                "customerAddress" : "",
                "customerCity" : "",
                "customerState" : "",
                "customerPhone" : ""
                }
    
    editName = input("\nEnter customer name for updating: ")

    if editName == "" :
        print("Warning : Customer name not given for editing!!")
        return


    editCust["customerName"] = input("Enter name change (press enter - no changes): ")
    editCust["customerAddress"] = input("Enter address change (press enter - no changes): ")
    editCust["customerCity"] = input("Enter City (press enter - no changes): ")
    editCust["customerState"] = input("Enter State (press enter - no changes): ")
    editCust["customerPhone"] = input("Enter new phone (press enter - no changes) : ")

    # print(f"cust change : {editCust}")

    if not any(editCust.values()):
        print(f"\nNo changes given for {editName}!!!\n")
        return


    editStatus = jsonFileHandler.editJsonFile(editName, editCust, "customers.json")

    if editStatus == 0 :
        print(f"\nSuccefully updated {editName}'s details!!")
    elif editStatus == 1 :
        print(f"\n{editName} not found in datafile!!\n")
    

def delCustomers() :
    # delete a customer
    delCustomer = input("\nEnter customer to be removed: ")

    if jsonFileHandler.delJsonFile(delCustomer, "customers.json"):
        print(f"\nSuccessfully deleted {delCustomer} from Customers details!!\n")
    else :
        print(f"\n{delCustomer} not found!!\n")
