import json 

# from tkinter.messagebox import YES, YESNOCANCEL
 
# #Opening a json file and printing customer information
# filename=r"C:\Users\rupma\Documents\BlockDuster\Movie\all_Movies.json"
filename="all_Movies.json"
movieJsonFile = ""


def readMovieRecord():
    data = ""
  
    try:
        with open (filename) as f: #opening file
            data = json.load(f)#loading the file in python object
    except IOError:
            print("Error")
    return data
     

# def write_json(new_data, fileName):

#     try:
#         with open (fileName) as f: #opening file
#             file_data = json.load(f)#loading the file in python object
#             file_data.append(","+new_data)           
#             json.dump([],file_data)
#     except IOError:
#             print("Error")

def writeJsonFile(newdata, filename) :
    # load data from json file   
    #data = readMovieRecord()
    #Data = readMovieRecord()
    # open json file in write mode        
    with open(filename, "w") as json_file:
        movieJsonFile.append(newdata)  # appending data list read from json file with new record
        print(json.dump(movieJsonFile, json_file, indent=1))  # writing data list of all records back to json file
    return True


movieJsonFile = readMovieRecord()
for myRec in (movieJsonFile):
    print("Movie ID:", myRec["Movie_ID"])
    print("Movie Title:",myRec["Movie Title"])

lenOfAllRecs = len(movieJsonFile)
#print(movieJsonFile[5-1]["Movie_ID"])
for i in lenOfAllRecs
    print(["Movie_ID"])


nextRecord = int(movieJsonFile[lenOfAllRecs-1]["Movie_ID"]) + 1
print(nextRecord)
#writeJmovieJsonFilesonFile(_Dict, filename)



# ans =input('Add Record to Movie List?' '(yes/no) ')
# if ans == "yes":
   
#     movieTitle = input('New Movie name?')
#     movieActors = input('Actor name?')


#     newMovie = {   
#                     "Movie_ID": "",
#                     "Movie Title": movieTitle, 
#                     "Movie Actors":movieActors 
#                 }

# write_json(newMovie,filename)

# from fileinput import filename
# import json
# from operator import ne

# #function to read from json file
# filename = 'all_Movies'
# def readJsonFile(filename) :
#     try:
#         with open(filename) as json_file :
#             data = json.load(json_file)
#             for i in data['movie']:
#                 print(i)

#     except IOError:
#         print("Error reading JSON file")
#     return data


# # function to add new data record  to jason file
# def editJsonFile(editCust, newdata, filename) :
#     # load data from json file
#     data = readJsonFile(filename)

#     # gets the number of records
#     lendata = len(data)
    
#     #parsing the records in data 

#     for i in range(0,lendata):
#         #  assigning new values to data if given for customerName, address, city, state
#         if data[i]['customerName'] == editCust :
#             if newdata['customerAddress'] != "":
#                  data[i]['customerAddress'] = newdata['customerAddress']
                 
#             elif newdata['customerCity'] != "" :
#                  data[i]['customerCity'] = newdata['customerCity']
                 
#             elif newdata['customerState'] != "" :
#                 data[i]['customerState'] = newdata['customerState']
                
#             elif newdata['customerPhone'] != "" :
#                 data[i]['customerPhone'] = newdata['customerPhone'] 
                
#             # opening json file and writing edited data back  
#             with open(filename, "w") as json_file :
#                 print(json.dump(data, json_file, indent=1))       
#                 return 0
            
#     else :
#         return 1

    



# def writeJsonFile(newdata, filename) :
#     # load data from json file   
#     data = readMovieRecord()
#     Data = readMovieRecord()
#     # open json file in write mode        
#     with open(filename, "w") as json_file:
#         data.append(newdata)  # appending data list read from json file with new record
#         print(json.dump(data, json_file, indent=1))  # writing data list of all records back to json file
#     return True




# # function to delete a customer from the json file 

# def delJsonFile(delCust, filename):
#     #load data from json file
#     data = readJsonFile(filename)
 
#     # calculating length of data dictionary to get the number of records
#     lendata = len(data)
    
#     for i in range(0, lendata) :
#         if data[i]['customerName'] == delCust :  # checking if the customer name matches the name to be deleted
#             data.pop(i)
#             with open(filename, "w") as json_file :  #open json file in write mode
#                 print(json.dump(data, json_file, indent=1))
#             break
#     else :
#         return False
#     return True
# import json
# import jsonFileHandler
# #import writeJsonHandler

# # reading from json file and populating data object

# data = jsonFileHandler.readJsonFile('customers.json')

# # initializing var to calculate last customer id
# lastCustID = 0

# # extracting and printing fields from data from json file

# for i in data :
#     print(f"Customer ID : {i['customerID']}", end = " -->")
#     print(f" {i['customerName']}", end = ", ")
#     print(f"{i['customerAddress']}, {i['customerCity']}, {i['customerState']}", end = " -->")
#     print(f" {i['customerPhone']}\n")
#     lastCustID = int(i['customerID'])  # storing last customer id in variable

# action = input("Enter a number for the action : add customers - 1 , edit customers - 2, delete customers - 3 : ")

# if action == "1" :
#     #initializing a dictionary to store the new customer data
#     newCust = { "customerID":"", 
#                 "customerName": "", 
#                 "customerAddress": "", 
#                 "customerCity": "", 
#                 "customerState": "",
#                 "customerPhone": ""
#                 }


#     # getting new customer details for adding new customers

#     custName = input("\nEnter new customer name: ")
#     custAddress = input("Enter street address: ")
#     custCity = input("Enter city: ")
#     custState = input("Enter State: ")
#     custPhone = input("Enter phone: ")


#     # populating the new customer dictionary with user inputs

#     newCust['customerID'] = str(lastCustID + 1)
#     newCust['customerName'] = custName
#     newCust['customerAddress'] = custAddress
#     newCust['customerCity'] = custCity
#     newCust['customerState'] = custState
#     newCust['customerPhone'] = custPhone


#     # calling funcion to write the new record in json file
#     if jsonFileHandler.writeJsonFile(newCust, "customers.json") :
#         print("Successfully added new customer!!")

        

# elif action == "2" :
#     #edit customer details

#     editCust = {"customerAddress" : "",
#                 "customerCity" : "",
#                 "customerState" : "",
#                 "customerPhone" : ""
#                 }
    
#     editName = input("\nEnter customer name for updating: ")

#     editCust["customerAddress"] = input("Enter new address (press enter - no changes): ")
#     editCust["customerCity"] = input("Enter City (press enter - no changes): ")
#     editCust["customerState"] = input("Enter State (press enter - no changes): ")
#     editCust["customerPhone"] = input("Enter new phone (press enter - no changes) : ")

#     if not any(editCust.values()):
#         print(f"\nNo changes given for {editName}!!!\n")
#         quit()

#     editStatus = jsonFileHandler.editJsonFile(editName, editCust, "customers.json")

#     if editStatus == 0 :
#         print(f"\nSuccefully updated {editName}'s details!!")
#     elif editStatus == 1 :
#         print(f"\n{editName} not found in datafile!!\n")
    

# elif action == "3" :
#     # delete a customer
#     delCustomer = input("\nEnter customer to be removed: ")

#     if jsonFileHandler.delJsonFile(delCustomer, "customers.json"):
#         print(f"\nSuccessfully deleted {delCustomer} from Custemers datafile!!\n")
#     else :
#         print(f"\n{delCustomer} not found!!\n")





   
