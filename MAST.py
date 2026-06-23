import numpy as np 
from astroquery.mast import Observations
from astroquery.mast import Mast


from OoOGal import * 


def do_query_mast(Galaxy):

    '''
    Perform MAST search for a given Galaxy object 
    '''

    mast = Mast()

    #get the name of our object 
    name = Galaxy.name 
    
    #get the coords of the object 
    try:
        coords = mast.resolve_object(name, resolve_all=False)
    except:
        coords = Galaxy.get_coords()



    #first try to search by name 

    #then try to search by coordinates if name fails 



    return 

