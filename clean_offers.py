import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """




Job description

Clurgo to firma stworzona przez developerów dla developerów. Nasze zespoły łączą pełne spektrum kompetencji - od rozwoju oprogramowania i infrastruktury, przez analizę oraz testy, aż po strategiczne zarządzanie produktem i procesami. Realizujemy różnorodne projekty IT dla klientów z wielu branż, dbając o dobre praktyki programistyczne i zachowanie work-life balance. Tworzymy rozwiązania, które mają znaczenie - dla firm w Polsce i na całym świecie.

✅ Dołączysz do strategicznego programu transformacji cyfrowej dużej organizacji z sektora ubezpieczeniowego. Projekt koncentruje się na rozwoju i transformacji środowiska danych oraz raportowania.

Będziesz współpracować z biznesem oraz zespołami technicznymi, analizując wymagania, duże wolumeny danych i wspierając projektowanie nowych rozwiązań.

✅Technologie i narzędzia: SQL, SAS, Enterprise Guide, 4GL

Szukamy Ciebie, jeśli:

    masz 4+ lata doświadczenia na podobnym stanowisku

    masz minimum 2 lata doświadczenia w analizie biznesowej lub systemowej w obszarze danych, hurtowni danych lub BI

    bardzo dobrze znasz SQL i potrafisz samodzielnie analizować duże wolumeny danych

    masz doświadczenie w przygotowywaniu dokumentacji analitycznej i specyfikacji wymagań

    potrafisz modelować procesy biznesowe

    masz doświadczenie w tworzeniu scenariuszy i przypadków testowych

    potrafisz współpracować bezpośrednio z użytkownikami biznesowymi i zespołami technicznymi

    masz analityczne podejście i potrafisz przekładać potrzeby biznesowe na rozwiązania IT

Mile widziane:

    doświadczenie w branży ubezpieczeniowej

    znajomość SAS, Enterprise Guide lub 4GL

    doświadczenie w projektach hurtowni danych, migracji danych lub przebudowy architektury danych

Zadania:

    analiza wymagań i procesów biznesowych

    przygotowywanie analiz, specyfikacji funkcjonalnych i dokumentacji projektowej

    analiza dużych wolumenów danych

    współpraca z biznesem przy definiowaniu wymagań dla rozwiązań danych i raportowych

    przygotowywanie scenariuszy i przypadków testowych

    współpraca z zespołami developerskimi przy projektowaniu i wdrażaniu rozwiązań

    udział w projektach związanych z rozwojem i transformacją środowiska danych oraz raportowania

Czego możesz się spodziewać:

    współpracy w oparciu o kontrakt B2B

    profesjonalnego procesu rekrutacyjnego – zawsze otrzymasz od nas feedback niezależnie od decyzji

 Poznaj nas lepiej👉 https://www.facebook.com/clurgo/

"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)