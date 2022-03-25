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
import os, BlockDusterColors, CustomerMainMenu, MoviesMainMenu, Rent
from Rent import RentalMainMenu

def MainMenu() :
    os.system('clear')  # Clear the terminal before starting the program so everything is clear
    print(BlockDusterColors.colorFormat.CGREEN + ''' 
    ################################################################
    #                         ,          ,                         #
    # "Hi, BlockDuster       _|\_       /|                         #
    #   here, Rent Movies   /___ "\----' |                         #
    #        We Care"      /=====\ \     `-.                       #
    #               \    // .--.  \|  |      \                     #
    #                   /(  [@@]   )  /       \                    #
    #       ,          |  \ '--'  /  /         \-------            #
    #       |\_        |   \___.-'              \----- \           #
    #  __,--'' \.     /|   _____..----) )       |     \ \          #
    # "----____: \.  / | ('          /      |   |      \ \         #
    #           `. \/ /\  \._     _./      /    |       \ \        #
    #             \_./  \    '====        /    /         \ \       #
    #                    \     ---     --'    /           \ `.     #
    #                     \.              _,-;           /,--.\    #
    #                       \___________/\/ /            "    "    #
    #                                   \/ /_                      #
    #                                   /`/  |                     #
    #  _____ _                +"""".   / /|  /                     #
    # |_   _| |__   ___        \    \./ / | /                      #
    #   | | | '_ \ / _ \        `\ . | /  +"                       #
    #   | | | | | |  __/          \  |/                            #
    #   |_| |_| |_|\___|           (_)                             #
    #  __  __                 _                    ___             #
    # |  \/  | ___  _ __  ___| |_ ___ _ __ ___    |_ _|_ __   ___  # 
    # | |\/| |/ _ \| '_ \/ __| __/ _ \ '__/ __|    | || '_ \ / __| #
    # | |  | | (_) | | | \__ \ ||  __/ |  \__ \_   | || | | | (__  # 
    # |_|  |_|\___/|_| |_|___/\__\___|_|  |___( ) |___|_| |_|\___( # 
    #                                         |/                   # 
    #                                                              #
    #               YOUR FRIENDLY MOVIE RENTAL PLACE               #
    ################################################################
    ''' + BlockDusterColors.colorFormat.ENDC)

    print(''' 
    ################################################################
    #       MAIN MENU - Choose one of the options from below       #
    ----------------------------------------------------------------
    #      1-Customers | 2-Movies | 3-Rental A Movie| 4-EXIT       #         
    ################################################################
    ''')

MainMenu()
selection = 0
while selection != "4" :
    selection=input(BlockDusterColors.colorFormat.CBLUE + "     Make your selection.......: " + BlockDusterColors.colorFormat.ENDC)
    if selection == '1' :
        showCustomerMenu = 0
        while showCustomerMenu == 0 :
            showCustomerMenu = CustomerMainMenu.MainMenu()
        MainMenu()
    elif selection == '2' :
        showMovieMenu = 0
        while showMovieMenu == 0 :
            showMovieMenu = MoviesMainMenu.MainMenu()
        MainMenu()
    elif selection == '3' :
        showRentalMenu = 0
        while showRentalMenu == 0 :
            showRentalMenu = RentalMainMenu()
        MainMenu()
    elif selection == '4' :
        os.system('clear')
    else :
        print("invalid option")
