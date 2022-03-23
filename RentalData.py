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

import json, datetime
import string
from datetime import date

today = date.today()

# Function: ReadRental()
# Purpose: Read existing rentals into a global variable so it can be accessed later
def ReadRental(fileData, filename) :
    # Open data file and read its contents to the list above
    # With will open the file and then it will close it also
    with open(filename, "r+") as jsonFile:
        fileData = json.load(jsonFile)

# Function: AddARental()
# Purpose: Add a new movie rental to the list of rentals
def AddARental(oneRecord, fileData, filename):
    # Append this record from the dictionary to a list of all records
    fileData.append(oneRecord)

    # now serialize the output
    NewFiletoWrite = json.dumps(fileData, indent=1)

    # Since we have opened this file earlier, we do not need to open it again. Just write the information back
    with open(filename, "r+") as jsonFile:
        jsonFile.write(NewFiletoWrite)
