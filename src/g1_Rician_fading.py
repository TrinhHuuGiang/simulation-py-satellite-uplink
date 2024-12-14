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
def rician_fading(dB_EIRP, dB_Rainloss, dB_Freespace, wt_af_freespace):
    '''
    Ap dung rician fading  cho tin hieu
    Kenh truyen co LOS
    - Truoc tien tinh toan lai cong suat anten thu co the nhan
    - Sau do mo phong tin hieu co fading
    '''
    # cong suat truyen sau suy hao tu do
    # bao gom ca cong suat tin hieu va cong suat fading
    dB_total_fading = dB_EIRP - dB_Rainloss - dB_Freespace

    Ptotal = 10**(dB_total_fading/10)
    '''
    Ptotal = PLOS+PNLOS  = PLOS*(1+1/K) = PNLOS*(1+K)
    -> PLOS = ( K/(K+1) ) *  Ptotal
    -> PNLOS = ( 1/(K+1) )  *   Ptotal
    '''

    # [Rician fading]
    # tinh phuong sai K= A^2/2*o^2 -> o^2
    # Lai co: A^2 ~ Plos, 2*o^2 ~ Plos (tong cong suat hieu thanh phan I, Q)
    # -> K = K*Ptotal/( (K+1)*2*o^2 )
    # -> Ptotal/( (K+1)*2 ) = o^2
    gd.rif_var = Ptotal / (2*(gd.rif_K + 1))
    
    # Tin hieu LOS
    # Ptotal / PLOS = (K+1)/K -> Atotal / ALOS = sqrt( K+1/(K))
    
    wt_LOS = wt_af_freespace*np.sqrt(gd.rif_K/(gd.rif_K+1))

    # sinh các bien ngau nhien Gaussian tu cac thanh phan I va Q
    total_sample = len(wt_LOS)
    # Tạo 2 mảng ngẫu nhiên có độ dài bằng len(wt_LOS)
    X1 = np.random.normal(0, 1, total_sample)  # Mảng ngẫu nhiên X1
    X2 = np.random.normal(0, 1, total_sample)  # Mảng ngẫu nhiên X2
    
    # LOS chiu fading
    wt_NLOS = np.sqrt(2*gd.rif_var) * (X1 + X2) # ly thuyet (X1 + jX2), cong luon X2 vi tin hieu QPSK ta tong 2 pha luon roi
    wt_af_fading = wt_LOS + wt_NLOS

    return dB_total_fading, wt_af_fading

def plot_rician_fading(t, wt_af_fading):
    '''
    Plot rician fading wave
    '''
    # chon do thi
    plt.figure(gd.fig3)

    # so mau can mo phong
    num_sample = gd.num_rician_symbol*gd.cw_sample

    # [plot wQPSK_af_BPF]
    plt.subplot(3,2,1) # 3 hang 2 cot, vi tri 1
    plt.title("Rician fading| {} wave first".format(gd.num_rician_symbol))
    plt.plot(t[:num_sample], wt_af_fading[:num_sample])
    plt.xlabel("(s)")
    plt.ylabel("(Volt)")

    # danh dau lai truc hoanh
    plt.xticks(t[:num_sample:gd.N_sample_1sb])

    # grid
    plt.grid()

    # can chinh lai cac do thi
    plt.tight_layout() # tu dong can lai khoang cach cac do thi

