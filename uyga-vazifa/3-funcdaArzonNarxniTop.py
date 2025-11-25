def eng_arzon(mahsulotlar):
    natija = []
    for nom,narxlar in mahsulotlar:
        natija.append([nom,min(narxlar)])
    return natija
meva = [['Olma', [12000, 11000, 11500]], ['Banan', [13000, 12500]]]
print(eng_arzon(meva))
