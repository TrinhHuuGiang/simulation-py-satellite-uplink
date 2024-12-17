# Satellite Uplink Simulation Program
# Copyright (C) 2024 SatComm 11

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

import a1_global_specific_data as gd
'''*************************************************************
* code
*************************************************************'''
def QPSK_Dedulator(t, wt_af_LNA):
    """
    Khoi phuc song pha I|Q khi nhan voi song sin va cos
    - Khoi phuc song I|Q
    - Tinh them SNR
    """
    # nhan voi song mang
    wI_DEM = wt_af_LNA*np.cos(2*np.pi*gd.cw_f*t)
    wQ_DEM = wt_af_LNA*np.sin(2*np.pi*gd.cw_f*t)

    return wI_DEM, wQ_DEM

def SNR():
    """
    Tin hieu chiu tac dong tu cac nguon:
    - fading
    - thermal noise
    """