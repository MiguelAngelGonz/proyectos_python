huevos = [2, 3, 5, 7, 12, 13, 18]

def contador_huevos(huevos):
    contador = 0
    for huevo in huevos:
        if huevo % 2 == 0:
            contador += huevo
    return contador

print(contador_huevos(huevos))