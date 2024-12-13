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
def Gain_ant_para_1(wQPSK_af_BPF):
    '''
    Transmitter antenna
    '''
    # anh huong Gain len tin hieu
    wt_af_at1 = wQPSK_af_BPF*np.sqrt(gd.at1_G)

    return wt_af_at1
