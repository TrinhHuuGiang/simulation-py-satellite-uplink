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
def thermal_noise(wt_af_fading):
    '''
    Thermal noise
    -> C/N
    -> Lay thermal noise theo tai lieu la 290K
    -> Chon khoang dao dong tu 270 den 300K
    '''
    # dB_total_receive: cong suat nhan duoc tai anten sau khi chiu fading, path loss, rain
    # gd.T: nhiet do tap am tai anten

    # tao mang T tuan theo Uniform
    T_min = 270
    T_max = 300
    sample = len(wt_af_fading)

    gd.thn_T = np.random.uniform(T_min, T_max, sample)

    # Tap am nhiet anh huong len tin hieu
    N_ther = gd.thn_k * gd.thn_T * gd.cw_Bandreal # Woat

    wt_af_thermal = wt_af_fading + np.sqrt(N_ther)

    # Tinh C/N
    aver_Pc = np.mean(wt_af_thermal**2)  # Trung bình công suất tín hiệu
    aver_Pn = np.mean(N_ther)  # Trung bình công suất nhiễu

    C_N = aver_Pc / aver_Pn
    dB_C_N = 10*np.log10(C_N)

    # Power after all noise, fading
    dB_total_receive = 10*np.log10(aver_Pc)

    return wt_af_thermal, dB_total_receive, dB_C_N

def plot_wave_after_thermal_noise(t, wt_af_thermal, dB_C_N):
    '''
    Plot wave after thermal noise
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_rician_symbol*gd.cw_sample

    # [plot thermal noise + C/N]
    plt.subplot(3,2,2) # 3 hang 2 cot, vi tri 2
    plt.title("with Thermal noise| C/N {:.5}dB".format(dB_C_N))
    plt.plot(t[:num_sample], wt_af_thermal[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

