a = "hello"

try:
    if isinstance(a, str) and len(a) > 7:
        print("a yra string ir a ilgis yra 7 arba daugiau")
    else:
        raise ValueError("a nera string arba a yra trumpesnis uz 7")
except:
    raise AttributeError("hello dar vienas")

