class dane_firmy:

    nip_attr = '666-66-66-666'
    nazwa_attr = 'Firmex'
    adres_attr = 'ul. Polna 5, 66-666 Pcimie Dolne'
    email_attr = 'biuro@firmex.pl'
    telefon_attr = '505505505'

    def __init__(self):
        print("Dane firmy:")
        print(f'NIP: {self.nip_attr}')
        print(f'Nazwa: {self.nazwa_attr}')
        print(f'Adres: {self.adres_attr}')
        print(f'E-mail: {self.email_attr}')
        print(f'Telefon: {self.telefon_attr}')


    def faktura_na_klienta(self, klient_nazwa, klient_nip):
        print(f'Faktura dla klienta: {klient_nazwa}')
        print(f'NIP klienta: {klient_nip}')
        print(f'Dane firmy: {self.nazwa_attr}, NIP: {self.nip_attr}')