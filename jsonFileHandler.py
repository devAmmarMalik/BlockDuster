import json

#function to read from json file

def readJsonFile(filename) :
    try:
        with open(filename) as json_file :
            data = json.load(json_file)
    except IOError:
        print("Error reading JSON file")
    return data


# function to add new data record  to jason file

def writeJsonFile(newdata, filename) :
    # load data from json file   
    data = readJsonFile(filename)
    
    # open json file in write mode         
    with open(filename, "w") as json_file:
        data.append(newdata)  # appending data list read from json file with new record
        print(json.dump(data, json_file, indent=1))  # writing data list of all records back to json file
    return True

# funtion to edit a customers details in json file



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







