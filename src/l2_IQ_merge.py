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
def Merge_bit_streams(I_bitstream_af_sample, Q_bitstream_af_sample):
    '''
    Merge bit stream I with Q
    '''

    recover_stream_bit = np.ravel([I_bitstream_af_sample, Q_bitstream_af_sample],order='F')

    return recover_stream_bit

def BER(streambit ,recover_stream_bit):
    # tim bit loi
    bit_errors = np.sum(streambit != recover_stream_bit)

    # tinh BER
    total_bits = len(streambit)
    bit_err_rate = bit_errors*100 / total_bits

    return bit_err_rate