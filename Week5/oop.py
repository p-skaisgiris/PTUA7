# Object Oriented Programming (OOP)
# Objektinis programavimas – programavimo būdas, naudojant objektus ir jų sąveikas
# Objektas – į vieną vienetą (klasę) sutalpintos susijusios savybės
# ir funkcionalumas (kintamieji, funkcijos ir t.t.)


# --- Skirtumai tarp funkcijų ir objektų
# Funkcijos dirba tik su išoriniais duomenimis, metodai dirba su vidiniais (ir
# išoriniais) duomenimis
def func(asd):
    print(asd)
    return 1

a = "hello"
func(a)

import datetime
now = datetime.datetime.now()
print(now)
# Objekto kintamieji vadinami savybėmis (Property)
print(now.minute)
# o funkcijos – metodais (Methods)
print(now.strftime("%y-%m-%d"))


# Kaip sukuriama objekto klasė:
# Objekto klasė duomenų nesaugo. Ji yra lyg instrukcija, pagal kurią sukuriamas
# objektas (kuris saugo objekto duomenis).
# __init__ metodas (konstruktorius) yra automatiškai įvykdomas kuriant objektą.
# Jame gali būti inicijuojamos savybės (objekto kintamieji), paleidžiami metodai
# (funkcijos) ir t.t.

# --- Pirmasis klasės pavyzdys


class Cat:
    # Constructor
    def __init__(self, name: str, colour: str, eyes_colour: str, legs: int):
        self.name = name
        self.colour = colour
        self.legs = legs
        self.eyes_colour = eyes_colour

    # Method
    def do_meow(self):
        print("meow")

    def extend_name(self):
        name = self.name + "_hello"
        self.do_meow()
        print(name)


cat1 = Cat(name="Mice", colour="grey", eyes_colour="red", legs=4)
cat2 = Cat("Tom", "white", "blue", 2)

# cat3 = Cat(name=12.3, colour="grey", eyes_color="red",legs=4)

print(cat2)
# cat2.extend_name()

# cat1.do_meow()
# print(f"cat1. name: {cat1.name}, legs: {cat1.legs}, colour: {cat1.colour}")
# print(f"cat2. name: {cat2.name}, legs: {cat2.legs}, colour: {cat2.colour}")

# Inkapsuliacija (Encapsulation) – vidiniai objekto (klasės) duomenys yra slepiami ir
# pasiekiami tik metodais (savybėmis, funkcijomis).
# Tai leidžia neprisirišti prie vidinės objekto struktūros, jį nesunkiai pakeisti
# kitu arba pakeisti jo struktūrą, nekeičiant pirminio kodo

# Abstrakcija (Abstraction) – galimybė naudotis objektais, nesigilinant į tai,
# kaip jie veikia. Supaprastina objektų naudojimą, sumažina pakeitimų poveikį
# likusiams kodui


class Cat:
    # Constructor
    def __init__(self, name: str, colour: str, eyes_colour: str, legs: int,
                 chip_id: int):
        self._name = name
        self._colour = colour
        self._legs = legs
        self._eyes_colour = eyes_colour
        # Protected property
        self._chip_id = chip_id

    def _decode_name(self):
        pass

    # Getter method for name
    def get_name(self):
        """Returns the name of the cat

        :return: name
        """
        # Make sure to return only a decoded name
        decoded_name = self._decode_name()
        return decoded_name

    # Protected method (not intended for direct use by the user)
    # to verify if the supplied name is a string
    def _verify_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Name is not a string")

        if len(name) > 100:
            raise ValueError("Too long name for cat")

    def set_name(self, name: str):
        # Make sure that the supplied name is a string
        self._verify_name(name)
        # If it is, encode it
        encoded_name = self._encode_name(name)
        # Set it as the name of this cat class instance
        self.name = name

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    # Method
    def do_meow(self):
        print("meow")

    def extend_name(self):
        name = self.name + "_hello"
        self.do_meow()
        print(name)

    # Protected methods
    def _move_legs(self):
        pass

    def _watch_where_to_run(self):
        pass

    def run(self):
        self._move_legs()
        self._watch_where_to_run()
        print("running")


class Account:
    def __init__(self, username, password):
        self._username = username
        self._verify_password(password)
        # self._password = self._encode_password(password)
        self._password = password
        self._id = None

    def _verify_password(self, password):
        pass

    def _encode_password(self, password):
        pass

    def get_password(self) -> str:
        # return self._decode_password()
        return self._password

    def set_password(self, password):
        self._verify_password(password)
        self._password = self._encode_password(password)

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

class AccountIDs:
    def __init__(self, company_name, usernames, ids):
        self.company_name = company_name
        self.usernames = usernames
        self._ids = ids

    def get_id(self, username):
        if username in self.usernames:
            i = self.usernames.index(username)
            return self._ids[i]
        else:
            print("no id found")


acc = Account(username="paulius", password="123456")
acc_id = AccountIDs()
# acc.get_password()
# # acc.password = "abcdefg"
# acc.set_password("abcdefg")
print(acc.get_password())
print(acc.get_id())

acc.set_id()

ASD = "asd"
def hello():
    print("hello")






# cat4 = Cat(name="Jonas", colour="grey", eyes_colour="red", legs=4, chip_id=123123)
# cat4.run()
# cat4 = Cat(name="Paulius", colour="grey", eyes_colour="red", legs=4, chip_id=123123)


# --- Kaip pakeisti objekto spausdinimą (str ir repr metodai)
# __repr__    developeriams, dažniausiai objekto sukūrimo pavyzdys
# __str__     naudotojams, dažniausiai "žmonių" kalba apibūdinama objekto instancė




