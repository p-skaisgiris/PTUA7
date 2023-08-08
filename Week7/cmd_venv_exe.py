# --- Kas yra cmd?
# cmd - Command Prompt programa Windows operacinėje sistemoje.
# cmd yra Windows'ų terminalas, galime paleisti programas "rankiniu" būdu (o ne
# grafiniu būdu naudojant pelę kaip esame pripratę įprastai naudojant Windows)

# --- Kaip atidaryti cmd?
# Paspausti Windows ikoną, įvesti "cmd" (be kabučių) į paiešką, paspausti Enter ant
# klaviatūros

# --- Kaip naviguoti ir sukurti direktoriją per cmd?
# dir - išrašyti visus failus direktorijoje
# cd - pakeisti vietą, nueiti į kitą direktoriją
# mkdir - sukurti naują direktoriją

# Pvz:
mkdir python-game
cd python-game

# --- Kas yra pip?
# pip yra Python paketų tvarkyklė.
# Tai reiškia, kad tai yra įrankis, leidžiantis įdiegti ir valdyti bibliotekas ir
# priklausomybes, kurios nėra platinamos kaip standartinės Python bibliotekos dalis.

# --- Kaip pažiūrėti kokie moduliai įdiegti sistemoje?

pip list
# arba
pip freeze

# --- Kas yra virtuali programavimo aplinka (virtual environment arba venv)?
# Virtuali aplinka padeda:
# - Išskirstyti skirtingų projektų naudojamus įrašytus paketus
# - Jei kažkokia klaida kyla viename projekte, ji nekenkia kitiems python projektams
# - Mažiau resursų naudojama naudotojo, nes nereikia instaliuoti visų jūsų instaliuotų
#   paketų

# --- Kaip sukurti virtualią programavimo aplinką per cmd?

python -m venv virtuali

# --- Kaip aktyvuoti/deaktyvuoti venv per cmd?

# Aktyvavimas:
virtuali\Scripts\activate.bat
# Deaktyvavimas:
deactivate

# --- Kaip įdiegti naujus paketus į virtualią aplinką?

pip install ...
# pvz.:
pip install pandas

# --- Kaip sukurti reikalavimų failą?

# Išrašom visus išorinius paketus
pip freeze
# Išsaugom visus išorinius paketus į failą
pip freeze > requirements.txt

# --- Kaip įdiegti paketus iš reikalavimų failo?

pip install -r requirements.txt

# --- Kaip sukurti naują projektą ir virtualią aplinką PyCharm projekte?

File -> New project -> New environment using Virtualenv -> Create

# --- VENV pastabos
# - Į virtualią aplinką nededame jokių projekto (.py ir kitų) failų
# - Virtualios aplinkos katalogo nededame į versijų valdymo sistemų repozitorijas
# - Dedame requirements failą, kad kiti kodu besinaudojantys asmenys galėtų
#   susikurti savo virtualias aplinkas
