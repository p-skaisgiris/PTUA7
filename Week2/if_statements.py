# IF statement / sąlyga "jeigu"
# Skaičius didesnis už 50

"""
if <condition>:
    ...

where <condition> is statement resulting in a boolean value
"""
print("--------------------- Example 1 -----------------------")
number = 49
if number > 50:
    print("Skaicius didesnis uz 50")
    print("asd")
    print("....some more code")
    # Empty statement not doing anything, just a placeholder
    pass

# ELSE statement / sąlyga "jei ne"
# Skaičius didesnis už 50, mažesnis už 50

"""
if <condition>:
    ...
else:
    ...

where <condition> is statement resulting in a boolean value
"""

number = 51
print("--------------------- Example 2 -----------------------")
if number > 50:
    print("Skaicius didesnis uz 50")
else:
    print("Skaicius nera didesnis uz 50")

# ELIF statement / sąlyga "jei sąlyga netenkinama ir jei"
# Skaičius - teigiamas, lygus nuliui, skaičius - neigiamas

print("--------------------- Example 3 -----------------------")

number = 0
if number > 0:
    print("skaicius yra teigimas")
elif number < 0:
    print("skicius yra neigiamas")
elif number == 5:
    print("skicius yra 5")
else:
    print("Skaicius yra nulis")

# ELIF statement without else

print("--------------------- Example 4 -----------------------")

number = 5
if number > 0:
    print("skaicius yra teigimas")
elif number < 0:
    print("skicius yra neigiamas")
elif number == 5:
    print("skaicius yra 5")

# (Beveik) alternatyva viršutiniam variantui. Flag check

print("--------------------- Example 5 -----------------------")

condition1 = False
condition2 = False
condition3 = False

if number > 0:
    condition1 = True
    print("skaicius yra teigimas")

if number < 0:
    condition2 = True
    print("skicius yra neigiamas")

if number == 5:
    condition3 = True
    print("skicius yra 5")

# Nested if statements

print("--------------------- Example 6 -----------------------")

number = -1
if number > 0:
    if number < 10:
        print(f"0 < {number} < 10")
        if True:
            pass
            if True:
                pass
            else:
                pass
        else:
            print("")
    else:
        print("")
else:
    print("not like that")

if 0 < number < 10:
        print(f"0 < {number} < 10")
else:
    print("not like that")
