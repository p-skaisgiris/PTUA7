# # importuojam / naudojam visa moduli
# import datetime
#
# # naudojam funkcijas / klases is modulio gan specifiskai per modulio pavadinima: datetime.<funkcija>
#
# datetime.datetime.now()
#
# import math
#
# math.pow(5, 6)
# math.sqrt(2)
# math.fabs(-1.5)
#
#
# # sutrumpinam modulio pavadinima
# import datetime as dt
#
# dt.datetime.now()
#
# # is datetime modulio, importuojame datetime (klase)
# from datetime import datetime
# datetime.now()
#
# # from math import pow, sqrt, fabs
#
# pow(5, 6)
#
#
# import greitai
#
#
# def fabs(x):
#     print(x)
#
#
# math.fabs(123123)

#from helper_funcs.damage import deal_damage
from helper_funcs.moving import move_char
from main_loop.loop import TOTAL_LOOPS
import helper_funcs.damage

#deal_damage(123)
move_char("sonic", "north", "20")
helper_funcs.damage.deal_damage(123)


