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

class Movies() :
    # Constructor to the class
    def __init__(self, movieFile):
        self.FileName = movieFile
        self.movieFileData = []
        self.idxFile = []
        self.idxDict = {
            "movieName":"",
            "RecNo":"",
            "movieID":""
        }

    # Update indexes on customers json. Filename will be supplied 
    def updateIndex(self):
        try:
            # read file into variable which was initialized in this class
            with open(self.FileName) as movieFile :
                self.movieFileData = json.load(movieFile)
            
            # now iterate through the data table, and update the index file
            recCounter = 0
            for cust in self.movieFileData:
                self.idxDict["movieName"] = cust["movieName"]
                self.idxDict['RecNo'] = str(recCounter)
                self.idxDict["movieID"] = cust["movieID"]
                self.idxFile.append(self.idxDict.copy())
                recCounter+=1

            # Seriallize the list to be written to the json index file
            ser_idxFile=json.dumps(self.idxFile, indent=1)

            # We have filled our new list with all indexes. Now write it back to the index file
            with open("idxMovies.json", "w+") as idxCust:
                idxCust.write(ser_idxFile)

        except IOError:
            print("There was an issue accessing {}", IOError)

    # Search a name in the index file
    def search(self, movieName):
        from os.path import exists
        recNumber = "0"
        movieID = "0"
        try:
            if exists("idxMovies.json"):
                with open("idxMovies.json", "r") as movieFile :
                    self.movieFileData = json.load(movieFile)

                # now iterate through the data table, and update the index file
                recCounter = 0
                for custSearch in self.movieFileData:
                    if custSearch["movieName"].upper() == movieName.upper():
                        recNumber = custSearch["RecNo"]
                        movieID = custSearch["customerID"]
            else:
                print("Index file not found to search for the customer")
        except IOError as e:
            print(e)
        return recNumber,movieID

    # Search a name in the index file then send back one row for the customer found
    def searchCustomer(self, movieName, movieJSONFile):
        from os.path import exists
        recNumber = -1
        movieID = "0"
        movieInfo = []
        try:
            if exists("idxMovies.json") and exists(movieJSONFile) :
                with open("idxMovies.json", "r") as movieFile :
                    self.movieFileData = json.load(movieFile)
                
                # now iterate through the data table, and update the index file
                recCounter = 0
                for custSearch in self.movieFileData:
                    if custSearch["movieName"].upper() == movieName.upper():
                        recNumber = int(custSearch["RecNo"])
                        movieID = custSearch["movieID"]

                # Now search for the record number in the Customer file and return it
                with open(movieJSONFile, "r") as movieFile :
                    movieJSON = json.load(movieFile)
                
                if recNumber >= 0 :
                    movieInfo = movieJSON[recNumber].copy()
            else:
                print("Index file or customer file not found to search for the customer")
        except IOError as e:
            print(e)
        return movieInfo, recNumber, movieID 