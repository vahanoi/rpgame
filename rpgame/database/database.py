'''
Created on 3 Nov 2018

@author: vahan
'''
import sqlite3
from sys import exit

class database:
    '''
    Check if DB exists if not, create and init game database, insert default data
    '''

    
    def __init__(self, dbname):
        '''
        Constructor
        '''
                
        
    def create (self, dbname):
        db = sqlite3.connect(dbname)
        
    def close (self):
        None

if __name__ == '__main__':
    print("Please run rpgame.py")
    exit (2)
        