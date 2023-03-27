from sys import path
# path.append('/home/win/src/PCAP-31/chapter_1/packages')

# step 5-7
# import extra.iota
# print(extra.iota.funI())
# import extra.good.best.sigma
# from extra.good.best.tau import funT
#
# print(extra.good.best.sigma.funS())
# print(funT())

## step 8
# from extra.iota import funI
# print(funI())
#
#
# import extra.good.best.sigma as sig
# import extra.good.alpha as alp
#
# print(sig.FunS())
# print(alp.FunA())

from sys import path

path.append('/home/win/src/PCAP-31/chapter_1/packages/extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())


#%%
