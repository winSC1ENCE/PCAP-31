from sys import path

path.append('/home/win/src/PCAP-31/chp1_module/modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

#%%
