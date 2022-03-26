import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName, "r") as jsonObjFile:
            data = json.load(jsonObjFile)
    except IOError:
        print("Could not read file")
    return data



origList = readJsonFile("customers.json")
#print(origList)

# Add new Record to a List. 
# Takes the json file and new record in dictionary format as args
# Append the new record and writes back to the file
def addNewRecord(fileName,recordDetail):
    origList = readJsonFile(fileName)
    
    try:
        origList.append(recordDetail)
        print ("list appended")
    except IOError:
        print("Could not add the record")
    try:
        with open(fileName, "w") as jfileHandle:
            json.dump(origList,jfileHandle,indent=1)
    except IOError:
        print("Could not append  file")
        
    #print(newList)
    return 

# Delete Record from the list
# Takes the jsonfile, matching field name and value
# Deletes the record and writes back to the file

def deleteRecord(fileName,fieldName,fieldValue):
    origList = readJsonFile(fileName)
    keyIndex = 0
    foundRec = False
    for item in origList:
        
        if (item[fieldName] == fieldValue ):
            foundRec = True
            print(keyIndex)
            try:
                delrec = origList.pop(keyIndex)
                print ("Record deleted")
                break
            except IOError:
                print("Delete Failed- Record not found")
        
        keyIndex = keyIndex +1
    try:
        with open(fileName, "w") as jfileHandle:
            json.dump(origList,jfileHandle,indent=1)
    except IOError:
        print("Could not delete the record")
    if (foundRec == False) :
        print("No matching record found")    
    #print(newList)
    return

def updateRecord(fileName,fieldName,oldFieldValue,newFieldValue):
    origList = readJsonFile(fileName)
    keyIndex = 0
    foundRec = False
    for item in origList:
        if (item[fieldName] == oldFieldValue ):
            foundRec = True
            print(keyIndex)
            try:
               item[fieldName] = newFieldValue
               print ("Record updated")
               break
            except IOError:
                print("Update Failed- Record not found")
        keyIndex = keyIndex +1
    try:
        with open(fileName, "w") as jfileHandle:
            json.dump(origList,jfileHandle,indent=1)
            print("File Updated")
    except IOError:
        print("Could not update the record")
    if (foundRec == False) :
        print("No matching record found") 

##Below This- Calling the functions  
 
record = {
   "customerID": "50",
   "customerName": "Jim Bell",
   "customerAddress": "11 rose st",
   "customerCity": "NYC",
   "customerState": "NY",
   "customerPhone": "9001231234"
  }
#addNewRecord("customers.json",record)
#
# updateRecord("customers.json","customerName","Jim Bell","Jimmy") 
deleteRecord("customers.json","customerName","Akshaya Ramakrishna") 
