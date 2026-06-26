import numpy as np
from astroquery.mast import Mast
from astroquery.mast import MastMissions
import astropy.table
import astropy

from OoOGal import *

# instruments that provide photometric data
HST_instruments = ["ACS", "WFPC", "WFC3", "WFPC2", "FOC", "HSP"]
JWST_instruments = ["NIRCAM", "MIRI"]


def do_query_mast(Galaxy):
    """
    Query MAST

    Perform MAST search for an inputted Galaxy object. Searches for all available HST and JWST photometric data.

    Args:
        Galaxy (object): Inputted galaxy

    Returns:
        Table: detailed information about the queried Galaxy object
        file: .txt file containing the table in ascii format
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
                "sci_instrume",
                "sci_spec_1234",
                "sci_actual_duration",
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

    for res, cols in zip(
        results_arr,
        [
            [
                "sci_instrume",
                "sci_spec_1234",
                "sci_pep_id",
            ],
            ["instrume", "opticalElements", "program"],
        ],
    ):
        columns = np.array(res.colnames)
        mask_remove = [False if i in cols else True for i in columns]

        columns_to_remove = columns[mask_remove]
        res.remove_columns(columns_to_remove)

    # renaming column names to more comprehensible headers
    hst_results = results_arr[0]
    jwst_results = results_arr[1]

    hst_results.rename_column("sci_instrume", "instrument")
    hst_results.rename_column("sci_spec_1234", "filters")
    # hst_results.rename_column("sci_actual_duration", "exposure time")
    hst_results.rename_column("sci_pep_id", "PID")

    jwst_results.rename_column("instrume", "instrument")
    jwst_results.rename_column("opticalElements", "filters")
    # jwst_results.rename_column("duration", "exposure time")
    jwst_results.rename_column("program", "PID")

    combined_arr = astropy.table.vstack([hst_results, jwst_results], join_type="outer")

    combined_arr = astropy.table.unique(combined_arr)

    # assign observations to Galaxy object

    # return a .txt file with the output
    filename = "MASTquery_output.txt"
    with open(filename, "w") as file:
        file.write("\t".join(combined_arr.colnames) + "\n")
        for row in combined_arr:
            file.write("\t".join(str(row[col]) for col in combined_arr.colnames) + "\n")

    return combined_arr
