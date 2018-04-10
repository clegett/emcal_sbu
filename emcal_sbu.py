# -*- coding: utf-8 -*-
""" Process and plot FTIR emissivity data.

This module provides the methods necessary to read, process, plot, and save
emissivity data collected at Stony Brook University's Center for Planetary
Exploration. It duplicates the functionality of the davinci emcal() and
emcal2() functions and adds plotting capability.
"""

from matplotlib import pyplot as plt
import numpy as np
import h5py
import sys
import glob
import re

__author__ = 'Carey Legett'
__contact__ = 'carey.legett@stonybrook.edu'
__copyright__ = 'Copyright 2018, Stony Brook University'
__credits__ = ['Carey Legett', 'Dylan McDougall']
__date__ = '2018/02/19'
__deprecated__ = False
__email__ = 'carey.legett@stonybrook.edu'
__license__ = 'GPLv3'
__maintainer = 'Carey Legett'
__status__ = 'Development'
__version__ = '0.1'

class Spectrum(object):
    pass

def read_ftir_files():
    pass


