# Python 3
# coding: utf-8

__author__ = "Ammar S Malik"
__copyright__ = "Copyright 2022, The Movie Rental Project"
__credits__ = ["Ammar Malik", ""]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

from logging import exception
import json

class Customer() :
    def __init__(self, customerFile):
        self.FileName = customerFile
        self.customerFileData = []
        self.idxFile = []
        self.idxDict = {
            "customerName":"",
            "RecNo":"",
            "customerID":""
        }

    # Update indexes on customers json. Filename will be supplied 
    def updateIndex(self):
        try:
            # read file into variable which was initialized in this class
            with open(self.FileName) as customerFile :
                self.customerFileData = json.load(customerFile)
            
            # now iterate through the data table, and update the index file
            recCounter = 0
            for cust in self.customerFileData:
                self.idxDict["customerName"] = cust["customerName"]
                self.idxDict['RecNo'] = str(recCounter)
                self.idxDict["customerID"] = cust["customerID"]
                self.idxFile.append(self.idxDict.copy())
                recCounter+=1

            # Seriallize the list to be written to the json index file
            ser_idxFile=json.dumps(self.idxFile, indent=1)

            # We have filled our new list with all indexes. Now write it back to the index file
            with open("idxCustomer.json", "w+") as idxCust:
                idxCust.write(ser_idxFile)

        except IOError:
            print("There was an issue accessing {}", IOError)

    # Search a name in the index file
    def search(self, customerName):
        from os.path import exists
        recNumber = "0"
        customerID = "0"
        try:
            if exists("idxCustomer.json"):
                with open("idxCustomer.json", "r") as customerFile :
                    self.customerFileData = json.load(customerFile)
                
                print("Searching for ... ", customerName)
                # now iterate through the data table, and update the index file
                recCounter = 0
                for custSearch in self.customerFileData:
                    if custSearch["customerName"].upper() == customerName.upper():
                        recNumber = custSearch["RecNo"]
                        customerID = custSearch["customerID"]

                print("Result looks like {}", recNumber)
            else:
                print("Index file not found to search for the customer")
        except IOError as e:
            print(e)
        return recNumber,customerID