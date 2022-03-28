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
import os, BlockDusterColors

def MainMenu() :
    os.system('clear')  # Clear the terminal before starting the program so everything is clear
    print('''                                                                              
                                                        _                      
                                                   .--"" `"-.                  
                                                  / .,---.__ \                 
                                                 : ""\,;`/."/`                 
                                                 `-^\`  __,_.'-.               
                                                   _}"""    \   `-.            
                                                 .'          `, /"             
                                                /          ,@" \`              
                                                `"}@"   `       ;              
                                                  |      ,      ;`.            
                                                  ;       ;      ; ;           
                                                 / ,      :      ; |           
                                                ;  |      `;    /  ;           
                                                : .J       ;,_,'    \          
                                               / :  \       ;  \     ;         
                                              ;  ;   }     L.---Y_   |         
                                              | /   .'   .' _.,_  `-,!         
                                      _..__   ;/   /SSs,l_.L :. `-,   `,       
                                    .'.--""   y   /S,, S;;   ! `-. `.   :      
                                   ; F      .'  .' /`  { J  /     `-.`,_J      
                           @-.-._@ \ `-._.-'  .'  {,___.'  /         ;         
                ___        `.`-'.'  `.    _.-';   F      ,'          ;         
             .="  _`-.       ;":      `"""    |   `.__.-"           ;          
           _J`}_,"<@,`-.     : '.             |                    .'          
         .',  ` =__, `-' ,_  l  |;            ;      ;""_          :           
        / .]     ; ,7_.';\=`T   ;`.          .'      ; F",        .'           
       / / \    /  ' ;  `.__,'  i-"`,        ;      ;  ; |        ;            
      : ;  :_.-'     ;      J    \_='         \     |  | ;       .'            
      ; i  / \__,.-I |     {     _J            }    :  :/        :             
      J. } ; : F   ; :      \`-,' ;          .'     _\ _; _,      \            
     / ;F  ; ; \  /,.`.     .i,|,-L          |_.-.,"  }  ;  :/"",' ;   fsc     
     `-^^--' '--' '---'    '---^---'         `-^--^--^---^---^--^--'           
    ---------------------------- MOVIES LIBRARY ----------------------------
    ''')

    print(''' 
    ##################################################################################
    #    Movies Library - Choose one of the options from below                        #
    ----------------------------------------------------------------------------------
    #    1-Movie List | 2-Add Movie | 3-Edit Movie | 4-Delete Movie | 5-Main Menu    #         
    ##################################################################################
    ''')
    selection = 0
    while selection != "5" :
        selection=input(BlockDusterColors.colorFormat.CBLUE + "     Movies Library selection.......:" + BlockDusterColors.colorFormat.ENDC)
        if selection == '1' :
            print("Movie List")
        elif selection == '2' :
            print("Add Movie")
        elif selection == '3' :
            print("Edit Movie")
        elif selection == '4' :
            print("Delete Movie")
        elif selection == '5' :
            os.system('clear')
        else :
            print("invalid option")
