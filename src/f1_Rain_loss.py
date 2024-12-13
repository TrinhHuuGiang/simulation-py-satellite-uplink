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
def rain_loss(wt_af_at1):
    '''
    Rain loss
    '''
    # Rain Loss dB
    dB_Rainloss = gd.rl_a*gd.rl_Dr

    # wave transmit after rain loss
    Rl = 10**(dB_Rainloss/10)
    wt_af_rl = wt_af_at1*np.sqrt(Rl)

    return dB_Rainloss, wt_af_rl