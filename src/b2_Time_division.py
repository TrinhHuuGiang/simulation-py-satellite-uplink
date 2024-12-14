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
    sI_reshape = np.ravel(np.tile(Istream, (gd.N_sample_1sb, 1)),order='F') # order F lay theo cot
    sQ_reshape = np.ravel(np.tile(Qstream, (gd.N_sample_1sb, 1)),order='F')

    # time axis - gioi han boi so bit
    t = np.arange(0, (gd.N_bit / 2) * gd.T_sb, gd.cw_Ts)

    # fix bat dong bo mau
    delta_sam = len(t)-len(sI_reshape)
    if(delta_sam > 0): t = t[:len(sI_reshape)]#cat bot ho toi t
    elif(delta_sam <0): 
        # Tao mang thoi gian them
        extra_time = np.arange(t[-1] + gd.cw_Ts, t[-1] + gd.cw_Ts * (-delta_sam), gd.cw_Ts)
        t = np.concatenate((t, extra_time))

    return t, sI_reshape, sQ_reshape

