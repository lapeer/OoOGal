import numpy as np 
from astroquery.mast import Observations
from astroquery.mast import Mast
from astroquery.mast import MastMissions


from OoOGal import * 

HST_instruments = ['ACS', 'WFPC', 'WFC3', 'WFPC2', 'FOC', 'HSP' ]
JWST_instruments = ['NIRCAM']

def do_query_mast(Galaxy):

    '''
    Perform MAST search for a given Galaxy object 
    '''

    mast = Mast()

    #get the name of our object 
    name = Galaxy.name 
    
    #get the coords of the object 
    try:
        #first try to search by name 
        coords = mast.resolve_object(name, resolve_all=False)
    except:
        #then try to search by coordinates if name fails 
        coords = Galaxy.get_coords()

    results_arr = []

    #obtaining available photometric data for HST and JWST instruments 
    for telescope, instrument in zip(['HST', 'JWST'], [HST_instruments, JWST_instruments]):

        missions = MastMissions(mission = telescope)

        if telescope == 'HST':
            select_cols = ['sci_data_set_name', 'sci_instrume', 'sci_aper_1234', ' sci_spec_1234', 'sci_actual_duration', 'sci_central_wavelength']
            results = missions.query_object(name, sci_instrume = instrument)
            
            
        else: 
            select_cols = ['instrume', 'opticalElements', 'duration', 'program']
            results = missions.query_object(name, instrume = instrument)

        results_arr.append(results)
        

        instru_list = results['']




    



    return 

