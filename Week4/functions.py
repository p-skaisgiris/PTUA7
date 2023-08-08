# Funkcijos. Kas jos yra? Kam jos naudingos?
# - Kodo grupavimas (jei darot tą patį veiksmą keliose vietose tik su skirtingais kintamaisiais)
# - Galima funkcijas, grupuotus veiksmus kartoti be copy-paste
# - Vietos sutaupymas
# - Logiškas funkcijų / kodo bloko išskirstymas, struktūrizacija
# - Funkcijų pervadinimas / apvilkimas (wrapping)

"""
Funkcijos sintaksė
def <funkcijos pavadinimas>(<argumentai>):
    return <suskaičiuota reikšmė>
"""

# --- Funkcijų pavyzdys

def pasisveikinti(vardas):
    print(f"Sveiki, {vardas}")

# --- Funkcija su argumentais

def nauja_tema(tema):
    print(f"----- {tema} -----")

# --- Funkcija be return

def tuscia_funkcija():
    print("Sveiki, nieko cia nera")

tuscia_funkcija()
res = tuscia_funkcija()
# res = None

def separator():
    print("*************************************")
    print("*************************************")
    print("*************************************\n")

# --- Funkcija su return

# f(x, y) = x^2 + y

def f(x, y):
    # Function scope means that
    # it only sees the arguments it was given
    # and local variables we have created
    # like result below
    result = x**2 + y
    print(result)
    return result

# 5^2 + 2 = 27
print(f(5, 2))
# 2^2 + 8 = 12
print(f(2, 8))
# 0^2 + 10 = 10
print(f(0, 10))

f_res = f(4, 2)
# f_res = 10

separator()


# --- Funkcija su tipais

# x: int ir y: str yra "argumentų tipai"
# -> float yra "funkcijos grąžinimo tipai"
# Šiuo atveju mes aprašėme, kad funckija tikisi argumento x sveiko skačiaus tipu,
# argumento y stringo tipu ir mūsų funkcija grąžins reikšmę, kuri bus float tipo
def kazkokia(x: int, y: str) -> float:
    # if not isinstance(x, int):
    if type(x) != int:
        raise ValueError("Ne toks x kintamojo tipas")

    if x == 1:
        return "vienas"
    elif x == 2:
        return 2
    elif x == 3:
        return 3.0
    else:
        return None


res = kazkokia(1, "asd")
print(type(res))

# --- Funkciju argumentu errorai

def printas(x):
    print(x)

# Viskas ok, nes funkcija tikisi vieno argumento
# ir mes kviečiame su vienu argumentu
printas(1)
# Keliamas erroras, nes bandome kviesti funkciją su dviem argumentais, nors
# funkcija tikisi vieno
# printas(1, 2)

def printas2(x, y, z):
    print(x, y)

# Viskas ok
# printas(1, 2)
# Keliamas erroras, nes funkcija tikisi dvieju argumentu, o mes duodam tik viena
# printas(1)

# --- Funkcija su nebūtinais argumentais (vienas iš trijų)

# Funkcijoje galime noryti "default" reikšmes tam tikriems argumentams

def printas(x, y, z=3):
    print(x, y, z)

separator()
printas(1, 2, 10)
# Tuo atveju, šių argumentų nebūtina nurodyti funkcijos kvietime
printas(3, 4)

# --- Funkcija su nebūtinais argumentais (visi trys)

def optional_args(x=1, y=2, z=3):
    return x + y + z

# Eiliškumas labai svarbus!
# Eilės tvarka šiuo atveju bus priskiriamos būtent mūsų nurodytos
# reikšmės atitinkamiems kintamiesiems funkcijoje
print(optional_args())       # x = 1, y = 2, z = 3
print(optional_args(3, 4))   # x = 3, y = 4, z = 3
print(optional_args(5))      # x = 5, y = 2, z = 3
print(optional_args(9, 10, 11))  # x = 9, y = 10, z = 11

# --- Funkcijos pakvietimas su specifinių argumentų priskyrimu

# Eilišumas nėra svarbus, galima prašokti pirmuosius kintamuosius
optional_args(x=2)  # x = 2, y = 2, z = 3
optional_args(2)    # x = 2, y = 2, z = 3

optional_args(y=10)  # x = 1, y = 10, z = 3
optional_args(x=8, z=9)  # x = 8, y = 2, z = 9
# ERROR: unexpected argument, funkcijoje nesame apsibrėžę argumento "asd"
# optional_args(x=8, z=9, asd=2)

# --- Funkcijos su neribotais argumentais (args)

numbers = [1, 2, 3, 4, 5]

separator()

def skaiciu_suma(skaiciai: list) -> float:
    suma = 0
    for i in skaiciai:
        suma += i
    return suma

print(skaiciu_suma(numbers))

# args leidžia dirbti su bet kiek kintamųjų, galima juos tiesiai duoti į funkciją
# args yra tuplas

