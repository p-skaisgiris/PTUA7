# --- Paveldėjimas (Inheritance)
# Galimybė apjungti panašių objektų funkcionalumą, naudojant tėvines klases.
# Tai leidžia nekartoti panašaus ar to paties kodo. Taip pat nekeičiant paties objekto
# kodo, papildyti arba keisti jo funkcionalumą.

class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print("Aš bėgu")


class Kate(Gyvunas):
    def miaukseti(self):
        print("miau")


# class Suo(Gyvunas):
#     def loti(self):
#         print("Au")




class Suo(Gyvunas):
    # Override function / perrašyta funkcija
    # papildoma ypatybė antkaklio_id
    def __init__(self, vardas, spalva, antkaklio_id):
        super().__init__(vardas, spalva)
        self.antkaklio_id = antkaklio_id

    def loti(self):
        print("Au")

    def get_antkaklio_id(self):
        return self.antkaklio_id

    def set_antkaklio_id(self, new_antkaklio_id):
        """Given the data, set antkaklio_id as the new value"""
        self.antkaklio_id = new_antkaklio_id


vezlys = Gyvunas("Tadas", "zalias")
vezlys.begti()
kate = Kate("Tomas", "pilka")
kate.begti()        # Metodas iš Gyvunas klasės
kate.miaukseti()    # Metodas iš Katė klasės
suo = Suo("Bobas", "rudas", 123123123)
suo.begti()         # Metodas iš Gyvunas klasės
suo.loti()          # Metodas iš Gyvunas klasės

# --- Galima paveldėti kelis dalykus, tik JEIGU jie nėra palyginami

class GyvunuGarsai(Suo, Kate):
    pass

# gyv_garsai = GyvunuGarsai("hello", "Asd")
# gyv_garsai.miaukseti()
# gyv_garsai.loti()

# --- Polimorfizmas (Polymorphism)
# Galimybė operacijas (metodus) vykdyti skirtingai,  priklausomai nuo konkrečios
# klasės (ar duomenų tipo) realizacijos, metodo kvietėjui nežinant apie tuos skirtumus.
# Tai pasiekiama perrašant tam tikrus metodus vaikinėse  klasėse.
# Metodo (funkcijos) perrašymas (Overriding)


class Vezlys(Gyvunas):
    def begti(self):
        print("Aš ne bėgu, o einu")

    def ropoti(self):
        print("Aš ropoju")


vezlys2 = Vezlys("Rimas", "zalia")
vezlys2.begti()

gyvunai = [suo, kate, vezlys2]
for gyvunas in gyvunai:
    gyvunas.begti()

# Kaip pasiekti tėvinės klasės metodą

class Vezlys(Gyvunas):
    def begti(self):
        super().begti()  # Tėvinės klasės metodo pašaukimas
        print("Aš ne bėgu, o einu")  # Naujas funkcionalumas

    def ropoti(self):
        print("Aš ropoju")

print("******************************************")
vezlys3 = Vezlys("Rimas", "zalia")
vezlys3.begti()

# Kaip vaikinei klasei pridėti papildomas savybes

class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Vaikas(Zmogus):
    def __init__(self, vardas, pavarde, mokymosi_istaiga):
        super().__init__(vardas, pavarde)
        self.mokymosi_istaiga = mokymosi_istaiga

    def print_my_name(self):
        print(self.vardas)


zmogus = Zmogus("Tadas", "Kosciuska")
zmogus2 = Vaikas("Pranas", "Pranckietis", "KTU gimnazija")

# Kaip patikrinti, kokiai klasei priklauso objektas (biudžeto pavyzdys)

class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    pass


class IslaiduIrasas(Irasas):
    pass


pajamos1 = PajamuIrasas(200)
pajamos2 = PajamuIrasas(100)
islaidos1 = IslaiduIrasas(12.2)
islaidos2 = IslaiduIrasas(26.8)

biudzetas = [pajamos1, pajamos2, islaidos1, islaidos2]

balansas = 0
for elementas in biudzetas:
    # Checking specific class
    # if type(elementas) == PajamuIrasas:
    # Checking class and class instance
    if isinstance(elementas, PajamuIrasas):
        balansas += elementas.suma
    else:
        balansas -= elementas.suma

print("balansas: ", balansas)