'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt
import numpy as np

import a1_global_specific_data as gd
'''*************************************************************
* code
*************************************************************'''
def QPSK_Modulator(t, rc_sI, rc_sQ):
    '''
    Dieu che QPSK
    '''
    # nhan song mang
    wI = gd.cw_Arms*np.sqrt(2)*(np.sqrt(2)/2)*rc_sI*np.cos(2*np.pi*gd.cw_f*t)
    wQ = gd.cw_Arms*np.sqrt(2)*(np.sqrt(2)/2)*rc_sQ*np.sin(2*np.pi*gd.cw_f*t)

    # tong hop thành sóng dieu che QPSK
    wQPSK = wI + wQ

    return wI, wQ, wQPSK

def plot_modulated_wave(t, wI, wQ, wQPSK):
    '''
    plot symbol after QPSK modulated
    - plot I phase, Q phase
    - plot QPSK wave
    '''
    # chon do thi
    plt.figure(gd.fig2)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot wI]
    plt.subplot(3,2,3) # 3 hang 2 cot, vi tri 3
    plt.title("In-phase x Cos(2.pi.fc+Phi)")
    plt.plot(t[:num_sample], wI[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()


    # [plot wQ]
    plt.subplot(3,2,5) # 3 hang 2 cot, vi tri 5
    plt.title("Quadrature x Sin(2.pi.fc+Phi)")
    plt.plot(t[:num_sample], wQ[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()


    # [plot wQPSK]
    plt.subplot(3,2,1) # 3 hang 2 cot, vi tri 1
    plt.title("QPSK waveform")
    plt.plot(t[:num_sample], wQPSK[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])
    
    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi