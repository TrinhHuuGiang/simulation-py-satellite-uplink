'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt

from a1_sub_function import sequence_calculate
from b1_GenBit_PNRZ_IQsplit import RandBit_PNRZ_IQsplit, plot_Bit_and_Symbol
from b2_Time_division import time_and_signal_div
from b3_Raised_cosine_filter import raised_cos_filter, plot_ht_raise_cosine_filter, plot_symbol_rc_filted
from c1_QPSK_modulation import QPSK_Modulator, plot_modulated_wave
from d1_Nonlinear_PA import Power_Amplifier, plot_PA_wQPSK
from d2_FIR_BPF import linear_FIR_BPF, plot_FIR_Hf, plot_BPF_wQPSK
from e1_Transmitter_antenna import Gain_ant_para_1
from f1_Rain_loss import rain_loss
from f2_Freespace_loss import freespace_loss
'''*************************************************************
* Code
*************************************************************'''
# calculate global variable
sequence_calculate()

# generate data stream
bitstream, Istream, Qstream = RandBit_PNRZ_IQsplit()

plot_Bit_and_Symbol(bitstream, Istream, Qstream)

# time div axis
t, sI_reshape, sQ_reshape = time_and_signal_div(Istream,Qstream)

# raise cosine filt
rc_time_h_t, rc_h_t, rc_sI, rc_sQ = raised_cos_filter(t, sI_reshape, sQ_reshape)

plot_ht_raise_cosine_filter(t, rc_time_h_t, rc_h_t)

plot_symbol_rc_filted(t, rc_sI, rc_sQ)

# QPSK modulation
wI, wQ, wQPSK = QPSK_Modulator(t, rc_sI, rc_sQ)

plot_modulated_wave(t, wI, wQ, wQPSK)

# Power amplifier
wQPSK_af_pa = Power_Amplifier(wQPSK)

plot_PA_wQPSK(t, wQPSK_af_pa)

# linear FIR BPF
wQPSK_af_BPF, FIR_bp_filter = linear_FIR_BPF(wQPSK_af_pa)

plot_FIR_Hf(FIR_bp_filter)

plot_BPF_wQPSK(t, wQPSK_af_BPF)

# transmitter antenna
wt_af_at1, dB_Ptx ,dB_cable_loss, dB_at1_G, dB_EIRP = Gain_ant_para_1(t, wQPSK_af_BPF)

print("Ptx: {}\nCable loss: {}\nGain_at1: {}\nEIRP: {}".format(dB_Ptx ,dB_cable_loss, dB_at1_G, dB_EIRP))

# rain loss
dB_Rainloss, wt_af_rl = rain_loss(wt_af_at1)

# Freespace loss
dB_Freespace, wt_af_freespace = freespace_loss(wt_af_rl)

print("Rainloss: {}\nFreespace loss: {}".format(dB_Rainloss, dB_Freespace))

# plt.show sau khi da ve xong
# sau khi dong cac cua so figure, cac doi tuong fig1, fig2,... cung bi xoa
plt.show()         # in ra do thi