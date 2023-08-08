import time
import datetime

ivestis = ""

while type(ivestis) != int:
    try:
        ivestis = input("iveskite skaiciu\n")
        ivestis = int(ivestis)
    except ValueError:
        print("ivestis nera skaicius, bandykite dar karta")

print(ivestis)