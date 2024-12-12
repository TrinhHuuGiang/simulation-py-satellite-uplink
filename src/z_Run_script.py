'''*************************************************************
* Lib
*************************************************************'''
import matplotlib.pyplot as plt

from a1_sub_function import sequence_calculate
from b1_GenBit_PNRZ_IQsplit import RandBit_PNRZ_IQsplit, plot_Bit_and_Symbol
from b2_Time_division import time_and_signal_div
from b3_Raised_cosine_filter import raised_cos_filter, plot_ht_raise_cosine_filter, plot_symbol_rc_filted
'''*************************************************************
* Code
*************************************************************'''
# calculate global variable
sequence_calculate()

# generate data stream
bitstream, Istream, Qstream = RandBit_PNRZ_IQsplit()

plot_Bit_and_Symbol(bitstream, Istream, Qstream)

# time div axis
t, sI_reshape, sQ_reshape = time_and_signal_div(Istream,Qstream)

# raise cosine filt
rc_time_h_t, rc_h_t, rc_sI, rc_sQ = raised_cos_filter(t, sI_reshape, sQ_reshape)

plot_ht_raise_cosine_filter(t, rc_time_h_t, rc_h_t)

plot_symbol_rc_filted(t, rc_sI, rc_sQ)





# plt.show sau khi da ve xong
# sau khi dong cac cua so figure, cac doi tuong fig1, fig2,... cung bi xoa
plt.show()         # in ra do thi