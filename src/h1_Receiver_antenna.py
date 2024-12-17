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
def Gain_ant_para_2(wt_af_fading, dB_total_fading):
    '''
    Receiver antenna
    - gain fading wave by anten
    '''
    # Tinh cong suat fading thu sau qua anten thu
    dB_at2_G =  10*np.log10(gd.at2_G)
    dB_total_after_ant2 = dB_total_fading + dB_at2_G

    # anh huong Gain len tin hieu
    wt_af_at2 = wt_af_fading*np.sqrt(gd.at2_G)

    return wt_af_at2, dB_at2_G, dB_total_after_ant2

def plot_wave_af_receiver_ant2(t, wt_af_at2):
    '''
    Plot tin hieu thu duoc sau khi suy hao cap noi phia thu
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot signal]
    plt.subplot(3,2,3) # 3 hang 2 cot, vi tri 3
    plt.title("Wave received (Grx)")
    plt.plot(t[:num_sample], wt_af_at2[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

