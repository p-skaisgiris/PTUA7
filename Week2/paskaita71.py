# Mass comment/uncomment:
# CTRL + /

# procentas = float(input("Iveskite procenta"))
#
# if 80 <= procentas <= 100:
#     print('A+')
# if 60 <= procentas < 80:
#     print('A')
# if 50 <= procentas < 60:
#     print('B+')
# if 45 <= procentas < 50:
#     print('B')
# if 25 <= procentas < 45:
#     print('C')
# if 0 <= procentas < 25:
#     print('D')

print('.....3.....')
num = int(input('Įveskite gautų balų skaičių nuo 1 iki 100: '))

if num in range(0, 26):
    print("Jūs įvertintas 'D'")
elif num in range(26, 46):
    print("Jūsų įvertinimas 'C'")
elif num in range(46, 51):
    print("Jūsų įvertinimas 'B'")
elif num in range(51, 61):
    print("Jūsų įvertinimas 'B+'")
elif num in range(61, 81):
    print("Jūsų įvertinimas 'A'")
elif num in range(81, 101):
    print("Jūsų įvertinimas 'A+'")
else:
    print("Jūsų įvestis neatitinka reikalavimų!")
