def ortacha_baholar(b):
    natija =[]
    for ism, baholar in b:
        orta  = sum(baholar) / len(baholar)
        natija.append([ism,round(orta,2)])
    return natija
baho =  [['Ali', [5, 4, 3]], ['Gulnoza', [4, 4, 5]]]
print(ortacha_baholar(baho))