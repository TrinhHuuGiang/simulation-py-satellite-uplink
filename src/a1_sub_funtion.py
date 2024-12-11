'''
The library updates missing values 'None' before using global data
- only call function 'sequence_calculate()' 1 time
'''

'''*************************************************************
* Lib
*************************************************************'''
import numpy as np
import a1_global_specific_data

'''*************************************************************
* code 
*************************************************************'''
def calculate_bit_rate_and_Bandreal():
    '''
    - cw_Bandreal
    - div_fc_Rs
    - R_sb, R_bit
    '''
    # tinh div_fc_Rs va R_sb
    div_fc_Rs = 1

    # div_fc_Rs = cw_f/R_sb == thuoc N*
    # Bandwidth = (1+rc_a)*R_sb <= cw_Bandmax

    R_sb = cw_f/div_fc_Rs
    while (1+rc_a)*R_sb > cw_Bandmax:
        div_fc_Rs+=1
        R_sb = cw_f/div_fc_Rs
    
    # tinh bandwidth real
    cw_Bandreal = (1+rc_a)*R_sb

    # tinh R_bit
    R_bit = R_sb*np.log2(cw_M)

    
def calculate_f_nyquist():
    '''
    f_nyquist for raised cosine filter
    '''
    # fnq = 1/(2.chu ky 1 symbol) = R_sb/2
    rc_fnq = R_sb/2

def calculate_Antenna_trans_gain():
    '''
    Gain of transmitter atenna
    '''
    # gain
    at1_G = at1_n*(np.pi * at1_D / at1_l)**2

def calculate_rain_tolerance_distance():
    '''
    Tinh cu ly chiu mua
    '''
    rl_Dr = (rl_hr-rl_ha)/np.sin(rl_e*np.pi/180)

def sequence_calculate():
    calculate_bit_rate_and_Bandreal()
    calculate_f_nyquist()
    calculate_Antenna_trans_gain()
    calculate_rain_tolerance_distance()