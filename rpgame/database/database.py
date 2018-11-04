'''
Created on 3 Nov 2018

@author: vahanoi
'''
import sqlite3
import os.path
from sys import exit

class database:
    '''
    Check if DB exists if not, create and init game database, insert default data
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
                
        
    def create (self, dbname):
        ''' check if game database exist
            if not - create and insert data
            if yes - check if records exists
                if no - add records
                if yes - skip and go
        
        '''
        if os.path.isfile(dbname): #TODO: check this not sure if will work
            print(os.path.isfile(dbname))
            db = sqlite3.connect(dbname)
            c = db.cursor()
            #TODO: check if tables exists before creating
            # Create tables
            c.execute('''SELECT COUNT(name) FROM sqlite_master WHERE type=\'table\'''')
            if c.fetchone() == 0:
                c.execute('''CREATE TABLE IF NOT EXISTS character
                    (id,name,race,experience)''')
                c.execute('''CREATE TABLE IF NOT EXISTS race 
                    (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom)''')
                # insert race data
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('1','Human','75','50','55','55','65','60');''') 
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('2','Drakl','85','45','55','75','55','45');''')
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('3','Blump','55','55','70','55','60','70');''')
                db.commit()
            else:
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('1','Human','75','50','55','55','65','60');''') 
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('2','Drakl','85','45','55','75','55','45');''')
                c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('3','Blump','55','55','70','55','60','70');''')
                db.commit()
        else:
            db = sqlite3.connect(dbname)
            c = db.cursor()
            # Create tables
            c.execute('''CREATE TABLE IF NOT EXISTS character
                    (id,name,race,experience)''')
            c.execute('''CREATE TABLE IF NOT EXISTS race 
                    (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom)''')
            # insert race data
            c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('1','Human','75','50','55','55','65','60');''') 
            c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('2','Drakl','85','45','55','75','55','45');''')
            c.execute('''insert into race (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
                    values ('3','Blump','55','55','70','55','60','70');''')
            db.commit()
        return (db)
    
    def close (self,dbname):
        dbname.close()

if __name__ == '__main__':
    print("Please run rpgame.py")
    exit (2)
        