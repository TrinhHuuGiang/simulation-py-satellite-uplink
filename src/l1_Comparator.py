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
def Comparator_signal(I_signal_LPF, Q_signal_LPF):
    '''
    The comparator detects the level of the signal by the voltage across the 0 V threshold
    '''
    # delay 1 khoang thoi gian 1/2 xung de lay mau
    # lay mau tin hieu sao 1 khoang thoi gian bang so mau cho 1 tin hieu
    delay_sample = gd.N_sample_1sb//2

    # boi vi tin hieu bi dao pha qua 2 bo loc, nen bit thu duoc bi dao
    I_bitstream_af_sample = [0 if level > 0 else 1 for level in I_signal_LPF[delay_sample::gd.N_sample_1sb]]
    Q_bitstream_af_sample = [0 if level > 0 else 1 for level in Q_signal_LPF[delay_sample::gd.N_sample_1sb]]

    return I_bitstream_af_sample, Q_bitstream_af_sample
