def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""


Buduj z nami bank przyszłości oparty na danych!


Szukamy specjalistów, którzy chcą współtworzyć transformację Banku Pekao S.A. w kierunku organizacji opartej na danych (data- driven- bank). Będziemy wspólnie rozwijać nowoczesne platformy danych i narzędzia analityczne oraz pracować projektowo i interdyscyplinarnie – z biznesem, IT, finansami i ryzykiem.


Poszukujemy osób na stanowiska: Analityk Danych / Inżynier Danych / BI Developer. Ofertę dopasujemy do Twoich kompetencji.


W naszym zespole będziesz odpowiadać za:


    Udział w strategicznym projekcie transformacyjnym „DATA”.
    Rozwój i utrzymanie platform danych (Data Lake, DWH) oraz systemów analityczno- raportowych (BI, MIS).
    Przygotowanie raportów i DataMartów na potrzeby biznesowe, zarządcze, regulacyjne.
    Współpracę z zespołami IT, finansów, ryzyka i innych domen banku.


Ta praca jest dla Ciebie, jeśli:


    Posiadasz doświadczenie w analizie danych, raportowaniu, przetwarzaniu dużych zbiorów na bazach danych (SQL, NoSQL).
    Znasz języki do przetwarzania i programowania danych (SQL, Python, SAS4GL, Scala/Spark/PySpark, LLM/NLP).
    Masz doświadczenie w pracy z narzędziami klasy DWH, BI, MIS, CRM, ETL/ELT.
    Interesujesz się przetwarzaniem dużych zbiorów danych, zarządzaniem informacją, controllingiem lub finansami w nowoczesnym wydaniu.
    Interesujesz się technologiami AI / ML / LLM.
    Łączysz kompetencje techniczne związane z przetwarzaniem danych z pracą na bazach danych i wiedzą biznesową.
    Posiadasz lub zamierzasz rozwinąć doświadczenie w modelowaniu baz danych.
    Znasz język angielski na poziomie co najmniej B2.


Oferujemy Ci:


    Zatrudnienie w ramach umowy o pracę.
    Atrakcyjne wynagrodzenie oraz premie uwzględniające indywidualne wyniki i zaangażowanie.
    Możliwość pracy hybrydowej.
    Prywatną opiekę medyczną dla Ciebie i Twojej rodziny na preferencyjnych warunkach.
    Kartę MultiSport i Ubezpieczenie Grupowe na korzystnych warunkach.
    Udział w nowatorskich i zróżnicowanych projektach o skali spotykanej wyłącznie w największych organizacjach.
    System szkoleń i programów rozwojowych, w tym dostęp do LinkedIn Learning.
    Udział w wyjątkowych inicjatywach realizowanych w Banku (wolontariat pracowniczy, letnie i zimowe mistrzostwa sportowe banku, akcje ekologiczne i prozdrowotne).


""")


print(outcome)