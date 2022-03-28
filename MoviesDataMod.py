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
data = jsonFileHandler.readJsonFile('movies.json')
fileName = 'movies.json'

# initializing var to calculate last movie id
lastMovieID = len(data)
     
def write_json(newMovie,fileName):

    try:
        with open(fileName, "w") as json_file:
            data.append(newMovie)
            print(json.dump(data, json_file, indent=1))


def addMovieRecord():
    newmovieID = (lastMovieID+1)
    # print("Last MovieID: ", str(lastMovieID) )
    movieTitle = input('New Movie Name?: ')
    movieGenre = input('New Movie Genre?: ')

    newMovie = {    "MovieID": newmovieID,
                    "MovieName": movieTitle, 
                    "MovieGenre": movieGenre 
                }

    write_json(newMovie)


