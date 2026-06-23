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

    
    
