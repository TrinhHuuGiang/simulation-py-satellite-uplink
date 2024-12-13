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
def linear_FIR_BPF(wQPSK_af_pa):
    """
    Linear FIR Bandpass filter 

    """

    # Compute cutoff frequencies
    fir_f_low = gd.cw_f - gd.cw_Bandreal / 2
    fir_f_high = gd.cw_f + gd.cw_Bandreal / 2

    # Design FIR bandpass filter
    FIR_bp_filter = signal.firwin(
        numtaps=gd.bpf_order+1,  # Filter order + 1
        cutoff=[fir_f_low, fir_f_high],
        pass_zero=False,  # Bandpass filter
        fs=gd.cw_fs
    )

    # Apply linear filter
    wQPSK_af_BPF = signal.lfilter(FIR_bp_filter, 1.0, wQPSK_af_pa)

    return wQPSK_af_BPF, FIR_bp_filter

def plot_FIR_Hf(FIR_bp_filter):
    # Frequency response visualization
    w, h = signal.freqz(FIR_bp_filter, fs=gd.cw_fs) # default FIR

    # chon figure
    plt.figure(gd.fig2)
    plt.subplot(3,2,4) # vi tri 4

    # plot dap ung tan so bo loc FIR
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title("H(f) FIR Bandpass")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi




def plot_BPF_wQPSK(t, wQPSK_af_BPF):
    '''
    Plot QPSK wave after BPF
    '''
    # chon do thi
    plt.figure(gd.fig2)

    # so mau can mo phong
    num_sample = gd.num_mod_symbol*gd.N_sample_1sb

    # [plot wQPSK_af_BPF]
    plt.subplot(3,2,6) # 3 hang 2 cot, vi tri 6
    plt.title("BPF|order {}".format(gd.bpf_order))
    plt.plot(t[:num_sample], wQPSK_af_BPF[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

