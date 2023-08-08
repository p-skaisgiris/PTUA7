## Užduotis 1

Parašyti programą, kuri atspausdintų skaičius tokiu būdu:

```commandline
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Tai yra, atspausdintų skaičius vieną po kito iki kažkokio skaičiaus `n`. Pavyzdžio atveju, `n = 5`

## Užduotis 2

Parašyti programą, kuri:
- Leistų vartotojui įvesti skaičių `n`.
- Suskaičiuotų sumą visų skaičiu nuo 1 iki `n` ir ją išrašytų

## Užduotis 3

Parašyti programą, kuri:
- Leistų vartotojui įvesti skaičių.
- Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
- Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą

## Užduotis 4

Parašyti programą, kuri:
- Leistų vartotojui įvesti skaičių.
- Suskaičiuotų, kiek skaitmenų yra įvestame SKAIČIUJE
- Dirbti su skaičiaus tipu, o ne stringu, nes kitaip tai padaryti labai paprasta su `len(n)`

Patarimas: prisiminkite sveiko skaičiaus dalybą su //

## Užduotis 5

PATARIMAS: šiai užduočiai naudokite `range` funckiją su trimis argumentais. 
Pasiskaitykite internete ką ši Pythono funkcija daro su kiekvienu argumentu ir kaip juos naudoti

Parašykite programą, kuri:
- Leistų vartotojui įvesti skaičių `n`
- Išrašytų visus pirmuosius `n` lyginius skaičius atbula tvarka
Pvz., jei `n = 13`:
```
26
24
22
20
18
16
14
12
10
8
6
4
2
0
```

Parašykite dar vieną programą, kuri:
- Leistų vartotojui įvesti skaičių `n`
- Išrašytų visus skaičius, kurie dalijasi iš 7, nuo `n` iki 0 atbula tvarka
Pvz., jei `n = 66`:
```
63
56
49
42
35
28
21
14
7
```

## Užduotis 6

Parašyti programą, kuri atspausdintų skaičius tokiu būdu:

```commandline
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
```

Tai yra, atspausdintų skaičius vieną po kito _atbuline tvarka_ nuo kažkokio skaičiaus `n`. Pavyzdžio atveju, `n = 5`

## Užduotis 7

Sukurti programą, kuri:
- Leistų vartotojui įvesti 5 žodžius
- Pridėtų įvestus žodžius į sąrašą
- Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį\

Patarimas: Naudoti list, ciklą for, funkcijas len ir index

## Užduotis 8

Išrašytų visus pirminius skaičius (dalijasi tik iš savęs ir iš 1)
nurodytose ribose. Pvz.:

```python
# range
start = 25
end = 50
```

```commandline
Prime numbers between 25 and 50 are:
29
31
37
41
43
47
```

## Užduotis 9

Fibonačio skaičių seka – sveikųjų skaičių seka. Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233. 
Pirmieji du skaičiai yra visada 0 ir 1. Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai.
Trečiasis skaičius tuomet bus apskaičiuojamas taip: 0 + 1 = 1. Ketvirtasis: 1 + 1 = 2. Penktasis: 1 + 2 = 3 ir t.t. 

Parašykite programą, kuri išrašytų pirmuosius `n` Fibonačio skaičius.

## Užduotis 10 (Sunku!)

Parašykite Bubble Sort listo rūšiavimo algoritmą Pythone. Bubble Sort algoritmo aprašymą galite rasti čia:
https://en.wikipedia.org/wiki/Bubble_sort#Analysis
