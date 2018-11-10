'''
Created on 3 Nov 2018

@author: vahanoi
'''
import sqlite3
import os.path
from sys import exit


class database:
    '''Check if DB exists if not, create and init game database, insert default data.
    
    '''
    
    def __init__(self):
        '''
        Constructor
        '''

    def createtables(self, dbcursor):
        ''' Create game tables during game initialisation
            full table structure
        '''
        dbcursor.execute('''CREATE TABLE IF NOT EXISTS character
                    (id,name,race,experience)''')
        dbcursor.execute('''CREATE TABLE IF NOT EXISTS race 
                    (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom)''')
        
    def insertdata(self, dbcursor):
        '''insert race data
        TODO: add race description with more details
        '''
        dbcursor.execute('''insert into race 
               (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
               values ('1','Human','75','50','55','55','65','60');''') 
        dbcursor.execute('''insert into race 
               (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
               values ('2','Drakl','85','45','55','75','55','45');''')
        dbcursor.execute('''insert into race 
               (id,rname,rstrenght,rluck,rdexterity,rstamina,rsocial,rwisdom) 
               values ('3','Blump','55','55','70','55','60','70');''')
        
    def create (self, dbname, debug):
        ''' check if game database exist
            if not - create and insert data
            if yes - check if records exists
                if no - add records
                if yes - skip and go
        
        '''
        if os.path.isfile(dbname): # If DB file exists
            if debug==True:
                print(os.path.isfile(dbname))
            db = sqlite3.connect(dbname)
            c = db.cursor()
            # TODO: check if tables exists before creating
            # Create tables
            c.execute('''SELECT COUNT(name) FROM sqlite_master WHERE type=\'table\'''')
            if c.fetchone() == 0:
                self.createtables(self, c)
                self.insertdata(self, c)
                db.commit()
            else:
                c.execute('SELECT count(rname) FROM race')
                if c.fetchone == 0:
                    self.insertdata(self, c)
                    db.commit()
        else:
            db = sqlite3.connect(dbname)
            c = db.cursor()
            # Create tables
            self.createtables(self, c)
            # insert race data
            self.insertdata(self, c)
            db.commit()
        return (db)
    
    def close (self, dbname):
        dbname.close()


if __name__ == '__main__':
    print("Please run rpgame.py")
    exit (2)
        
