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
def Gain_ant_para_1(t, wQPSK_af_BPF):
    '''
    Transmitter antenna
    - loss by cable
    - gain by anten
    - EIRP
    '''
    # Tinh cong suat phat trung binh
    Ptx_real = np.mean(wQPSK_af_BPF**2)  # Trung bình công suất tín hiệu


    # anh huong cua suy hao cap noi
    # anh huong Gain len tin hieu
    wt_af_at1 = wQPSK_af_BPF*np.sqrt(gd.at1_G/gd.cable_loss)

    # (dB) Ptx,cable, anten1 Gain, EIRP
    dB_Ptx = 10*np.log10(Ptx_real)
    dB_cable_loss = 10*np.log10(gd.cable_loss)
    dB_at1_G = 10*np.log10(gd.at1_G)
    dB_EIRP = dB_Ptx - dB_cable_loss + dB_at1_G

    return wt_af_at1, dB_Ptx ,dB_cable_loss, dB_at1_G, dB_EIRP

