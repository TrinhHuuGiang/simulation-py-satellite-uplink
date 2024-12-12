'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

import a1_global_specific_data as gd
'''*************************************************************
* code
*************************************************************'''
def raised_cos_filter(t, sI_reshape, sQ_reshape):
    '''
    Mo phong bo loc cos nang
    - gioi han mo phong dap ung xung trong 3 chu ky symbol
    '''

    # Truc thoi gian cho dap ung xung bo loc
    right_sinc = t[:gd.num_rcos_order * gd.N_sample_1sb]

    rc_time_h_t = np.concatenate([-right_sinc[::-1], right_sinc[1:]])

    # tinh dap ung xung h(t)
    rc_h_t = (np.sinc(rc_time_h_t / gd.T_sb) * np.cos(gd.rc_a * np.pi * rc_time_h_t / gd.T_sb))/ \
            (1 - 4 * (gd.rc_a**2) * (rc_time_h_t**2) / (gd.T_sb**2))

    # Tich chap de co duoc tin hieu raised cosin
    # chia cho n mau de chuan hoa gia tri sau chap
    rc_sI = convolve(sI_reshape, rc_h_t, mode='same') / gd.N_sample_1sb
    rc_sQ = convolve(sQ_reshape, rc_h_t, mode='same') / gd.N_sample_1sb

    return rc_time_h_t, rc_h_t, rc_sI, rc_sQ


def plot_ht_raise_cosine_filter(t, rc_time_h_t, rc_h_t):
    '''
    Plot dap ung xung bo loc cos nang
    '''
    # chon do thi
    plt.figure(gd.fig1)

    # plot dap ung xung bo loc
    plt.subplot(3,2,2) # 3 hang 2 cot, vi tri 2
    plt.title("h(t) r-cos filter - Tsb = {:.4} s".format(gd.T_sb))
    plt.plot(rc_time_h_t, rc_h_t)
    
    # them cac vach chia chu ky
    x_positions = [] # tao list lưu vi tri can ve
    for i in range(gd.num_rcos_order):
        x_positions.append(t[i*gd.N_sample_1sb])

    x_positions = np.array(x_positions) # chuyen list thanh array
    x_positions = np.concatenate([-x_positions[::-1],x_positions[1:]])

    for x_pos in x_positions:
        plt.axvline(x_pos, color='r', linestyle='--', alpha = 0.2)
    
    # danh dau lai truc hoanh
    plt.xticks(x_positions)

    # ve truc hoanh
    plt.axhline(0, color='black',linewidth = 0.2)

    # can chinh lai do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

def plot_symbol_rc_filted(t, rc_sI, rc_sQ):
    '''
    Plot symbol after raised cosine filter
    '''
    # chon do thi
    plt.figure(gd.fig1)
    
    # so mau can mo phong
    num_sample = gd.N_sample_1sb*gd.num_mod_symbol

    # [plot rc_sI]
    plt.subplot(3,2,4) # 3 hang 2 cot, vi tri 4
    plt.plot(t[:num_sample], rc_sI[:num_sample])
    
    # them cac vach chia symbol
    for i in range(gd.num_mod_symbol):
        plt.axvline(t[i*gd.N_sample_1sb], color='r', linestyle='--', alpha = 0.2)
    
    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # ve truc hoanh
    plt.axhline(0, color='black',linewidth = 0.2)

    # [plot rc_sQ]
    plt.subplot(3,2,6) # 3 hang 2 cot, vi tri 6
    plt.plot(t[:num_sample], rc_sQ[:num_sample])
    
    # them cac vach chia symbol
    for i in range(gd.num_mod_symbol):
        plt.axvline(t[i*gd.N_sample_1sb], color='r', linestyle='--', alpha = 0.2)
    
    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # ve truc hoanh
    plt.axhline(0, color='black',linewidth = 0.2)
