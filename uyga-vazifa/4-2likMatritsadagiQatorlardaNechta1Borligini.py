def nechta_bir(matritsa):
    natija  =[]
    for qator in matritsa:
        natija.append(qator.count(1))
    return natija
print(nechta_bir([[1, 0, 1], [1, 1, 0], [0, 0, 1]]))