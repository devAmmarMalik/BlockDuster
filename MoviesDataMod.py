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
from hashlib import new
import os, BlockDusterColors
import json, jsonFileHandler


# reading from json file and populating data object
movieData = jsonFileHandler.readJsonFile('movies.json')

# initializing var to calculate last movie id
lastMovieID = len(movieData)

     
def write_json(new_data, fileName = 'movies.json'):

    try:
        with open (fileName, 'r+') as file:
                with open(filename, "w") as json_file:
        data.append(newdata)  # appending data list read from json file with new record
        print(json.dump(data, json_file, indent=1))
            except IOError:
        print("Error reading JSON file")

    return

def addMovieRecord():
        movieID = (lastMovieID+1)
        print("Last MovieID: ", str(lastMovieID) )
        movieTitle = input('New Movie Name?: ')
        movieGenre = input('New Movie Genre?: ')

        newMovie = {    "MovieID": movieID,
                        "MovieName": movieTitle, 
                        "MovieGenre": movieGenre 
                    }
        print (newMovie)
    
        write_json(newMovie)
    return


addMovieRecord()