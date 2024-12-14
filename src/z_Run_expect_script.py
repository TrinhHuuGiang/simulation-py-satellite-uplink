'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt

from a1_global_specific_data import N_bit
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
from g1_Rician_fading import rician_fading, plot_rician_fading
from g2_Thermal_noise import thermal_noise, plot_wave_after_thermal_noise
from h1_Receiver_antenna import Gain_ant_para_2, plot_wave_af_receiver_ant2_cable_loss
from i1_LNA import Low_Noise_Amplifier, plot_LNA_wave
from j1_QPSK_Demodulation import QPSK_Dedulator
from k1_LPF import FIR_LPF, plot_DemodQPSK_LPF
from l1_Comparator import Comparator_signal
from l2_IQ_merge import Merge_bit_streams, BER
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

# rain loss
dB_Rainloss, wt_af_rl = rain_loss(wt_af_at1)

# Freespace loss
dB_Freespace, wt_af_freespace = freespace_loss(wt_af_rl)

# Rician fading
dB_total_fading, wt_af_fading = rician_fading(dB_EIRP, dB_Rainloss, dB_Freespace, wt_af_freespace)

plot_rician_fading(t, wt_af_fading)


# Thermal noise [bo sung sau]
wt_af_thermal, dB_total_receive , dB_C_N = thermal_noise(wt_af_fading)

plot_wave_after_thermal_noise(t, wt_af_thermal, dB_C_N)

# Receiver antenna (tam thoi dung after fading)
wt_af_at2, dB_Prx , dB_at2_G, dB_rx_cable = Gain_ant_para_2(dB_total_receive, wt_af_thermal)

plot_wave_af_receiver_ant2_cable_loss(t, wt_af_at2)

# LNA
wt_af_LNA = Low_Noise_Amplifier(wt_af_at2)

plot_LNA_wave(t, wt_af_LNA)

# QPSK Demodulator
wI_DEM, wQ_DEM = QPSK_Dedulator(t, wt_af_LNA)

# LPF
I_signal_LPF, Q_signal_LPF = FIR_LPF(wI_DEM, wQ_DEM)

plot_DemodQPSK_LPF(t,I_signal_LPF, Q_signal_LPF)

# Comparator
I_bitstream_af_sample, Q_bitstream_af_sample = Comparator_signal(I_signal_LPF, Q_signal_LPF)

# merge
recover_stream_bit = Merge_bit_streams(I_bitstream_af_sample, Q_bitstream_af_sample)

bit_err_rate = BER(bitstream, recover_stream_bit)


# print
print("Ptx: {:.5}dB\nCable loss: {:.5}dB\nGain_at1: {:.5}dB\nEIRP: {:.5}dB".format(dB_Ptx ,dB_cable_loss, dB_at1_G, dB_EIRP))
print("-"*20)
print("Rainloss: {:.5}dB\nFreespace loss: {:.5}dB".format(dB_Rainloss, dB_Freespace))
print("Pwave after fading: {:.5}dB".format(dB_total_fading))
print("Pwave after thermal: {:.5}dB".format(dB_total_receive))

print("-"*20)
print("At2_gain: {:.5}dB\tRX Cable: {:.5}dB".format(dB_at2_G,dB_rx_cable))
print("Prx_after_gain_loss: {:.5}dB".format(dB_Prx))
print("Prx_after_gain_loss: {:.5}W".format(10**(dB_Prx/10)))

print("-"*20)
print("Total expect bits: {}".format(N_bit))
print("I received   bits: {}".format(len(I_bitstream_af_sample)))
print("Q received   bits: {}".format(len(Q_bitstream_af_sample)))

print("-"*20)
print("2 bit stream matched" if (bitstream == recover_stream_bit).all() else "does not match") 
print("Rand bit: {}".format(bitstream[:10]))
print("Recv bit: {}".format(recover_stream_bit[:10]))
print("BER: {}%".format(bit_err_rate))

# plt.show sau khi da ve xong
# sau khi dong cac cua so figure, cac doi tuong fig1, fig2,... cung bi xoa
plt.show()         # in ra do thi