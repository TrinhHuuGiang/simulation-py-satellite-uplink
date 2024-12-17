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
def Comparator_signal(I_signal_LPF, Q_signal_LPF):
    '''
    The comparator detects the level of the signal by the voltage across the 0 V threshold
    '''
    # delay 1 khoang thoi gian 1/2 xung de lay mau
    # lay mau tin hieu sao 1 khoang thoi gian bang so mau cho 1 tin hieu
    delay_sample = gd.N_sample_1sb//2

    # lay mau va so sanh voi mau lay duoc
    I_bitstream_af_sample = [1 if level > 0 else 0 for level in I_signal_LPF[delay_sample::gd.N_sample_1sb]]
    Q_bitstream_af_sample = [1 if level > 0 else 0 for level in Q_signal_LPF[delay_sample::gd.N_sample_1sb]]

    return I_bitstream_af_sample, Q_bitstream_af_sample
