from MAST import * 
from OoOGal import * 

def test_galaxy_object():

    galaxy_name = 'M51'
    galaxy = Galaxy(name = galaxy_name)

    assert Galaxy.name == 'M51'


    return 

def test_query_MAST():

    galaxy_name = 'M51'
    galaxy = Galaxy(name = galaxy_name)
    

    mast_results = do_query_mast(galaxy)


    assert len(mast_results) == 164 
    assert mast_results.colnames == ['instrument', 'filters', 'PID']

    return 

test_query_MAST()