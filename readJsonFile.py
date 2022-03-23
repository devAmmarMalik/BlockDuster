import json

def readJsonFile(filename) :
    try:
        with open(filename) as json_file :
            data = json.load(json_file)
    except IOError:
        print("Error reading JSON file")
    return data
    






