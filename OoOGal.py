#begin file! 
import numpy as np 

class Galaxy(object): 
    """
    Galaxy class.
    
    """

    def __init__(self, name = None, right_ascension = None, 
                 declination = None, redshift = None):
        
        self.name = name 

        self.RA = right_ascension 

        self.Dec = declination 

        self.redshift = redshift 

        return 


    def init_galaxy_from_file(self):

        
        '''
        Initalize a Galaxy object based on a list of properties 
        '''

        return 
    
    def query_mast(self):


        '''
        Queries MAST to check available data 
        '''
        return 
    
    def check_all_data(self):

        '''
        Searches all available data
        '''

        
    



        
