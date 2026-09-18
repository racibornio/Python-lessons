import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """




Warszawa Kontrakt B2B PLN120 - PLN160 per hour praca zdalna

Updated on 04/09/2026

    Praca w 100% zdalna
    Umowa B2B via Michael Page

O naszym kliencie

Projekt realizowany jest dla międzynarodowej organizacji będącej dostawcą zaawansowanej infrastruktury i usług B2B dla instytucji finansowych, która rozwija globalne kompetencje w obszarze ServiceNow oraz transformacji procesów biznesowych.
Opis stanowiska

    Zbieranie, analiza oraz dokumentowanie wymagań biznesowych, funkcjonalnych i niefunkcjonalnych dla inicjatyw związanych z platformą ServiceNow.
    Prowadzenie warsztatów, sesji discovery oraz analiz procesów biznesowych.
    Wspieranie definiowania rozwiązań, zarządzania backlogiem oraz priorytetyzacji wymagań.
    Przekładanie potrzeb biznesowych na skalowalne rozwiązania i usprawnienia w platformie ServiceNow.
    Współpraca z architektami, deweloperami oraz właścicielami platformy przy projektowaniu i wdrażaniu rozwiązań.
    Przygotowywanie uzasadnień biznesowych, analiz wartości oraz oczekiwanych korzyści z realizowanych inicjatyw.
    Wspieranie rozwoju modelu operacyjnego ServiceNow oraz procesów governance.
    Udział w tworzeniu standardów, polityk, procedur i praktyk związanych z funkcjonowaniem platformy.
    Analiza i optymalizacja procesów IT oraz procesów biznesowych zgodnie z dobrymi praktykami ServiceNow.
    Identyfikowanie możliwości automatyzacji oraz inicjatyw zwiększających efektywność procesów.
    Wspieranie harmonizacji procesów pomiędzy różnymi jednostkami biznesowymi.
    Budowanie i utrzymywanie relacji z interesariuszami biznesowymi, zespołami technologicznymi oraz funkcjami wspierającymi.
    Facylitowanie procesu podejmowania decyzji i osiągania konsensusu pomiędzy zaangażowanymi stronami.
    Wsparcie działań związanych z gotowością operacyjną, przejęciem usług oraz przygotowaniem modelu wsparcia.
    Definiowanie wymagań dotyczących wsparcia biznesowego, KPI, SLA i procesów operacyjnych.
    Udział w testach, walidacji rozwiązań oraz odbiorach użytkowników biznesowych.
    Analiza wpływu biznesowego integracji pomiędzy ServiceNow a systemami wewnętrznymi i zewnętrznymi.
    Koordynacja zależności pomiędzy zespołami realizującymi inicjatywy integracyjne.
    Zapewnienie zgodności rozwiązań z wymaganiami architektonicznymi, bezpieczeństwa, ryzyka i compliance.
    Identyfikowanie oraz analiza przypadków użycia dla rozwiązań AI i inteligentnej automatyzacji procesów.
    Współtworzenie przyszłych procesów biznesowych wykorzystujących możliwości sztucznej inteligencji.



Profil kandydata

    Doświadczenie na stanowisku Business Analysta lub Business Solutions Analysta w środowisku ServiceNow.
    Znajomość języka angielskiego umożliwiająca swobodną konwersację (min. poziom C1)
    Praktyczna znajomość analizy biznesowej, zarządzania wymaganiami i modelowania procesów.
    Doświadczenie w prowadzeniu warsztatów oraz współpracy z interesariuszami biznesowymi i technicznymi.
    Umiejętność przekładania potrzeb biznesowych na rozwiązania systemowe i procesowe.
    Znajomość funkcjonowania platformy ServiceNow oraz projektów jej wdrażania i rozwoju.
    Doświadczenie w obszarze governance, zarządzania usługami lub transformacji procesów.
    Umiejętność pracy w złożonym środowisku organizacyjnym obejmującym wiele zespołów i obszarów biznesowych.
    Doświadczenie we współpracy z architektami, zespołami technicznymi oraz właścicielami procesów.
    Wysoko rozwinięte umiejętności komunikacyjne, analityczne i organizacyjne.
    Znajomość zagadnień związanych z integracjami systemowymi oraz zależnościami międzyplatformowymi.



Mile widziane

    Doświadczenie w budowie lub rozwijaniu modelu operacyjnego ServiceNow.
    Znajomość zagadnień związanych z architekturą korporacyjną, bezpieczeństwem i compliance.
    Udział w programach transformacyjnych realizowanych w dużych organizacjach.
    Doświadczenie związane z automatyzacją procesów oraz inicjatywami AI.
    Znajomość frameworków zarządzania usługami i procesami IT.

Oferujemy

    Stawka: 120 - 160 PLN netto/h B2B
    Start współpracy: 15.10.2026.
    Praca w 100% zdalna (jedynie pierwsze kilka dni pracy to warsztaty stacjonarne z całym zespołem w Warszawie)
    Kluczowa rola w strategicznym rozwoju platformy ServiceNow w międzynarodowym środowisku.
    Umowa B2B via Michael Page.

Kontakt
Olga Lefelbajn
Numer referencyjny
JN-092026-7095324
Szczegóły oferty

Sektor
    Informatyka

Obszar
    Analizy biznesowe

Branża
    Technology & Telecoms

Lokalizacja
    Warszawa

Rodzaj umowy
    Kontrakt B2B

Twoja aplikacja trafi do
    Olga Lefelbajn

Numer referencyjny
    JN-092026-7095324

System pracy
    praca zdalna



"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)