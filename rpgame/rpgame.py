"""
Created on 27 Oct 2018

@author: vahanoi

RPG game created as a python learning exercise.

"""

import sqlite3 
import sys
import msvcrt as m # wait for keypress
from character.character import *

def splashscreen():
    print(f'Hi this is a RPGame - test game written in Python \n')
    print('Please chose your Name and Race below \n\n')   

def main():
    ch = Character("","","")

    # create sqlite database
    db = sqlite3.connect('game.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS player
                    (id,name,race,experience)''')

# main loop
    while True:
        splashscreen() #general info about a game - text
        print ('\n\n Would you start game? [Y/N]')
        key = input('Do you need me to start the Game [Y/N]')
        if key == 'N' or key == 'n':
            db.close()
            print('\n\nClosing awesome world!!!!!\n\n')
            sys.exit(0)
        elif key=='Y' or key=='y':
            suname=input(f"What will be your name? ")
            print(f'Chosen name: {suname}')
            sracename=input(f"chose a race[Human/Drakl/Blump] ")
            print(f'Chosen name: {sracename}')
        else: print('have you read info yet???')

if __name__ == '__main__':
    main()
