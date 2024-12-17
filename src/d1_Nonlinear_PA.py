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

def Power_Amplifier(wQPSK):
    '''
    Cho tin hieu sau dieu che qua PA
    - Tin hieu ra co meo dang
    '''
    # tinh toan tac dong PA phi tuyen len QPSK
    wQPSK_af_pa = gd.pa_a1*wQPSK + gd.pa_a2*wQPSK**2 + gd.pa_a3*wQPSK**3

    return wQPSK_af_pa

def plot_PA_wQPSK(t, wQPSK_af_pa):
    '''
    Plot QPSK wave after PA
    '''
    # chon do thi
    plt.figure(gd.fig2)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot wQPSK_af_pa]
    plt.subplot(3,2,2) # 3 hang 2 cot, vi tri 2
    plt.title("QPSK after PA | Beta ~ {:.3} times".format(gd.pa_a1))
    plt.plot(t[:num_sample], wQPSK_af_pa[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi