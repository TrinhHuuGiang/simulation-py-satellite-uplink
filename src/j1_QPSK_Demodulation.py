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
def QPSK_Dedulator(t, wt_af_LNA):
    """
    Khoi phuc song pha I|Q khi nhan voi song sin va cos
    - Khoi phuc song I|Q
    - Tinh them SNR
    """
    # nhan voi song mang
    wI_DEM = wt_af_LNA*np.cos(2*np.pi*gd.cw_f*t)
    wQ_DEM = wt_af_LNA*np.sin(2*np.pi*gd.cw_f*t)

    return wI_DEM, wQ_DEM

def SNR():
    """
    Tin hieu chiu tac dong tu cac nguon:
    - fading
    - thermal noise
    """