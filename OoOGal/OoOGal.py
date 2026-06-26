# begin file!
import numpy as np

from astropy.coordinates import SkyCoord
import astropy.units as u


class Galaxy(object):
    """
    Galaxy class.

    """

    def __init__(
        self, name=None, right_ascension=None, declination=None, redshift=None
    ):

        self.name = name

        self.RA = right_ascension

        self.Dec = declination

        self.redshift = redshift

        return

    def set_observations(self, obs_table):
        """
        Assigns observations Table to a given galaxy
        """
        self.observations = obs_table

        return

    def make_filter_plot(self):
        """
        Make a plot showing the throughput and filters available for a given galaxy
        """

        obs_table = self.observations

        return

    def get_coords(self):
        """
        Reads in arbitraily formated object coordinates and creates a SkyCoord object
        """

        # if the user does not input one or both:
        if self.Ra is None or self.dec is None:
            raise Exception("Must input a value for RA and Dec")

        # if the user inputs the

        return
