#####################################################################
#                                                                   #
# /naqslab_devices/SignalGenerator/Models.py                        #
#                                                                   #
# Copyright 2018, David Meyer                                       #
#                                                                   #
# This file is part of the naqslab devices extension to the         #
# labscript_suite. It is licensed under the Simplified BSD License. #
#                                                                   #
#                                                                   #
#####################################################################
from __future__ import division, unicode_literals, print_function, absolute_import
from labscript_utils import PY2
if PY2:
    str = unicode

from naqslab_devices.SignalGenerator.labscript_device import SignalGenerator

__version__ = '0.1.0'
__author__ = ['dihm']
                     
class RS_SMF100A(SignalGenerator):
    description = 'Rhode & Schwarz SMF100A Signal Generator'
    # define the scale factor - converts between BLACS front panel and 
    # Writing: scale*desired_freq // Reading:desired_freq/scale
    scale_factor = 1.0e9 # ensure that the BLACS worker class has same scale_factor
    freq_limits = (100e3, 22e9) # set in scaled unit (Hz)
    amp_scale_factor = 1.0 # ensure that the BLACS worker class has same amp_scale_factor
    amp_limits = (-26, 18) # set in scaled unit (dBm) 
    
class RS_SMHU(SignalGenerator):
    description = 'RS SMHU Signal Generator'
    # define the scale factor - converts between BLACS front panel and 
    # Writing: scale*desired_freq // Reading:desired_freq/scale
    scale_factor = 1.0e6 # ensure that the BLACS worker class has same scale_factor
    freq_limits = (100e3, 4320e6) # set in scaled unit (Hz)
    amp_scale_factor = 1.0 # ensure that the BLACS worker class has same amp_scale_factor
    amp_limits = (-140, 13) # set in scaled unit (dBm)
    # Output high can be adjusted up to 19dBm without spec guarantee
    # above 13 will generate error warnings
    
class HP_8643A(SignalGenerator):
    description = 'HP 8643A Signal Generator'
    # define the scale factor - converts between BLACS front panel and 
    # Writing: scale*desired_freq // Reading:desired_freq/scale
    scale_factor = 1.0e6 # ensure that the BLACS worker class has same scale_factor
    freq_limits = (260e3, 1030e6) # set in scaled unit (Hz)
    amp_scale_factor = 1.0 # ensure that the BLACS worker class has same amp_scale_factor
    amp_limits = (-137, 13) # set in scaled unit (dBm)
    
class HP_8642A(SignalGenerator):
    description = 'HP 8642A Signal Generator'
    # define the scale factor - converts between BLACS front panel and 
    # Writing: scale*desired_freq // Reading:desired_freq/scale
    scale_factor = 1.0e6 # ensure that the BLACS worker class has same scale_factor
    freq_limits = (100e3, 1057.5e6) # set in scaled unit (Hz)
    amp_scale_factor = 1.0 # ensure that the BLACS worker class has same amp_scale_factor
    amp_limits = (-140, 20) # set in scaled unit (dBm)
    # Output limits depend on frequency. Can be as low as 17 dBm
