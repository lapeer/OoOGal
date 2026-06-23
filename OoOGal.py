#begin file! 
import numpy as np 

from astropy.coordinates import SkyCoord
import astropy.units as u

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
    
    def get_coords(self):
        '''
        Reads in arbitraily formated object coordinates and creates a SkyCoord object
        '''

        return


    
