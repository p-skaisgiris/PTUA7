# Užduotis 1

Parašyti programą, kuri:
- Leistų vartotojui įvesti pradžios ir pabaigos datą
- Suskaičiuotų kiek praėjo sekundžių tarp datų

# Užduotis 2

Parašyti programą, kuri:
- Atspausdintų dabartinę datą ir laiką
- Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
- Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
- Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17

- Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

# Užduotis 3

Parašyti programą, kuri:
- Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
- Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
  - Metų
  - Mėnesių
  - Dienų
  - Valandų
  - Minučių
  - Sekundžių
- Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.

Patarimas: naudoti datetime, .days, .total_seconds(), round

# Užduotis 4

Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms, programos mestų norimas klaidas lietuvių kalba 
(panaudoti try/except)

# Užduotis 5

Parašyti programą, kuri atspausdintų norimą žodį, kas X sekundžių. Programa turi:
- Gauti sekundes iš vartotojo
- Spausdinti vartotojo įvesta žodį
- Įvedus netinkamą sekundžių formatą, programa turi paprašyti įvesti sekundes iš naujo
