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
