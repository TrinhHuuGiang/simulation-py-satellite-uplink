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
def FIR_LPF(wI_DEM, wQ_DEM):
    # [Loc thong thap]
    fir_f_cutoff = gd.cw_Bandreal/2

    # Design FIR lowpass filter
    FIR_lp_filter = signal.firwin(
        numtaps=gd.bpf_order+1,  # Filter order + 1
        cutoff=fir_f_cutoff,  # Lowpass cutoff frequency
        pass_zero=True,  # Lowpass filter
        fs=gd.cw_fs
    )

    # Apply linear filter
    I_signal_LPF = signal.lfilter(FIR_lp_filter,1.0, wI_DEM)
    Q_signal_LPF = signal.lfilter(FIR_lp_filter,1.0, wQ_DEM)

    return I_signal_LPF, Q_signal_LPF

def plot_DemodQPSK_LPF(t, I_signal_LPF, Q_signal_LPF):
    '''
    Plot I|Q signal after LPF
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot In-phase]
    plt.subplot(3,2,4) # 3 hang 2 cot, vi tri 4
    plt.title("LPF In-phase")
    plt.plot(t[:num_sample], I_signal_LPF[:num_sample])
    plt.xlabel("(s)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # [plot Quadrature]
    plt.subplot(3,2,6) # 3 hang 2 cot, vi tri 2
    plt.title("LPF Quadrature")
    plt.plot(t[:num_sample], Q_signal_LPF[:num_sample])
    plt.xlabel("(s)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi