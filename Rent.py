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

import os, BlockDusterColors, json, datetime, RentalData, Library, CustomerIDX, MoviesIDX

from datetime import date

today = date.today().strftime('%m/%d/%Y')

oneRecord = {
    "VideoID" : "",
    "CustomerID" : "",
    "IssueDate" : "",
    "ReturnDate" : ""
}

filename = os.getcwd() + "/Rental.json"
fileData = [2]

def getCustomer():
    import CustomerIDX
    recNumber = -1
    customerID = 0
    objCustomer = CustomerIDX.Customer("customers.json")
    cCustomerName = input("     Customer name to rent : ")
    showCustomer, recNumber, customerID = objCustomer.searchCustomer(cCustomerName, "customers.json")
    if len(showCustomer) > 0 :
        print(BlockDusterColors.colorFormat.CGREY +
              " Customer Name : ", showCustomer["customerName"])
        print("       Address : ", showCustomer["customerAddress"])
        print("          City : ", showCustomer["customerCity"])
        print("         state : ", showCustomer["customerState"])
        print("  Phone Number : ", showCustomer["customerPhone"] + 
        BlockDusterColors.colorFormat.ENDC)
    else:
        print(BlockDusterColors.colorFormat.CBLINK + " *** Customer not found ***" + BlockDusterColors.colorFormat.ENDC)

    return (customerID)

def getMovie():
    recNumber = -1
    movieID = -1
    objMovies = MoviesIDX.Movies("movies.json")
    cMovieName = input("     Movie name to rent : ")
    showMovie, recNumber, movieID = objMovies.searchMovie(cMovieName, "Movies.json")
    if len(showMovie) > 0 :
        print(BlockDusterColors.colorFormat.CGREY +" Movie Name : ", showMovie["MovieName"])
        print("      Genre : ", showMovie["MovieGenre"] + BlockDusterColors.colorFormat.ENDC)
    else:
       print(BlockDusterColors.colorFormat.CBLINK + " *** Movie not found ***" + BlockDusterColors.colorFormat.ENDC)

    return (movieID)

def RentalMainMenu() :
    Library.clearTerminal()  # Clear the terminal before starting the program so everything is clear
    print(BlockDusterColors.colorFormat.HEADER2)
    print('''        _
                    ( \\
         __         _)_\_
        ' \;---.-._S_____2_
          /   / /_/       (______
       __(  _;-'    =    =|____._'.__
      /   _/     _  @\ _(@(      '--.\\
      (_ /      /\  _   =( ) ___     \\
        /      /\ \_ '.___'-.___~.    '\\
  snd  /      /\ \__'--') '-.__c` \    |
      |     .'  )___'--'/  /`)     \   /
      |    |'-|    _|--'\_(_/       '.'
      |    |   \_  -\\
       \   |     \ /`)
        '._/      (_/

    ''')

    print(''' 
    ################################################################
    #     Movies Rental - Choose one of the options from below     #
    ----------------------------------------------------------------
    #    1-New Rental | 2-View Rental | 3-Return | 4-Main Menu     #         
    ################################################################
    ''')

    print(BlockDusterColors.colorFormat.ENDC)                

    selection = 0
    while selection != "4" :
        selection=input(BlockDusterColors.colorFormat.CBLUE + "     [Movies Rental Menu] Rental selection.......: " + BlockDusterColors.colorFormat.ENDC)
        if selection == '1' :
            # So fileData has a collection of the entire file. Get the input from the user and save it to the 
            # dictionary variable above
            oneRecord["VideoID"] = getMovie()
            if int(oneRecord["VideoID"]) > 0:
                oneRecord["CustomerID"] = getCustomer()
                if int(oneRecord["CustomerID"]) > -1:
                    oneRecord["IssueDate"] = today
                    RentalData.AddARental(oneRecord, fileData, filename)
                    input("Record saved successfully")
                else:
                    input("Press any key to continue...")
            else:
                input("Press any key to continue...")

            Library.clearTerminal()
            return 0
        elif selection == '2' :
            # Show all outstanding movie rentals with Customer name, Movie name, Issue date
            print(BlockDusterColors.colorFormat.CRED)
            print("     *** Rental History to date. Outstanding and Returned")
            print("     Customer             Phone                Movie                Issue                Return")
            print("     Name                 Number               Rented                Date                 Date")
            print('     ------------------------------------------------------------------------------------------')
            for hist in RentalData.RentalHistory("customers.json", "Movies.json", filename) :
                # Now show the history on the screen 
                print("     " + 
                      hist["Customer"].ljust(21) +  
                      hist["CustomerPhone"].ljust(21) +
                      hist["Movie"].ljust(21) + 
                      hist["IssueDate"].ljust(21) + 
                      hist["ReturnDate"]
                      )
            print()
            input("     Press any key to continue..." + BlockDusterColors.colorFormat.ENDC)
            return 0 

        elif selection == '3' :
            objCustomer = CustomerIDX.Customer("customers.json")
            cCustomerName = input("     Customer name to rent : ")
            showCustomer, recNumber, customerID = objCustomer.searchCustomer(cCustomerName, "customers.json")

            if int(showCustomer["customerID"]) > -1:
                print(BlockDusterColors.colorFormat.CGREY)
                print("")
                print("     Customer Name : ", showCustomer["customerName"])
                print("           Address : ", showCustomer["customerAddress"])
                print("              City : ", showCustomer["customerCity"])
                print("             state : ", showCustomer["customerState"])
                print("      Phone Number : ", showCustomer["customerPhone"])
                print("     ------------------------------------------------------")
                
                print("     *** Rental History to date. Outstanding and Returned")
                print("     Movie                Issue                Return")
                print("     Rented                Date                 Date")
                print('     -----------------------------------------------------')                
                
                allRentedMovies = RentalData.ShowAllOutstandingRental(customerID, "Movies.json", filename)
                for hist in allRentedMovies:
                    print("     " + 
                        hist["Movie"].ljust(21) + 
                        hist["IssueDate"].ljust(21) + 
                        hist["ReturnDate"]
                        )

                print(BlockDusterColors.colorFormat.ENDC)                
                print()

                returnWhichMovie = input("     Return which movie: ")

                # Now find out what movie is being returned. We have a list all related movies in the list above
                for hist in allRentedMovies:
                    if hist["Movie"].upper() == returnWhichMovie.upper():
                        rentalRecNo = hist["RecNo"]
                        break

                RentalData.RentalReturn(filename, rentalRecNo, today)
                input("     Movie returned successfully")
            else:
                input("Press any key to continue...")
            return 0
        elif selection == '4' :
            os.system('clear')
            return 
        else :
            print("invalid option")