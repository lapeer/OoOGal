#begin file! 
import numpy as np 

from astropy.coordinates import SkyCoord
import astropy.units as u

class Galaxy(object):
    """
    Galaxy class.

    Represents a galaxy object with its core observational properties.
    
    Args:
        name (str, optional): Name of the galaxy
        right_ascension (float, optional): Right ascension coordinate of the galaxy
        declination (float, optional): Declination coordinate of the galaxy
        redshift (float, optional): Redshift value of the galaxy
    """

    def __init__(self, name=None, right_ascension=None, declination=None, redshift=None):
        """
        Initialize Galaxy

        Creates a Galaxy instance with its core observational properties.

        Args:
            name (str, optional): Name of the galaxy
            right_ascension (float, optional): Right ascension coordinate of the galaxy
            declination (float, optional): Declination coordinate of the galaxy
            redshift (float, optional): Redshift value of the galaxy

        Returns:
            None
        """
        self.name = name
        self.RA = right_ascension
        self.Dec = declination
        self.redshift = redshift
        return

    def set_observations(self, obs_table):
        """
        Set Observations

        Assigns an observations table to the galaxy instance.
        Args:
            obs_table (Table): Astropy Table containing observational data for the galaxy
        Returns:
            None
        """

        self.observations = obs_table
        return

    def make_filter_plot(self):
        """
        Make Filter Plot

        Generates a plot displaying the throughput and available filters for the galaxy,
        based on its assigned observations table.
        Args:
            None
        Returns:
            plot: Figure showing filter throughput curves for all available filters
        """
        obs_table = self.observations
        return

    def get_coords(self):
        """
        Get Coordinates

        Reads in arbitrarily formatted object coordinates and constructs
        an Astropy SkyCoord object for use in astronomical queries.
        Args:
            None
        Returns:
            SkyCoord: Astropy SkyCoord object representing the galaxy's sky position
        """
        return


    
