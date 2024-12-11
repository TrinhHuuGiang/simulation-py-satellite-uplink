# Cac bieu do
global fig1
# global fig2
# global fig3


# so luong can mo phong
global num_src_bit              # Mo phong mot so lan bi nguon
global num_src_symbol           # Mo phong mot so lan ky tu (tin hieu I|Q) ma hoa PNRZ
                                # 1 symbol QPSK = log2(4) = 2 bit
                                # 1 bit for I (In-phase) , 1 bit for Q (Quadrature)
                                # Mo phong mot so lan tin hieu I|Q da qua cos nang
global num_rcos_order           # Mo phong mot so lan chu ky symbol
global num_mod_symbol           # Mo phong mot so lan chu ky song da qua dieu che QPSK

# Dieu che
global cw_f                     # (const) Tan so song mang (14Ghz cho uplink GEO)
global cw_Arms                  # (const) Arms, bien do song mang root mean square
global cw_sample                # (const) Lay mau tin hieu song mang, >> chuan Nyquist
global cw_M                     # (const) M la so trang thai M-PSK
                                # M=4, phi0 = pi/4 ->QPSK

# Tin hieu
global N_bit                    # (random) So luong bit can mo phong, random du nhieu
global N_sb                     # (random)So luong symbol de dieu che = N_bit/log2(cw_M)
global R_bit                    # (const) Toc do truyen bit = R_sb*log2(cw_M)
global R_sb                     # (const) Toc do truyen ky tu (toc do cac dong I|Q trong Qpsk)

# Raise cosine
global rc_fnq                   # (const) Tan so Nyquist yeu cau cho thiet ke bo loc
                                # fnq = 1/(2.chu ky 1 ky tu) = R_sb/2
global rc_a                     # (const) He so cat 0< a < 1
                                # a->1: giam ISI, tang pho tan
                                # a->0: tang ISI, giam pho tan


# Power Amplifier
global pa_a1                    # Cac he so khuech dai
global pa_a2                    # cua bo PA bi phi tuyen
global pa_a3                    # 

# FIR BPF
global bpf_order                # (const) Bac cua bo loc FIR tuyen tinh

# Anten phat
global at1_n                    # (const) do hieu qua (0.5 -0.8)
global at1_D                    # (const) duong kinh anten (m)
global at1_l                    # (const) buoc song - wavelength (m)
global at1_G                    # (const) antenna Gain

#  rain loss
global rl_a;                    # (const) he so suy hao do mua
global rl_hr;                   # (const) do cao chiu mua
global rl_ha;                   # (const) do cao anten vs nuoc bien
global rl_e;                    # (const) goc ngang anten
global rl_Dr;                   # (const) cu li chiu mua

#  path loss
global pl_d;                    # (const) khoang cach tram phat - ve tinh 


# Thermal noise dau vao may thu
global thn_T;                   # (random) Bien ngau nhien nhieu nhiet - K
global thn_k;                   # (const) hang so boltzman

