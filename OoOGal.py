#begin file! 
import numpy as np 

class Galaxy(object): 
    """
    Galaxy class.
    
    """

    def __init__(self, name = None, right_ascension = None, 
                 declination = None):
        
        
        self.name = name 

        self.RA = right_ascension 

        self.Dec = declination 

        return 


    def init_galaxy_from_dict(self):

        
        '''
        Initalize a Galaxy object based on a list of properties 
        '''
        

        return 

        
    def query_ned(self):
        '''
        Query galaxy properties on NED. 
        '''

        gal_name = str(self.name)
    

        
