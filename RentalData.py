# Python 3
# coding: utf-8
__author__ = "Per-Scholas Cohort-5"
__copyright__ = "Copyright 2022, Customer main menu"
__credits__ = ["Ricardo,Tim,Ammar,Zee,Bakal,Anju,Rupa"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

import json, datetime, CustomerIDX, MoviesIDX
import string
from datetime import date

today = date.today()

# Function: ReadRental()
# Purpose: Read existing rentals into a global variable so it can be accessed later
def ReadRental(filename) :
    # Open data file and read its contents to the list above
    # With will open the file and then it will close it also
    with open(filename, "r") as jsonFile:
        fileData = json.load(jsonFile)
    return fileData
# Function: AddARental()
# Purpose: Add a new movie rental to the list of rentals
def AddARental(oneRecord, fileData, filename):
    fileData = ReadRental(filename)

    # Append this record from the dictionary to a list of all records
    fileData.append(oneRecord.copy())

    # now serialize the output
    NewFiletoWrite = json.dumps(fileData, indent=1)

    # Since we have opened this file earlier, we do not need to open it again. Just write the information back
    with open(filename, "r+") as jsonFile:
        jsonFile.write(NewFiletoWrite)

# Function: MergeRental()
# Purpose: Open Rental data, customer data and movies data. Combine them for all customer ID and Movie ID and 
#          create a list of all outstanding and returned movies
def RentalHistory(customerFileName, moviesFileName, filename):
    RentalHistory = []
    RentalHistoryDict = {
        "Customer" : "",
        "CustomerPhone" : "",
        "Movie" : "",
        "IssueDate" : "",
        "ReturnDate" : ""
    }

    oCustmers = CustomerIDX.Customer(customerFileName)
    oMovies = MoviesIDX.Movies(moviesFileName)

    with open(filename) as rentalHist :
        moviesFileData = json.load(rentalHist)

    for outStanding in moviesFileData:
        ## Get customer information from customers json 
        customerInfo, recNo, custID = oCustmers.searchCustomerByID(outStanding["CustomerID"], "Customers.json")
        if recNo >= 0 :
            RentalHistoryDict["Customer"] = customerInfo["customerName"]
            RentalHistoryDict["CustomerPhone"] = customerInfo["customerPhone"]

        ## Get movie name from the movies informaiton
        movieInfo, movieRecNo, movID = oMovies.searchMovieByID(outStanding["VideoID"],"Movies.json")
        if movieRecNo >= 0:
            RentalHistoryDict["Movie"] = movieInfo["MovieName"]

        ## Now get the issue date and if there, return date
        RentalHistoryDict["IssueDate"] = outStanding["IssueDate"]
        RentalHistoryDict["ReturnDate"] = outStanding["ReturnDate"]

        if recNo >= 0 and movieRecNo >= 0:
            RentalHistory.append(RentalHistoryDict.copy())

    ## Now return the data back
    return RentalHistory

# Function: RentalReturn()
# Purpose: Update rental return date
def RentalReturn(filename, RecNo, ReturnDate):
    allRentals = ReadRental(filename)
    allRentals[RecNo]["ReturnDate"] = ReturnDate
    # now serialize the output
    NewFiletoWrite = json.dumps(allRentals, indent=1)

    # Since we have opened this file earlier, we do not need to open it again. Just write the information back
    with open(filename, "r+") as jsonFile:
        jsonFile.write(NewFiletoWrite)

# Function: ShowAllOutstandingRental()
# Purpose: Shpw all outstanding movies by customer name
def ShowAllOutstandingRental(CustomerID, moviesFileName, filename):
    allRentals = ReadRental(filename)
    selectedMovies = []
    rowCounter = 0

    RentalHistoryDict = {
        "RecNo" : 0,
        "Movie" : "",
        "IssueDate" : "",
        "ReturnDate" : ""
    }

    oMovies = MoviesIDX.Movies(moviesFileName)

    for rows in allRentals:
        if rows["CustomerID"] == CustomerID:
            RentalHistoryDict["RecNo"] = rowCounter
            # This movie is rented by the customer id. Get movie information 
            ## Get movie name from the movies informaiton
            movieInfo, movieRecNo, movID = oMovies.searchMovieByID(rows["VideoID"],"Movies.json")
            RentalHistoryDict["Movie"] = movieInfo["MovieName"]

            ## Now get the issue date and if there, return date
            RentalHistoryDict["IssueDate"] = rows["IssueDate"]
            RentalHistoryDict["ReturnDate"] = rows["ReturnDate"]

            selectedMovies.append(RentalHistoryDict.copy())
        rowCounter+=1

    return selectedMovies