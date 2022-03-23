import json 
#Opening a json file and printing customer information
with open ('movie_rentalfile.json') as f: #opening file
    data =json.load(f)
    for movie in data['movies']: # using movie key of the python object 
        print(movie)
       
