import json

#function to read from json file

def readJsonFile(filename) :
    try:
        with open(filename) as json_file :
            data = json.load(json_file)
            return data
    except IOError:
        print("Error reading JSON file")
    


# function to add new data record  to jason file
def editJsonFile(editCust, newdata, filename) :
    # load data from json file
    data = readJsonFile(filename)

    # gets the number of records
    lendata = len(data)
    
    print(newdata)
    #parsing the records in data 

    for i in range(0,lendata):
        #  assigning new values to data if given for customerName, address, city, state
        if data[i]['customerName'] == editCust :
        
            if newdata['customerAddress'] != "":
                 data[i]['customerAddress'] = newdata['customerAddress']
            if newdata['customerCity'] != "" :
                 data[i]['customerCity'] = newdata['customerCity']     
            if newdata['customerState'] != "" :
                data[i]['customerState'] = newdata['customerState']
            if newdata['customerPhone'] != "" :
                data[i]['customerPhone'] = newdata['customerPhone'] 
            if newdata['customerName'] != "":
                data[i]['customerName'] = newdata['customerName']
            
                
            # opening json file and writing edited data back  
            with open(filename, "w") as json_file :
                print(json.dump(data, json_file, indent=1))       
                return 0
            
    else :
        return 1

    
def writeJsonFile(newdata, filename) :
    # load data from json file   
    data = readJsonFile(filename)
    # assigning customer id to new customer by adding 1 to the customer id of last record
    newdata['customerID'] = str(int(data[-1]['customerID']) + 1)

    print(newdata)
    
    # open json file in write mode         
    with open(filename, "w") as json_file:
        data.append(newdata)  # appending data list read from json file with new record
        print(json.dump(data, json_file, indent=1))  # writing data list of all records back to json file
    return True




# function to delete a customer from the json file 

def delJsonFile(delCust, filename):
    #load data from json file
    data = readJsonFile(filename)
 
    # calculating length of data dictionary to get the number of records
    lendata = len(data)
    
    for i in range(0, lendata) :
        if data[i]['customerName'] == delCust :  # checking if the customer name matches the name to be deleted
            data.pop(i)
            with open(filename, "w") as json_file :  #open json file in write mode
                print(json.dump(data, json_file, indent=1))
            break
    else :
        return False
    return True







