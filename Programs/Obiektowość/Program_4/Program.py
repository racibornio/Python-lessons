from Zasoby_klas import dane_firmy

dane_dokumentu_o = dane_firmy()
print()
print('NIP firmy to:', dane_dokumentu_o.nip_attr)
print('Nazwa firmy to:', dane_dokumentu_o.nazwa_attr)
print('Adres firmy to:', dane_dokumentu_o.adres_attr)
print('E-mail firmy to:', dane_dokumentu_o.email_attr)
print('Telefon firmy to:', dane_dokumentu_o.telefon_attr)
print()

dane_dokumentu_o.faktura_na_klienta('Jan Kowalski', '123-45-67-890')