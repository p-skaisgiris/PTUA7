DAYS_IN_YEAR = 365.25

def kazkokia(x: int, y: str) -> float:
    if type(x) != int:
        raise ValueError("Ne toks x kintamojo tipas, turi būti int")

    if x == 1:
        return "vienas"
    elif x == 2:
        return 2
    elif x == 3:
        return 3.0
    else:
        return None


res = kazkokia(1.2, "asd")
print(res)
print(type(res))