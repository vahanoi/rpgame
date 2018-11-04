"""
Created on 27 Oct 2018

@author: vahanoi

RPG game created as a python learning exercise.

"""

import sqlite3 
import sys
from database.database import *

from character.character import *

class cls(object):
    def __repr__(self):
        import os

        os.system('cls' if os.name == 'nt' else 'clear')
        return ''
cls = cls()
def splashscreen():
    '''
    Display initial splash screen for the game
    Multi-line
    
    '''
    print(f'''
Hi this is a RPGame - test game written in Python \n
Please chose your Name and Race below \n\n
        ''')   

def main():
    '''
    Create sqlite database
    TODO: create separate module database tohandle most of database requests
    TODO: DB as a object so starting and initial checks in a separate module
    TODO: indexing
    CREATE UNIQUE INDEX `` ON `character` (
    `id` );
    '''
    db = database.create('','game.db')
    #####db = sqlite3.connect('game.db')
    c = db.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS character
    #                (id,name,race,experience)''')
    # c.execute('''CREATE TABLE IF NOT EXISTS race 
    #                (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom)''')
    '''
    insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
            values ('1','Human','75','50','55','55','65','60'); 
    insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
            values ('2','Drakl','85','45','55','75','55','45'); 
    insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
            values ('3','Blump','55','55','70','55','60','70');
    '''
    c.execute('''''')
    '''
    TODO: Create Race table with race parameters (max 3)
    id, 
    rname,
    race modifiers - strength, luck, dexterity, Stamina, Social, wisdom
    
    '''
    debug=True
# main loop
    while True:
        # General info about a game - text
        splashscreen() 
        key = input('Do you need me to start the Game [Y/N]')
        '''
        Exit game procedure - db closing
        '''
        if key == 'N' or key == 'n': # N to exit
            database.close('',db)
            #db.close() # Closing database
            print('\n\nClosing awesome world!!!!!\n\n')
            #curses.nocbreak()
            #curses.echo()
            cls
            sys.exit(0)
        elif key=='Y' or key=='y':
            print('Loading the RPGame......\n\n')
            chname=input(f"What will be your name> ")
            t=(chname,)
            if debug==True: 
                print(f'Chosen name: {chname} Checking if exists.')
            # TODO: check if name exists in DB if yes load it if no create new
            c.execute ('SELECT * FROM character WHERE name=?',t)
            result=c.fetchone()
            
            if debug==True:
                print(result)
            if result==None:
                print("\nNow time has come to chose your tribe")
                racename=input(f"chose a race[Human/Drakl/Blump] ")
                print(f'Chosen name> {racename}')
            else:
                input('Character exists. Load Character?')
        else: print('\n\nHave you read info yet???')
    ch = Character(chname,racename,"")
    
if __name__ == '__main__':
    main()
