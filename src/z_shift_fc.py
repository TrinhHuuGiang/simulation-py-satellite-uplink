'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt
import numpy as np
import os

import a1_global_specific_data as gd
from a1_sub_function import sequence_calculate, recalculate_when_shift_value
from b1_GenBit_PNRZ_IQsplit import RandBit_PNRZ_IQsplit
from b2_Time_division import time_and_signal_div
from b3_Raised_cosine_filter import raised_cos_filter
from c1_QPSK_modulation import QPSK_Modulator
from d1_Nonlinear_PA import Power_Amplifier
from d2_FIR_BPF import linear_FIR_BPF
from e1_Transmitter_antenna import Gain_ant_para_1
from f1_Rain_loss import rain_loss
from f2_Freespace_loss import freespace_loss
from g1_Rician_fading import rician_fading
from h1_Receiver_antenna import Gain_ant_para_2
from h2_Thermal_noise import thermal_noise
from i1_LNA import Low_Noise_Amplifier
from j1_QPSK_Demodulation import QPSK_Dedulator
from k1_LPF import FIR_LPF
from l1_Comparator import Comparator_signal
from l2_IQ_merge import Merge_bit_streams, BER
'''*************************************************************
* Code
*************************************************************'''
def repeat_log(order):
    # calculate global variable
    recalculate_when_shift_value(order)

    # calculate global variable
    sequence_calculate()

    # generate data stream
    bitstream, Istream, Qstream = RandBit_PNRZ_IQsplit()

    # time div axis
    t, sI_reshape, sQ_reshape = time_and_signal_div(Istream,Qstream)

    # raise cosine filt
    rc_time_h_t, rc_h_t, rc_sI, rc_sQ = raised_cos_filter(t, sI_reshape, sQ_reshape)

    # QPSK modulation
    wI, wQ, wQPSK = QPSK_Modulator(t, rc_sI, rc_sQ)

    # Power amplifier
    wQPSK_af_pa = Power_Amplifier(wQPSK)

    # linear FIR BPF
    wQPSK_af_BPF, FIR_bp_filter = linear_FIR_BPF(wQPSK_af_pa)

    # transmitter antenna
    wt_af_at1, dB_Ptx ,dB_cable_loss, dB_at1_G, dB_EIRP = Gain_ant_para_1(t, wQPSK_af_BPF)

    # rain loss
    dB_Rainloss, wt_af_rl = rain_loss(wt_af_at1)

    # Freespace loss
    dB_Freespace, wt_af_freespace = freespace_loss(wt_af_rl)

    # Rician fading
    dB_total_fading, wt_af_fading = rician_fading(dB_EIRP, dB_Rainloss, dB_Freespace, wt_af_freespace)

    # Receiver antenna
    wt_af_at2, dB_at2_G, dB_total_after_ant2 = Gain_ant_para_2(wt_af_fading, dB_total_fading)

    # Thermal noise
    wt_af_thermal, dB_total_receive, dB_C_N, dB_SNR = thermal_noise(wt_af_at2, dB_total_after_ant2)

    # LNA
    wt_af_LNA, dB_Prx, dB_rx_cable = Low_Noise_Amplifier(wt_af_thermal, dB_total_receive)

    # QPSK Demodulator
    wI_DEM, wQ_DEM = QPSK_Dedulator(t, wt_af_LNA)

    # LPF
    I_signal_LPF, Q_signal_LPF = FIR_LPF(wI_DEM, wQ_DEM)

    # Comparator
    I_bitstream_af_sample, Q_bitstream_af_sample = Comparator_signal(I_signal_LPF, Q_signal_LPF)

    # merge
    recover_stream_bit = Merge_bit_streams(I_bitstream_af_sample, Q_bitstream_af_sample)

    bit_err_rate = BER(bitstream, recover_stream_bit)

    return bit_err_rate, dB_C_N, dB_SNR

def plot_fc_expected_value(fc_map, BER_map, C_N_map, SNR_map):
    # ************  f - BER  *************
    plt.figure(gd.fig1) # tao plot figure
    plt.title("Carrier frequency - BER | K = {}".format(gd.rif_K))
    plt.plot(fc_map, BER_map)
    plt.ylabel("(%)")
    plt.xlabel("(Ghz)")

    # danh dau lai truc hoanh
    # plt.xticks(fc_map)

    # grid
    # plt.grid()

    # ************  f - C/N  *************
    plt.figure(gd.fig2) # tao plot figure
    plt.title("Carrier frequency - C/N")
    plt.plot(fc_map, C_N_map)
    plt.ylabel("(dB)")
    plt.xlabel("(Ghz)")
    # danh dau lai truc hoanh
    # plt.xticks(fc_map)

    # ************  f - SRN  *************
    plt.figure(gd.fig3) # tao plot figure
    plt.title("Carrier frequency - SNR")
    plt.plot(fc_map, SNR_map)
    plt.ylabel("SNR (dB)")
    plt.xlabel("(Ghz)")
    # danh dau lai truc hoanh
    # plt.xticks(fc_map)

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

'''*************************************************************
* Script
*************************************************************'''
num_sim = 50
fc_map = np.linspace(12*(10**9), 18*(10**9), num_sim)
BER_map = []
C_N_map = []
SNR_map = []

for f in fc_map: # thuc hien 25 lan
    gd.cw_f = f # thay doi global fc - tan so song mang

    n = 100
    count = n
    bit_err_rate = 0
    dB_C_N = 0
    dB_SNR = 0
    while count:
        print(count)
        count-=1 # 10^4 theo chuan ?

        Log_bit_err_rate, Log_dB_C_N, Log_dB_SNR = repeat_log(1)
        
        bit_err_rate+=Log_bit_err_rate
        dB_C_N+=Log_dB_C_N
        dB_SNR+=Log_dB_SNR

        os.system('cls' if os.name == 'nt' else 'clear')

    bit_err_rate/=n
    dB_C_N/=n
    dB_SNR/=n

    BER_map.append(bit_err_rate)
    C_N_map.append(dB_C_N)
    SNR_map.append(dB_SNR)
    
    print("\n","-"*10,"[fc = {}]".format(gd.cw_f),"-"*10)
    print("BER: {}%".format(bit_err_rate))
    print("C_N: {:.6}dB".format(dB_C_N))
    print("SNR: {:.6}dB".format(dB_SNR))
    

plot_fc_expected_value(fc_map, BER_map, C_N_map, SNR_map)

# plt.show sau khi da ve xong
# sau khi dong cac cua so figure, cac doi tuong fig1, fig2,... cung bi xoa
plt.show()         # in ra do thi