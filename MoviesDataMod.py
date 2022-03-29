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
from fileinput import filename
from hashlib import new
import os, BlockDusterColors
import json, jsonFileHandler


# reading from json file and populating data object
movieData = jsonFileHandler.readJsonFile('movies.json')

# initializing var to calculate last movie id
lastMovieID = len(movieData)

     
def write_json(newMovie, fileName = 'movies.json'):

    try:
        with open (fileName, 'w') as file:
            movieData.append(newMovie)
            print(json.dump(movieData, file, indent=1))
    except IOError:
            print("Error reading JSON file")
    return
    

def addMovieRecord():

        # set new movie record ID by incrementing lastMovieID by 1
        # and convert to a string for dictionary compatibility
        movieID = str(lastMovieID+1)
        print("New MovieID: ", movieID )
        movieTitle = input('New Movie Name?: ')
        movieGenre = input('New Movie Genre?: ')

        newMovie = {    "MovieID": movieID,
                        "MovieName": movieTitle, 
                        "MovieGenre": movieGenre 
                    }
        print (newMovie)
    
        write_json(newMovie)

def delMovieRecord():
        # get movieID to be deleted 
        #   > search for movieID from movieList 
        #   > if/else based on search results 
        #   > confirm movieID deletion
        #   > execute movieID entry from json file 
        #   > repeat until exit to Main menu

        # get movieID 
        findMovieID = input('Find Movie ID?: ')
        print(findMovieID)

        # find movieID
        while i != findMovieID:
            if i == movieData[i]:
                print(movieData['MovieName'])
            elif i < findMovieID:
                i = i + 1
            else:
                print("Did not find movie in inventory.")    
        #
        # write_json(newMovie)


addMovieRecord()