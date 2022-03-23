import json

def writeJsonFile(newdata, filename) :
       
    with open(filename) as json_f:
        data = json.load(json_f)
            
    with open(filename, "w") as json_file:
        data.append(newdata)
        print(json.dump(data, json_file, indent=1))
    return True


   
