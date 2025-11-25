def filter_ichimliklar(mahsulotlar):
    natija = []
    for m in mahsulotlar:
        if m ['narx'] < 10000 and m['tur'] =='ichimlik':
         natija.append(m)
    return natija
mahsulotlar = [
    {'nom': 'Cola', 'narx': 9000, 'tur': 'ichimlik'},
    {'nom': 'Non', 'narx': 3000, 'tur': 'ovqat'},
    {'nom': 'Suv', 'narx': 5000, 'tur': 'ichimlik'}
]
print(filter_ichimliklar(mahsulotlar))
