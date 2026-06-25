from MAST import * 
from OoOGal import * 


def test_query_MAST():

    galaxy_name = 'M51'
    galaxy = Galaxy(name = galaxy_name)
    #print(galaxy)

    mast_results = do_query_mast(galaxy)

    print(mast_results)

    return 

test_query_MAST()