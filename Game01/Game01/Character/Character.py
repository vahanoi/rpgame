'''
Created on 27 Oct 2018

@author: vahanoi

name of game character
class
race
profession
specialisation

Mods:
Strenght
Agility
luck

'''

class Character(object):
    '''
    Game character class - Who, background sizes all in database
    '''
    #TODO: db table for a character

    def __init__(self, chname, race, chhealth, chenergy):
        '''
        Constructor
        
        '''
        # TODO: load character from database
        # TODO: tvaluedisplay - to display character params when testing /debug ON
        self.chname=chname
        self.chhealth=chhealth
        

    def battleshout(self):
        '''
        player 
        '''
        None
    
    kind=''
    
    