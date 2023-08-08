# 1. Kas yra kintamasis? Kodėl kintamieji yra naudingi? Kaip jį sukurti?

# Kintamieji mums duoda daug galios programavimui, skaiciavimams ir t.t.
# Taip sukuriamas String kintamasis
kazkas = 'Paulius'

# 2. Kaip sukurti sveiko skaičiaus / int kintamąjį? Kam jis naudingas?

intas = 42
intas2 = intas + 4

# 3. Kaip sukurti netaisyklingo skaičiaus / float kintamąjį? Kam jis naudingas?

floatas = 7.36


# 4. Kaip pakelti skaičių 1.1 kvadratu?

result41 = pow(3, 2)
result42 = 3**2

# 5. Kaip sukurti string kintamąjį? Kam jis naudingas?

result5 = 'Paulius'

# 6. Kaip sukurti tuple? Kam jis naudingas?

# Classic
result6 = (1, 2, 3, 4)
# Lazy
result62 = 2, 2, 2
# Conversion
x = [1, 2, 3]
y = tuple(x)

# 7. Kaip sukurti list? Kam jis naudingas?

# Tuscias listas
result7 = list()
result71 = []
# Square brackets
result72 = ["a", "b", "c", 1.23]

# Kaip sukurti aibe / seta?

# Manual creation of empty set
result75 = set()
# This is a dictionary, not a set!!
result78 = {}
# Manual data in set
result76 = {1, 2, 3}
# Conversion
result77 = set((1,2,3))

# 8. Kaip ištraukti trečią elementą iš tuplo? Iš listo? Iš seto?

tuplas = ("a", "b", "c")
listas = ["a", "b", "c"]
setas = {"a", "b", "c"}

print(tuplas[2])
print(listas[2])
# Negalima! Setas neturi eiliskumo
# print(setas[2])

# 9. Kaip priskirti naują reikšmę tuplui? Listui? Setui?

# Negalima!
# tuplas[2] = 123

listas[2] = 123

# Seto naujos reikmes priskyrimas yra keistas...
setas.remove("b")
setas.add("d")

# 10. Kaip gauti didžiausią skaičių iš tuplo? Listo? Seto?

tuplas_int = (1,2,3)
listas_int = [1,2,3]
setas_int = {1,2,3}
max_tuple = max(tuplas_int)
max_list = max(listas_int)
max_set = max(setas_int)
print(max_tuple, max_list, max_set)

# 11. Kaip praiteruoti / išskleisti tuplą? Listą? Setą?

print("israsom list po viena")
for i in listas_int:
    print(i)

print("enumerate list")
for i, val in enumerate(listas_int):
    print(i, val)

print("israsomas set po viena")
for i in setas_int:
    print(i)

# 12. Kaip sukurti loginį / bool kintamąjį? Kam jis naudingas?

asd = True
dsa = False

# (Sunkiau!)
# 13. Kaip patikrinti, jog sveikas skaičius 4 yra lygus 2 kvadratui?

print("exercise 13")
x = 4
e = 2**2
res = (x == e)
print(res)

# 14. Kaip patikrinti, kad kažkoks (svarbu! Reikšmės galbūt nežinosime) kintamasis x yra NElygus 10?

print(x != 10)

# 15. Kaip patikrinti, kad kažkoks kintamasis x yra 5 arba tarp 11-14?

# Hacky but works (veikia tik su sveikaisiais skaiciais)
print(x == 5 or (x in range(11, 14)))
# Alternative, universal, works with arbitrary float numbers
print(x == 5 or 11 <= x <= 14)

# 16. Kaip patikrinti, kad kažkoks kintamasis x yra tarp 11-100 IR yra kvadratas kazkokio sveiko skaiciaus?
# Prisiminkite: pakelti 0.5 laipsniu reiskia istraukti sakni

print("Exercise 16")
for x in range(1, 101):
    # print(x)
    # Traukiam sakni is kazkokio skaiciaus ir apvalinam
    square_int = round(x**0.5)
    # Traukiam sakni is kazkokio skaiciausi ir NEapvalinam
    square = x ** 0.5
    if 11 <= x <= 100 and square - square_int == 0:
        print("Version 1", x)

    if 11 <= x <= 100 and x % (x ** 0.5) == 0:
        print("Version 2", x)
