# Python 3
# coding: utf-8

__author__ = "Ammar S "
__copyright__ = "Copyright 2022, The Movie Rental Project"
__credits__ = ["Ammar Malik", "", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

# Simple main menu to handle our Movie Rental store
# It will show a static menu and will ask for an option
# Then it will clear the screen and proceed accordingly
import os, BlockDusterColors, CustomerMainMenu, MoviesMainMenu, Rent, Library, CustomerIDX, MoviesIDX
from Rent import RentalMainMenu

def MainMenu() :
    Library.clearTerminal() #os.system('clear')  # Clear the terminal before starting the program so everything is clear

    print(BlockDusterColors.colorFormat.CGREEN + ''' 
    ######################################################################
    #                            ,          ,                            #
    #    "Hi, BlockDuster       _|\_       /|                            #
    #      here, Rent Movies   /___ "\----' |                            #
    #           We Care"      /=====\ \     `-.                          #
    #                  \    // .--.  \|  |      \                        #
    #                      /(  [@@]   )  /       \                       #
    #          ,          |  \ '--'  /  /         \-------               #
    #          |\_        |   \___.-'              \----- \              #
    #     __,--'' \.     /|   _____..----) )       |     \ \             #
    #    "----____: \.  / | ('          /      |   |      \ \            #
    #              `. \/ /\  \._     _./      /    |       \ \           #
    #                \_./  \    '====        /    /         \ \          #
    #                       \     ---     --'    /           \ `.        #
    #                        \.              _,-;           /,--.\       #
    #                          \___________/\/ /            "    "       #
    #                                      \/ /_                         #
    #                                      /`/  |                        #
    #     _____ _                +"""".   / /|  /                        #
    #    |_   _| |__   ___        \    \./ / | /                         #
    #      | | | '_ \ / _ \        `\ . | /  +"                          #
    #      | | | | | |  __/          \  |/                               #
    #      |_| |_| |_|\___|           (_)                                #
    #     __  __                 _                    ___                #
    #    |  \/  | ___  _ __  ___| |_ ___ _ __ ___    |_ _|_ __   ___     # 
    #    | |\/| |/ _ \| '_ \/ __| __/ _ \ '__/ __|    | || '_ \ / __|    #
    #    | |  | | (_) | | | \__ \ ||  __/ |  \__ \_   | || | | | (__     # 
    #    |_|  |_|\___/|_| |_|___/\__\___|_|  |___( ) |___|_| |_|\___(    # 
    #                                            |/                      # 
    #                                                                    #
    #                  YOUR FRIENDLY MOVIE RENTAL PLACE                  #
    ######################################################################
    ''' + BlockDusterColors.colorFormat.ENDC)

    print(''' 
    ######################################################################
    #          MAIN MENU - Choose one of the options from below          #
    ----------------------------------------------------------------------
    #  1-Customers | 2-Movies | 3-Rent A Movie | 4-Update DB | 5-EXIT    #   
    ######################################################################
    ''')

MainMenu()
selection = 0
while selection != "5" :
    selection=input(BlockDusterColors.colorFormat.CBLUE + "     [Main Menu] Make your selection.......: " + BlockDusterColors.colorFormat.ENDC)
    if selection == '1' :
        showCustomerMenu = 0
        while showCustomerMenu == 0 :
            showCustomerMenu = CustomerMainMenu.MainMenu()
        MainMenu()

    elif selection == '2' :
        showMovieMenu = 0
        while showMovieMenu == 0 :
            showMovieMenu = MoviesMainMenu.MainMenu.MainMenu()
        MainMenu()

    elif selection == '3' :
        showRentalMenu = 0
        while showRentalMenu == 0 :
            showRentalMenu = RentalMainMenu()
        MainMenu()

    elif selection == '4' :
        # Update all index files on Customer and on Movies
        print("     Processing indexex on customer information")
        oCustomer = CustomerIDX.Customer("customers.json")
        oCustomer.updateIndex()

        print("     Processing indexes on movies information")
        oMovie = MoviesIDX.Movies("Movies.json")
        oMovie.updateIndex()
        MainMenu()

    elif selection == '5' :
        Library.clearTerminal() #os.system('clear')  # Clear the terminal before starting the program so everything is clear
    else :
        print("invalid option")
