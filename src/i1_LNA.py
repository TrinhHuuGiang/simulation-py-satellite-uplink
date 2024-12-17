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

import a1_global_specific_data as gd
'''*************************************************************
* code
*************************************************************'''

def Low_Noise_Amplifier(wt_af_thermal, dB_total_receive):
    '''
    Cho tin hieu nhan qua LNA
    - loss by cable
    - Prx
    - Tin hieu ra khuech dai manh
    - Meo dang khong dang ke
    '''
    dB_rx_cable =  10*np.log10(gd.cable_loss)
    dB_Prx = dB_total_receive - dB_rx_cable

    # tinh toan tac dong LNA len tin hieu
    wt_af_LNA = gd.LNA_a1*wt_af_thermal + gd.LNA_a2*wt_af_thermal**2 + gd.LNA_a3*wt_af_thermal**3

    return wt_af_LNA, dB_Prx, dB_rx_cable

def plot_LNA_wave(t, wt_af_LNA):
    '''
    Plot received wave after LNA
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot wQPSK_af_pa]
    plt.subplot(3,2,5) # 3 hang 2 cot, vi tri 5
    plt.title("LNA ~ 60dB")
    plt.plot(t[:num_sample], wt_af_LNA[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi