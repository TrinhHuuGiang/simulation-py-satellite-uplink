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