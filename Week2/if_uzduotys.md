## Užduotis 1

Parašyti programą, kuri:
- Leistų įvesti skaičius a ir b (int arba float)
- Išvestų į ekraną „a mažesnis už b“, jei taip yra
- Išvestų į ekraną „a lygu b“, jei taip yra
- Išvestų į ekraną „a didesnis už b“, jei taip yra

- Patarimas: naudoti if, elif, else sąlygas

## Užduotis 2

Parašyti programą, kuri:
- Leistų įvesti skaičių
- Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
- Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
- Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų

- Patarimas: naudoti input(), if, print, %, <, >

## Užduotis 3

Parašyti programą, kuri suskaičiuotų amerikietiškus pažymius pagal procentus:
- Leistų įvesti skaičių
- Išvesti į ekraną „D“, jei procentų mažiau nei 25
- Išvesti į ekraną „C“, jei procentų nuo 25 iki 45
- Išvesti į ekraną „B“, jei procentų nuo 45 iki 50
- Išvesti į ekraną „B+“, jei procentų nuo 50 iki 60
- Išvesti į ekraną „A“, jei procentų nuo 60 iki 80
- Išvesti į ekraną „A+“, jei procentų daugiau nei 80

## Užduotis 4

Parašyti programą, kuri:
- Leistų įvesti du skaičius `total_working_days` ir `absent_days` (abu `int`), kurie bus atitinkamai
  - Viso darbo dienų skaičius
  - Kiek darbo dienų praleista (dėl ligos ar pan.)
- Suskaičiuotų, kiek procentų darbuotojas lankėsi darbe ir išrašytų tai
- Jei apsilankyta darbe mažiau nei 70%, tai išrašytų 'Su Jumis susisieks darbo administracija'

## Užduotis 5

Turime tokį kodą:

```python
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print(i, j, k)
```

Kokias reikšmes šis paleistas kodas atvaizduos, jei mūsų i, j, k reikšmės bus:

a) i = 3, j = 5, k = 7

b) i = -2, j = -5, k = 9 

c) i = 8, j = 15, k = 12 

d) i = 13, j = 15, k = 13

e) i = 3, j = 5, k = 17,

f) i = 25, j = 15, k = 17

Išrašykite visus atvejus askirai, pvz.:

a) 2 3 4

b) 1 1 12

c) 9 8 5 

...