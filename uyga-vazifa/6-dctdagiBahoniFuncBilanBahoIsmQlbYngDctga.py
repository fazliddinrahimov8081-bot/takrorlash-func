def guruhla (baholar):
    natija = {}
    for ism, baho in baholar.items():
        if baho not in natija:
            natija[baho] = []
        natija[baho].append(ism)
    return natija
print(guruhla({'Ali': 5, 'Vali': 4, 'Gulnoza': 5}))