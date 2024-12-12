'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

import a1_global_specific_data as gd
'''*************************************************************
* code
*************************************************************'''
def time_and_signal_div(Istream, Qstream):
    '''
    - Tao truc thoi gian cho mo phong
    - Lay mau tin hieu theo tan so lay mau song mang cw_fs
    '''
    # lay mau tin hieu theo tan so lay mau song mang
    sI_reshape = np.ravel(np.tile(Istream, (gd.N_sample_1sb, 1)),order='F')
    sQ_reshape = np.ravel(np.tile(Qstream, (gd.N_sample_1sb, 1)),order='F')

    # time axis - gioi han boi so bit
    t = np.arange(0, (gd.N_bit / 2) * gd.T_sb, gd.cw_Ts)

    return t, sI_reshape, sQ_reshape

