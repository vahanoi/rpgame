"""
Created on 27 Oct 2018

@author: vahanoi

Kind of game rollplay
"""

import sqlite3

from Character.Character import *


def main():
    ch = Character("","","")
    print(f'Hi this is a game')
    # create sqlite database
    db = sqlite3.connect('game.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS player
                    (id,name,race,experience)''')

# main loop
    while True:
        print ('\n\n Would you start game? [Y/N] Any other key go')
        key = input()
        if key == 'N' or key == 'n':
            db.close()
            break
        suname=input(f"What will be your name? ")

        sracename=input(f"chose a race[Human/Drakl/Blump] ")


if __name__ == '__main__':
    main()
