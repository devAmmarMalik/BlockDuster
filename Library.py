# Python 3
# coding: utf-8

__author__ = "Per Scholas - Cohort 5 - Python team"
__copyright__ = "Copyright 2022, The Movie Rental Project"
__credits__ = ["Ammar Malik", "", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

# Purpose: Clear terminal screen for the next user interface to be shown
def clearTerminal():
    # import only system from os
    from os import system, name
    if name == 'nt':
        _ = system('cls')   # for windows
    else:
        _ = system('clear') # for mac and linux(here, os.name is 'posix')
