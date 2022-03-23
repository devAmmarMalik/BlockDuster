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
    with open(filename) as json_f:
        data = json.load(json_f)

    # open json file in write mode         
    with open(filename, "w") as json_file:
        data.append(newdata)  # appending data list read from json file with new record
        print(json.dump(data, json_file, indent=1))  # writing data list of all records back to json file
    return True







