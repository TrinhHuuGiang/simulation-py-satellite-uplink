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
def Gain_ant_para_2(dB_total_receive, wt_af_thermal):
    '''
    Receiver antenna
    - gain by anten
    - loss by cable
    - Prx
    '''
    # Tinh cong suat thu sau qua anten thu, cable loss
    dB_rx_cable =  10*np.log10(gd.cable_loss)
    dB_at2_G =  10*np.log10(gd.at2_G)
    dB_Prx = dB_total_receive + dB_at2_G - dB_rx_cable

    # anh huong Gain, cable loss len tin hieu
    wt_af_at2 = wt_af_thermal*np.sqrt(gd.at1_G/gd.cable_loss)

    return wt_af_at2, dB_Prx, dB_at2_G, dB_rx_cable

def plot_wave_af_receiver_ant2_cable_loss(t, wt_af_at2):
    '''
    Plot tin hieu thu duoc sau khi suy hao cap noi phia thu
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot signal]
    plt.subplot(3,2,3) # 3 hang 2 cot, vi tri 3
    plt.title("Wave received (Grx, cable loss)")
    plt.plot(t[:num_sample], wt_af_at2[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

