import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """




W związku z dynamicznym rozwojem Biuro IT Centralnego Portu Komunikacyjnego sp. z o.o. poszukuje kandydatów na stanowisko: Ekspert ds. projektów IT (K/M)

 

Czym będziesz się zajmować:

    Współpraca z właścicielami biznesowymi i analitykami w celu efektywnego ustalenia uzgodnień projektowych
    Kierowanie realizacją projektów IT w całym cyklu życia
    Tworzenie planów, harmonogramów, monitorowanie postępów prac i ryzyk projektowych
    Raportowanie postępów prac projektowych
    Organizacja testów, przygotowanie do wdrożenia i powołania usług IT
    Zarządzanie komunikacją w ramach prowadzonych projektów
    Koordynacja prac podwykonawców i zaangażowanych zespołów wewnętrznych oraz postępowań zakupowych
    Tworzenie dokumentacji projektowej
    Pełnienie funkcji koordynatora umów, w ramach których są wdrażane lub rozwijane usługi IT
    Współpraca z biurami, wykonawcami zewnętrznymi, deweloperami i testerami przy realizacji i wdrażaniu projektów IT
    Koordynowanie odbiorów dokumentacji analitycznej i projektowej
    Współpraca z zespołami projektowymi
    Współpraca z producentami oprogramowania oraz innymi zewnętrznymi podmiotami
    Udział od strony IT w postępowaniach zakupowych związanych w wdrażaniem projektów IT

Nasze wymagania:

    Wykształcenie wyższe (preferowane techniczne IT lub związane z zarządzaniem projektami)
    Wiedza teoretyczna i praktyczna z zakresu metodyk PRINCE2/AGILE/SCRUM
    Minimum 5-letnie doświadczenie w prowadzeniu projektów i zarządzaniu zespołami projektowymi
    Doświadczenie w testowaniu i wdrażaniu aplikacji
    Bardzo dobra znajomość pakietu Microsoft Office 365
    Znajomość narzędzia Microsoft Project Portfolio Management
    Samodzielność w organizacji pracy i realizacji powierzonych zadań
    Wysokie zdolności interpersonalne, komunikacyjne i prezentacyjne
    Znajomość języka angielskiego na poziomie umożliwiającym swobodną komunikację

Co oferujemy:

    Udział w największym projekcie infrastrukturalnym w Polsce o międzynarodowym znaczeniu
    Kultura organizacyjna oparta na współpracy, partnerskich relacjach oraz innowacyjności
    Środowisko pracy zapewniające równe traktowanie oraz wsparcie dla różnorodności
    Zatrudnienie na podstawie umowy o zastępstwo
    Elastyczne godziny rozpoczęcia pracy
    Rozwój zawodowy oparty na szkoleniach wewnętrznych i zewnętrznych
    Dofinansowanie do prywatnej opieki medycznej
    Dostęp do platformy benefitowej, w tym karty sportowej
    Dofinansowanie do ubezpieczenia grupowego na życie
    Dofinansowanie do wypoczynku
    Zniżki na zakupy w sklepach sieci Baltona
    Dostęp do programu well-being
    Pracę w nowoczesnym biurze tuż przy Dworcu Zachodnim



"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)