def args_skaiciu_suma(a, b, *args) -> float:
    suma = 0
    for i in args:
        suma += i
    return suma

# skaiciu_suma([1,2,3])   # be args
# skaiciu_suma(1, 2, 3)   # su args

print(args_skaiciu_suma(1,2,3,4,5))  # a = 1, b = 2, args = (3,4,5)

# --- Funkcijos su neribotais argumentais (kwargs)

info_dict = {
    "name": "Paulius",
    "surname": "Skaisgiris",
    "ssn": 123123,
    "age": 123132
}


def print_info(info):
    print("naudotojo info:")
    print(f"Name Surname: {info['name']} {info['surname']}")
    print(f"SSN: {info['ssn']}")
    print(f"Age: {info['age']}")


def kwargs_info(a, b, **kwargs):
    # print("naudotojo info:")
    # print(f"Name Surname: {kwargs['name']} {kwargs['surname']}")
    # print(f"SSN: {kwargs['ssn']}")
    # print(f"Age: {kwargs['age']}")
    for key, value in kwargs.items():
        print(key, value)

# kwargs pakeičia argumentus į dictionary funkcijoje
# būtina pakviesti funkciją su keyword argumentais (per =)

separator()
print_info(info_dict)
kwargs_info(name="Paulius", ssn=123123, age=123123, a=1, b=2)

# --- Globalūs ir lokalūs kintamieji, jų panaudojimas funkcijose

# globalus ir dar_vienas kintamasieji matomas visame programos kontekse
# aprašomi programos pagrindiniame lygyje, be indentacijos
# globalūs kintamieji dažniausiai aprašomi didžiosiomis raidėmis
# apie juos paprasčiausia galvoti kaip konstantos
GLOBALUS = "global"
DAR_VIENAS = "labas"

def printas(a, b, c):
    d = 2
    # šiame kontekse a, b, c, d kintamieji yra vadinami "lokaliais"
    print(a, b, c)
    print(GLOBALUS)
    return d

SUO = printas(1,2,3)

def printas2():
    hello = printas(1, 2, 3)
    # hello yra lokalus kintamasis printas2 funkcijos kontekste
    print(SUO)


PI = 3.14159

def skritulio_perimetras(r):
    return 2 * PI * r


# --- Funkcijų komentavimas (docstrings)

# Trumpesnis, vienos eilutės aprašymas
def mokesciu_apskaiciavimas(pajamos: float, gpm: float = 0.15, psd: float = 58.5) -> float:
    """Lietuvos mokesčių apskaičiavimas pagal pajamas."""
    return pajamos - pajamos * gpm - psd


# Ilgenis aprašymas: ką daro funkcija, kodėl ji naudinga, kokie yra argumentai, kokie jų tipai, kas jie yra
def mokesciu_apskaiciavimas(pajamos: float, gpm: float = 0.15, psd: float = 58.5) -> float:
    """Lietuvos mokesčių apskaičiavimas pagal pajamas.

    Pagal 2023 metų nuostatas, pajamos turi būti deklaruojamos,
    todėl ši funkcija padeda apskaičiuoti likusias pajamas po mokesčių.
    Ji padės deklaruoti pajamas.

    :param pajamos: pajamų dydis einamaisiais metais
    :param gpm: skaičius po kablelio, nurodantis gyventojų pajamų mokestį procentais.
    Bus naudojamas padauginti pajamas ir atimti iš visų pajamų. Numatytoji reikšmė 0.15
    :param psd: skaičius po kablelio, nurodantis privalomojo sveikatos draudimo dydį. Numatytoji
    reikšmė pagal 2023 metus: 58.5
    :return: pajamos po mokesčių atskaičiavimo
    """
    return pajamos - pajamos * gpm - psd

mokesciu_apskaiciavimas(1000)


# --- Rekursyvinės funkcijos

# faktorialas 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial_for(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_for(10))

def factorial(n: int) -> int:
    # Stopping condition
    # Kitaip funkcija kvies save be sustojimo
    if n == 1:
        return 1

    # Funkcija kviečia save su pakeistu argumentu
    return n * factorial(n - 1)

print(factorial(10))

# --- Anoniminės, lambda funkcijos

def kvadratas(x):
    return x**2

# Anonimė funkcija priskirta kintamajam

# Pati funkcija pavadinimo neturi. lambda nėra pavadinimas, o raktažodis!!
kv = lambda x: x**2
# weird alternative to lambda
asdasd = kvadratas

# Su dviem argumentais
def suma_dvieju_skaiciu(x, y):
    return x + y
kita_suma_dvieju = lambda x, y: x + y

print(kvadratas(5))

skaiciai = [1, 2, 3, 4, 5]

# Map funkcija taiko nurodytą funkciją kiekvienam sąrašo elementui
kvadratai = list(map(kvadratas, skaiciai))
print(kvadratai)

kvadratai = []
for skaicius in skaiciai:
    kvadratai.append(kvadratas(skaicius))

