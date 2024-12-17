# Satellite Uplink Simulation Program
# Copyright (C) 2024 SatComm 11

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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