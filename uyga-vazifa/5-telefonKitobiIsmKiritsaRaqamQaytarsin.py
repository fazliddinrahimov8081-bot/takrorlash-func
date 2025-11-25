def telefon_top(kitob,ism):
    return kitob.get(ism,"Topilmadi")
kitob = {
    'Ali': '998901234567',
    'Gulnoza': '998935678901'
}
print(telefon_top(kitob,"Ali"))