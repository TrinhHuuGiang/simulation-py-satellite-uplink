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
import random 

import a1_global_specific_data as gd

'''*************************************************************
* Code
*************************************************************'''
def RandBit_PNRZ_IQsplit():
    # Tao chuoi bit
    bitstream = np.array([random.randint(0, 1) for _ in range(gd.N_bit)])

    # Ma hoa PNRZ
    PNRZstream = 2*bitstream-1

    #  Tach bit I,Q
    Istream = PNRZstream[0::2]
    Qstream = PNRZstream[1::2]

    return bitstream, Istream, Qstream


def plot_Bit_and_Symbol(bitstream, Istream, Qstream):
    # chon do thi
    plt.figure(gd.fig1)
    
    # plot bit stream
    x_positions = np.arange(0,gd.num_src_bit+1,1)
    plt.subplot(3,2,1) # 3 hang 2 cot, vi tri 1
    plt.title("Bit stream")
    plt.step(np.arange(0,gd.num_src_bit+1,1),bitstream[:gd.num_src_bit+1], where='post')
    
    plt.xticks(x_positions)
    
    # grid
    plt.grid()

    # plot I stream
    x_positions = np.arange(0,gd.num_src_symbol+1,1)
    plt.subplot(3,2,3) # 3 hang 2 cot, vi tri 3
    plt.title("I-PNRZ")
    plt.step(x_positions,Istream[:gd.num_src_symbol+1], where='post')

    plt.xticks(x_positions)
    
    # grid
    plt.grid()

    # plot Q stream
    plt.subplot(3,2,5) # 3 hang 2 cot, vi tri 5
    plt.title("Q-PNRZ")
    plt.step(x_positions,Qstream[:gd.num_src_symbol+1], where='post')

    plt.xticks(x_positions)
    
    # grid
    plt.grid()
    
    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi
