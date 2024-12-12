'''
Muc tieu:
- Xay dung kenh truyen uplink cho he thong thong tin ve tinh dia tinh GEO
Thong so tu chon:
- Bang thong toi da: 50Mhz
- Cong suat phat mong muon: 5W
- Tan so song mang mo phong: 14 - 14.5Ghz

Tham khao:
- Tan so uplink:
https://en.wikipedia.org/wiki/Ku_band
- Bang thong:
DVB-S2 Technical Presentation
https://www.advantechwireless.com/wp-content/uploads/DVB-S2-theory.pdf
'''

'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt  # plot 2d, 3d
import numpy as np               # mang, ham toan hoc
'''*************************************************************
* global specific
*************************************************************'''
# Cac bieu do
fig1 = plt.figure()
fig2 = plt.figure()
# global fig3
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x,y)

# plt.show()

# so luong can mo phong
num_src_bit = 20        # Mo phong mot so lan bi nguon
num_src_symbol = 10     # Mo phong mot so lan ky tu (tin hieu I|Q) ma hoa PNRZ
                                # 1 symbol QPSK = log2(4) = 2 bit
                                # 1 bit for I (In-phase) , 1 bit for Q (Quadrature)
                                # Mo phong mot so lan tin hieu I|Q da qua cos nang
num_rcos_order = 3      # Mo phong mot so lan chu ky symbol cua dap ung xung h(t) bo loc
num_mod_symbol = 10     # Mo phong so chu ky song da qua dieu che QPSK
                                # tuong duong mot so lan ky tu


# Dieu che song
cw_f = 14*10**9          # (var) Tan so song mang (14Ghz cho uplink GEO)
                                # thay doi theo bang Ku uplink: 14 - 14.5 Ghz
cw_Arms = 1             # (const)  Arms, bien do song mang root mean square, lay dai dien 1V cho de tinh toan
cw_sample = 2*10        # (const)  Lay mau tin hieu song mang, >> chuan Nyquist (*2)
cw_fs = cw_f*cw_sample  # (depend) Tan so lay mau cho song mang 
cw_Ts = 1/cw_fs         # (depend) Chu ky lay mau cho song mang
cw_M = 4                # (const)  M la so trang thai M-PSK
                                # M=4, phi0 = pi/4 ->QPSK
cw_Bandmax = 50*10**6    # (Tham khao tai lieu) Bang thong toi da (Max Bandwidth) - 50Mhz
cw_Bandreal = None      # (depend) tinh toan thong qua cong thuc R_sb*(1+rc_a)

# Tin hieu
N_bit = 100             # (random) So luong bit can mo phong, random du nhieu (lon qua bi crash)
N_sb = N_bit/np.log2(cw_M)  # (random) So luong symbol de dieu che = N_bit/log2(cw_M)
div_fc_Rs = None        # ty le cw_f/R_sb thuoc N*
R_sb = None             # (depend) Toc do truyen ky tu (toc do cac dong I|Q trong Qpsk)
T_sb = None             # (depend) Do rong ky tu = 1/R_sb
N_sample_1sb = None     # (depend) So lan lay mau 1 symbol
R_bit = None            # (depend) Toc do truyen bit = R_sb*log2(cw_M)


# Raise cosine
rc_fnq = None           # (depend) Tan so Nyquist yeu cau cho thiet ke bo loc
                                # fnq = 1/(2.chu ky 1 ky tu) = R_sb/2
rc_a = 0.66             # (tu chon) He so cat 0< a < 1
                                # a->1: giam ISI, tang pho tan
                                # a->0: tang ISI, giam pho tan


# Power Amplifier
pa_a1 = 5/(cw_Arms**2)  # (var) Cac he so khuech dai
pa_a2 = pa_a1/10        # cua bo PA bi phi tuyen
pa_a3 = pa_a1/100       # (Tham khao bai tap) Ptx = 5W -> pa_a1*Arms^2 = Ptx
                                # pa_a1~5 lan, chon pa_a2 = 1/10pa_a1, pa_a3 = 1/100pa_a1

# FIR BPF
bpf_order = 50          # (tu chon) Bac cua bo loc FIR tuyen tinh

# Anten phat
at1_n = 0.6             # (Tham khao bai tap) do hieu qua (0.5 -0.8)
at1_D = 3               # (Tham khao bai tap) duong kinh anten (m)
at1_l = (3*10**8)/cw_f  # (Tham khao bai tap) buoc song - wavelength (m)
at1_G = None            # (depend) cong thuc antenna Gain

#  rain loss
rl_a = 3                # (Tham khao bai tap) he so suy hao do mua (3dB/Km - vietnam)
rl_hr = 5               # (Tham khao bai tap) do cao chiu mua - km
rl_ha = 0.1             # (Tham khao bai tap) do cao anten vs nuoc bien - km
rl_e = 55               # (Tham khao bai tap) goc ngang anten - do
rl_Dr = None            # (depend) cu li chiu mua - km

#  path loss
pl_d = 35786            # (const) khoang cach tram phat - ve tinh - Km


# System_margin

# Rician fading

# Thermal noise dau vao may thu
thn_T = None            # (random) Bien ngau nhien nhieu nhiet - K
thn_k = 1.38*10**(-23)  # (const) hang so boltzman
