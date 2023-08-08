"""
Programos tikslas:
Gavus listą su palaikinusiais žmonių vardais, išvesti kas 'laikina', kaip pavyzdžiuose:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Jei daugiau nei 4 žmonės, tiesiog didiname skaičių prie "2 others".
"""

users = []
for i in range(100):
    like = str(input('koks laikintojo vardas? Jei nenorite tęsti, spausskite Enter: '))
    if like == '':
        if len(users) == 0:
            print(' niekam nepatinka')
            exit()
    users.append(like)
    if len(users) == 1:
        print(f"{like[0]} patinka")
    if len(users) == 2:
        print(f"{users[0]} ir {users[1]} patinka")
    if len(users) == 3:
        print(f"{users[0]} , {users[1]} ir {users[2]} patinka")
    if len(users) >= 4:
        print(f"{users[-2]}, {users[-1]} ir dar {len(users)-2} patinka ")