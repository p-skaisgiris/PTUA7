# Užmigdo pythoną trims sekundėmis
# import time
# time.sleep(3)

# datetime biblioteka ir jos panaudojimas
# Importuodami gausime naudoti funkcijas iš šios bibliotekos
import datetime

# datetime.today() Dabartinė data ir laikas
# rodo dabartinės kompo laiko zonos laiką

now = datetime.datetime.now()
print(now)

# date.today() - tik data

today = datetime.date.today()
print(today)

# datetime.today().time() - tik laikas

data_today = datetime.date.today()
# ERROR, nes laikas neegzistuoja datoje (naudojom .date, o ne datetime)
# data_today.time()

# Save/Freeze today's time AND date
datetime_today = datetime.datetime.today()
print(datetime_today)
# Calling .date() means we just the date property of our variable datetime_today
print(datetime_today.date())
# Calling .time() means we just check the time property of our variable datetime_today
print(datetime_today.time())

# The two below are equivalent
datetime_today = datetime_today.today()
datetime_today = datetime.datetime.today()
datetime_today = datetime.datetime.now()

# Ištraukimas: metai, mėnesis, valandos, minutės, sekundės, mikrosekundės
# Retrieve properties of year, month, hour, etc

print("---- Datetime properties -----")
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# strftime() - datos formatavimas

print("-----Datos formatavimas-----")
now = datetime.datetime.now()
# Weekday full name, day, month

formatuotas_laikas = now.strftime("%A, %d %B")  # Gaunam stringą
print(type(formatuotas_laikas))
print(formatuotas_laikas)
print(now.strftime("%Y-%m-%d %H:%M"))

# Datetime objekto sukūrimas

print("Datetime objekto sukūrimas")
kazkokia_data = datetime.datetime(year=2021, month=2, day=12, hour=8, minute=2)
print(kazkokia_data)

# Aritmetika su laiku

now = datetime.datetime.now()
print(now - kazkokia_data)
print(kazkokia_data - now)

# ERROR: year and month arguments unfilled
# penkiu_dienu_skirtumas = datetime.datetime(day=5)

# TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'datetime.datetime'
# print(now + kazkokia_data)

# timedelta objekto sukūrimas ir panaudojimas skirtumuose
# naudojamas, nes datetime+datetime neleidžiamas
# timedelta yra nurodomas laiko skirtumas

print("timedelta")
penkiu_dienu_skirtumas = datetime.timedelta(days=5, hours=6)
print(now)
print(now + penkiu_dienu_skirtumas)
print(now - penkiu_dienu_skirtumas)

# strptime, Laiko įvedimas per input ir skirtumo apskaičiavimas

print("Datos ir laiko įvedimas")
ivesta = input("Iveskite datą ir laiką\n")

# Pirmas argumentas - kazkoks stringas parasytas tam tikru formatu,
#                     ivestis turi PILNAI atitikti nurodyta formatą
# Antras argumentas - tas stringo formatas nurodytas strftime kodais
data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %H:%M:%S")  # Gaunam datetime.datetime objektą

print(data)
print(data - penkiu_dienu_skirtumas)
print(data + penkiu_dienu_skirtumas)
print(data - kazkokia_data)

# Klaidos / išimtys ir jų suvaldymas

dalinys = 7
daliklis = 0
if daliklis == 0:
    print("Daliklis yra lygus 0, dalyba negalima")
else:
    print(dalinys / daliklis)

# try/except, automatiškai išmesti errorai yra pagaunami ir mus nuveda į except kodo bloką,
# kuriame galime informuoti naudotoją apie nepavykimą
# try blok'e rašome kodą, kuris potencialiai iškeltų išimtį / klaidą / exception
# except blok'e rašome žinutę naudotojui arba aprašome default elgseną

try:
    print(dalinys / daliklis)
except ZeroDivisionError:
    print("Daliklis yra lygus 0, dalyba su 0 negalima, daliname iš 2")
    print(dalinys / 2)

# except Exception as e
# išsaugojame išimties kintamąjį, kurio pavadinimas yra e. Tai dažnai daroma norint išprintinti
# vartotojui, kokia yra specifinė problema
# Exception yra pati plačiausia išimties klasė Pythone, bandyti nenaudoti
# ir pagauti specifinius errorus

while True:
    skaicius = input("Iveskite skaiciu\n")
    try:
        skaicius = int(skaicius)
        print(skaicius)
        break
    except Exception as e:
        print(e)
        print("Neteisinga ivestis. Iveskite skaiciu dar karta")

# Try/multiple except - daugelio išimčių suvaldymas

# Jeigu turime ilgesni varianta:
# while True:
#     try:
#         dalinys = input("Iveskite dalini\n")
#         daliklis = input("Iveskite dalikli\n")
#         dalinys = int(dalinys)     # Potentially raises ValueError
#         daliklis = int(daliklis)   # Potentially raises ValueError
#         break
#     except ValueError:
#         print("Neteisinga ivestis. Iveskite skaicius dar karta")
#
# try:
#     print(dalinys / daliklis)  # Potentially raises ZeroDivisionError
# except ZeroDivisionError:
#     print("Daliklis yra lygus 0, dalyba su 0 negalima, daliname iš 2")
#     print(dalinys / 2)

# Galime jį perrašyti trumpiau

while True:
    try:
        dalinys = input("Iveskite dalini\n")
        daliklis = input("Iveskite dalikli\n")
        dalinys = int(dalinys)     # Potentially raises ValueError
        daliklis = int(daliklis)   # Potentially raises ValueError
        print(dalinys / daliklis)  # Potentially raises ZeroDivisionError
        break
    except ValueError:
        print("Neteisinga ivestis. Iveskite skaicius dar karta")
    except ZeroDivisionError:
        print("Daliklis yra lygus 0, dalyba su 0 negalima, daliname iš 2")
        print(dalinys / 2)
        break

# Jei specifiškas erroras nenurodytas except bloke, jis bus iškeliamas ir nepagautas

# while True:
#     try:
#         dalinys = input("Iveskite dalini\n")
#         daliklis = input("Iveskite dalikli\n")
#         dalinys = int(dalinys)     # Potentially raises ValueError
#         daliklis = int(daliklis)   # Potentially raises ValueError
#         raise TypeError
#         break
#     except ValueError:
#         print("Neteisinga ivestis. Iveskite skaicius dar karta")

# finally blokas - visada paleidžiamas po try/excpet

try:
    print(dalinys / daliklis)
except ZeroDivisionError:
    print("Daliklis yra lygus 0, dalyba su 0 negalima, daliname iš 2")
    print(dalinys / 2)
finally:
    print("po visko")

print("po visko 2")
