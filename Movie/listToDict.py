# convert movieData list to dictionary

from asyncore import read
import json

filename="all_Movies.json"
movieJsonFile = ""


def readMovieRecord():
    data = ""
  
    try:
        with open (filename) as f: #opening file
            data = json.load(f)#loading the file in python object
    except IOError:
            print("Error")
    return data


def convertToDict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
        
# testing
movieListDist = readMovieRecord()
print(convertToDict(movieListDist))