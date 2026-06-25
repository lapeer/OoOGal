import numpy as np
from astroquery.mast import Observations
from astroquery.mast import Mast
from astroquery.mast import MastMissions
import astropy.table

from OoOGal import *

HST_instruments = ["ACS", "WFPC", "WFC3", "WFPC2", "FOC", "HSP"]
JWST_instruments = ["NIRCAM"]


def do_query_mast(Galaxy):
    """
    Query MAST

    Perform MAST search for an inputted Galaxy object. Searches for all available HST and JWST data.

    Args:
        Galaxy (object): Inputted galaxy

    Returns:
        Table: detailed information about the queried Galaxy object
    """

    mast = Mast()

    # get the name of our object
    name = Galaxy.name

    # get the coords of the object
    try:
        # first try to search by name
        coords = mast.resolve_object(name, resolve_all=False)
    except:
        # then try to search by coordinates if name fails
        coords = Galaxy.get_coords()

    results_arr = []

    # obtaining available photometric data for HST and JWST instruments
    for telescope, instrument in zip(
        ["HST", "JWST"], [HST_instruments, JWST_instruments]
    ):
        missions = MastMissions(mission=telescope)

        if telescope == "HST":
            select_cols = [
                "sci_data_set_name",
                "sci_instrume",
                "sci_aper_1234",
                "sci_spec_1234",
                "sci_actual_duration",
                "sci_central_wavelength",
                "sci_pep_id",
            ]
            results = missions.query_object(
                name, sci_instrume=instrument, select_cols=select_cols
            )

        else:
            select_cols = ["instrume", "opticalElements", "duration", "program"]
            results = missions.query_object(
                name, instrume=instrument, select_cols=select_cols
            )

        results_arr.append(results)

        # renaming column names to more comprehensible headers
        hst_results = results_arr[0]
        jwst_results = results_arr[1]

        hst_results.rename_column("sci_instrume", "instrument")
        hst_results.rename_column("sci_spec_1234", "filters")
        hst_results.rename_column("sci_actual_duration", "exposure time")
        hst_results.rename_column("sci_pep_id", "PID")
        hst_results.rename_column("sci_central_wavelength", "central wavelength")

        jwst_results.rename_column("instrume", "instrument")
        jwst_results.rename_column("opticalElements", "filters")
        jwst_results.rename_column("duration", "exposure time")
        jwst_results.rename_column("program", "PID")

        combined_arr = astropy.table.vstack(
            [hst_results, jwst_results], join_type="outer"
        )

    return
