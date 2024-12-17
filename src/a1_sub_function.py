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

'''
The library updates missing values 'None' before using global data
- (*) call recalculate_when_shift_value() - when change default value simulate (cw_fc, Ptx(Arms), rif_K)
- then call function 'sequence_calculate()' when to calculate None value essential
'''

'''*************************************************************
* Lib
*************************************************************'''
import numpy as np
import a1_global_specific_data as gd

'''*************************************************************
* code 
*************************************************************'''
def recalculate_when_shift_value(order):
    '''
    order: 1- shift f, 2- shift Ptx (Arms), 3- shift rif_K
    '''
    if(order == 1):
        # shift f
        gd.cw_fs = gd.cw_f*gd.cw_sample
        gd.cw_Ts = 1/gd.cw_fs # cw_fs depend cw_fs
        gd.at1_l = (3*10**8)/gd.cw_f
        gd.at2_l = (3*10**8)/gd.cw_f
    if(order == 2):
        # shift cw_Arms
        # thay doi Ptx
        pass


def calculate_bit_rate_and_Bandreal():
    '''
    - cw_Bandreal
    - div_fc_Rs
    - R_sb, R_bit
    - N_sample_1sb
    '''
    # tinh div_fc_Rs va R_sb
    gd.div_fc_Rs = 1

    # div_fc_Rs = cw_f/R_sb == thuoc N*
    # Bandwidth = (1+rc_a)*R_sb <= cw_Bandmax
    # Lua chon R_sb thuoc N* cho de tinh

    gd.R_sb = gd.cw_f/gd.div_fc_Rs
    while (1+gd.rc_a)*gd.R_sb > gd.cw_Bandmax:
        gd.div_fc_Rs+=1
        gd.R_sb = gd.cw_f/gd.div_fc_Rs
    
    # tinh bandwidth real
    gd.cw_Bandreal = (1+gd.rc_a)*gd.R_sb

    # tinh do rong xung symbol T_sb
    gd.T_sb = 1/gd.R_sb

    # tinh so lan lay mau 1 symbol
    gd.N_sample_1sb = gd.cw_sample*gd.div_fc_Rs

    # tinh R_bit, T_sb
    gd.R_bit = gd.R_sb*np.log2(gd.cw_M)
    
def calculate_f_nyquist():
    '''
    f_nyquist for raised cosine filter
    '''
    # fnq = 1/(2.chu ky 1 symbol) = R_sb/2
    gd.rc_fnq = gd.R_sb/2

def calculate_Antenna_trans_gain():
    '''
    Gain of transmitter atenna
    '''
    min_fc=12*10**9
    gd.at1_l = (3*10**8)/(min_fc)

    # gain (lan cong suat)
    gd.at1_G = gd.at1_n*(np.pi * gd.at1_D / gd.at1_l)**2

def calculate_rain_tolerance_distance():
    '''
    Tinh cu ly chiu mua
    '''
    gd.rl_Dr = (gd.rl_hr-gd.rl_ha)/np.sin(gd.rl_e*np.pi/180)

def calculate_Antenna_receive_gain():
    '''
    Gain of receive atenna
    '''
    min_fc=12*10**9
    gd.at2_l = (3*10**8)/(min_fc)

    # gain (lan cong suat)
    gd.at2_G = gd.at2_n*(np.pi * gd.at2_D / gd.at2_l)**2

    # limtit
    

def sequence_calculate():
    calculate_bit_rate_and_Bandreal()
    calculate_f_nyquist()
    calculate_Antenna_trans_gain()
    calculate_rain_tolerance_distance()
    calculate_Antenna_receive_gain()

    # Log essential data
    # print("Bandwidth: {:.3f} Hz\nDiv(fc/Rsb): {} lan\nSymbol rate: {:.3} bps\tBitrate: {:.3} bps\tSymbol div: {} lan\nFnyquist: {} Hz\nGain ant tx: {:.3} lan\ndo cao chiu mua: {:.3} km".format(
    #     gd.cw_Bandreal,
    #     gd.div_fc_Rs,
    #     gd.R_sb,
    #     gd.R_bit,
    #     gd.N_sample_1sb,
    #     gd.rc_fnq,
    #     gd.at1_G,
    #     gd.rl_Dr))
    # print("Gain ant rx: {:.3} lan".format(gd.at2_G))