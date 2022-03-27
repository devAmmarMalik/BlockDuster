
import json
from tkinter.messagebox import YES, YESNOCANCEL
 
#Opening a json file and printing customer information

def readMovieRecord():
    data = ""
    try:
        with open ('movie_rentalfile.json' , 'r') as f: #opening file
            data = json.load(f)#loading the file in python object
                            
    except IOError:
            print("Error")
    return data
     

def write_json(new_data, fileName = 'data.json'):

    try:
        with open (fileName, 'r+') as file: #opening file
            file_data = json.load(file)#loading the file in python object
            file_data["new_Movie"].append(new_data)
            file.seek(0)
            json.dump(file_data,file, indent=4)
    except IOError:
            print("Error")


    ans = input('Add Record to Movie List?' '(yes/no) ')
    if ans == "yes":
        movieID = input('New Movie name?')
        movieTitle = input('New Movie name?')
        movieActors = input('New Movie name?')


        newMovie = {    "Movie ID": "movieID",
                        "Movie Title": "movieTitle", 
                        "Movie Actors":"movieActors" 
                    }
    elif ans != "no":
            print("Please try again")
    write_json(newMovie)
   
