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
def freespace_loss(wt_af_rl):
    '''
    Freespace loss
    '''
    # Freespace Loss dB
    dB_Freespace = 92.44 + 20*np.log10(gd.pl_d) + 20*np.log10(gd.cw_f/(10**9))

    # wave transmit after rain loss
    Lfs = 10**(dB_Freespace/10)
    wt_af_freespace = wt_af_rl/np.sqrt(Lfs)

    return dB_Freespace, wt_af_freespace