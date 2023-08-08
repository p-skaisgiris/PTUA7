# --- Kada gali prireikti get/set metodų
# Darbuotojo klase: vardas, pavarde, atlyginimas
# atlyginimas neigiamas - negali buti

class Darbuotojas:
    def __init__(self, vardas: str, pavarde: str, atlyginimas: float):
        if isinstance(vardas, str):
            self._vardas = vardas
        else:
            raise ValueError("vardas is not a str")

        if isinstance(pavarde, str):
            self._pavarde = pavarde
        else:
            raise ValueError("pavarde is not a str")

        if isinstance(atlyginimas, float):
            if atlyginimas > 0:
                self._atlyginimas = atlyginimas
            else:
                raise ValueError("atlyginimas is less than 0")
        else:
            raise ValueError("atlyginimas is not a float")

    def get_vardas(self):
        return self._vardas

    def set_vardas(self, vardas):
        if isinstance(vardas, str):
            self._vardas = vardas
        else:
            raise ValueError("vardas is not a str")

    def get_pavarde(self):
        return self._pavarde

    def set_pavarde(self, pavarde):
        if isinstance(pavarde, str):
            self._pavarde = pavarde
        else:
            raise ValueError("pavarde is not a str")

    def get_atlyginimas(self):
        return self._atlyginimas

    def set_atlyginimas(self, atlyginimas):
        if isinstance(atlyginimas, float):
            if atlyginimas > 0:
                self._atlyginimas = atlyginimas
            else:
                raise ValueError("atlyginimas is less than 0")
        else:
            raise ValueError("atlyginimas is not a float")


darbuotojas1 = Darbuotojas("petras", "petraitis", 1000.0)
print("darbuotojo1 vardas: ", darbuotojas1.get_vardas())

# darbuotojas1.vardas = 123
# darbuotojas1.set_pavarde(123)
print("darbuotojo1 atlyginimas pries pakeitima: ", darbuotojas1.get_atlyginimas())
darbuotojas1.set_atlyginimas(float(700))

# print("darbuotojo1 vardas po pakeitimo: ", darbuotojas1.get_vardas())
# darbuotojas1.atlyginimas = -1000
print("darbuotojo1 atlyginimas po pakeitimo: ", darbuotojas1.get_atlyginimas())

# --- Dekoratorius @property
# Rašosi virš klasių metodų; setteriai priklauso nuo property pavadinimo


class Kate:
    def __init__(self, vardas):
        self._vardas = vardas

    # More general method appearing in other OOP languages
    def get_vardas(self):
        return self._vardas

    def set_vardas(self, vardas):
        if isinstance(vardas, str):
            self._vardas = vardas
        else:
            raise ValueError("vardas is not a str")

print("*********************************************")
kate1 = Kate("tomas")
print("kates vardas pries pakeitima: ", kate1.get_vardas())
kate1.set_vardas("pilkius")
print("kates vardas po pakeitimo: ", kate1.get_vardas())


class Kate2:
    def __init__(self, vardas):
        self._vardas = vardas

    # Very pythonic way of using getter/setter methods
    @property
    def vardas(self):
        return self._vardas

    @vardas.setter
    def vardas(self, new_vardas):
        if isinstance(new_vardas, str):
            self._vardas = new_vardas
        else:
            raise ValueError("vardas is not a str")

print("*********************************************")
kate1 = Kate2("tomas")
print("kates vardas pries pakeitima: ", kate1.vardas)
kate1.vardas = "pilkius"
print("kates vardas po pakeitimo: ", kate1.vardas)

# --- Debug - Klaidų taisymas
# Paspauskite kairiu pelės mygtuku ant norimos kodo eilutės kairėje
# Šioje vietoje jūsų kodas sustos ir galėsite pamayti toje vietoje nustatytas
# kintamųjų reikšmes. Tai dažniausiai leidžia pamatyti, ar yra įvelta kokia nors klaida


def patikrinti_skaiciu(skaicius):
    if skaicius < 0:
        print("Skaičius teigiamas")
    if skaicius == 0:
        print("Skaičius lygus 0")
    if skaicius < 0:
        print("Skaičius neigiamas")

patikrinti_skaiciu(20)

# --- Kaip patikrinti objektus

class Automobolis:
    def __init__(self, modelis, metai):
        self.modelis = modelis
        self.metai = metai

toyota = Automobolis("Toyota Auris", 2015)
tesla = Automobolis("Tesla Y", 2020)

pass