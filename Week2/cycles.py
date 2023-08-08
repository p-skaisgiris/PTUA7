# Kam naudojami ciklai?
# 1. Kodo kartojimas
# 2. Iteracija per masyvus / duomenų struktūras

# Paprastas for ciklas (iteracija per elementus)

"""
Šablonas

for <kintamasis> in <iterable kintamasis>:
    <kodas>
"""


lst = [1, 2, 3, 4, 5]
for a in lst:
    print(a + 2)

# Sumuojame listo elementus naudojant for ciklą

lst = [1, 2, 3, 4, 5]
suma = 0
for i in lst:
    suma += i
print(suma)

lst = [1, 2, 3, 4, 5]
factorial = 0
for i in lst:
    suma *= i
print(factorial)

string_list = ["a", "b", "c", "d", "e"]
concatenated_string = ""
for single_string in string_list:
    concatenated_string += single_string

# Sukame for ciklą tam tikrą kiekį kartų (su range)

for i in range(10):
    print(i + 2)

# Enumerate su for ciklu

raides = ["a", "b", "c", "d", "e", "f"]
# Lygiai toks pat kaip enumerate(raides)
raidziu_tuplas = [(0, "a"), (1, "b"), (2, "c"), (3, "a"), (4, "b"), (5, "c")]

for indeksas, reiksme in enumerate(raides):
    print(f"{reiksme} yra {indeksas + 1}-a raidė")

# Enumerate su dviem listais ir indekso panaudojimas kitam listui

vardai = ["Jonas", "Petras", "Herbertas", "Stasys", "Egle", "Igne"]

for indeksas, raide in enumerate(raides):
    print(f"{raide} yra {vardai[indeksas]} raidė")

# Zip, vietoje enumerate + indeksai

for raide, vardas in zip(raides, vardai):
    print(f"{raide} yraa {vardas} raidė")


# For ciklas for cikle (nested for loop)

for i in range(10):
    print("startas")

    for j in range(10):
        print(f"i = {i}, j = {j}")

    print("pabaiga")

# Paprastas while ciklas

"""
Šablonas

while <condition>:
    <code>
    
if <condition> is satisfied,
then run the <code> block,
if <condition> is satisfied,
then run the <code> block,
...
"""

i = 0
while i < 5:
    i += 1

# For loop alternative
for i in range(5):
    print(i)


# While ciklas while cikle

i = 0
while i < 5:
    j = 0
    print("startas")

    while j < 5:
        print(f"i = {i}, j = {j}")
        j += 1

    print("pabaiga")
    i += 1

# For ciklo alternatyva
for i in range(5):
    for j in range(5):
        print(f"i = {i}, j = {j}")

# Ciklo nutraukimas (break)

# Simple for
for i in range(1, 100):
    print(i)
    if i % 7 == 0:
        # For some reason, cancel the loop prematurely
        break

# Nested for
for i in range(5):
    for j in range(5):
        print(f"i = {i}, j = {j}")

    if i == 2:
        break
    print("asd")


print("********************************")

# Nested while
i = 0
while i < 5:
    j = 0
    print("startas")

    while j < 5:
        print(f"i = {i}, j = {j}")

        j += 1

    if i == 2:
        break

    print("pabaiga")
    i += 1

# Begalinis while ciklas (infinite loop)

# Examples of infinite cycles
# while True:
#     print("hello")
#
# while 1 == 1:
#     print("helo")
#
# i = 0
# while i < 5:
#     print("asd")

# Infinite loop until the input is x
# while True:
#     ivestis = input("iveskite kazka")
#     print("jusu ivestis yra", ivestis)
#     if ivestis == "x":
#         break

# remaining_attempts = 3
# while remaining_attempts > 0:
#     password = input("Input your password\n")
#     if password == "12345":
#         print("Logged in")
#         break
#     else:
#         remaining_attempts -= 1
#         print(f"Try again. You have {remaining_attempts} left")
#         if remaining_attempts == 0:
#             print("You are blocked :(")

# Pakartojimo praleidimas (continue)

for i in range(10):
    if i == 5:
        print("found 5, skipping")
        continue

    print(i)

print("**************************")
i = 0
while i < 5:
    i += 1

    if i == 2:
        print("found 2, skipping")
        continue

    print(i)


# Sąlyga [else] for cikle



# Sąlyga [else] for cikle 2


