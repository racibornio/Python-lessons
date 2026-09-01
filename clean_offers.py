import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
Product Owner poszukiwany 🕵🏻‍♀️
Cześć!😊

Jestem Rekruterką w firmie NATEK i szukam obecnie Product Ownera do projektu w bankowości, związanego z wdrożeniem nowego modułu aplikacji mobilnej do obsługi produktów inwestycyjnych.

Kluczowe wymagania:
• 8 lat doświadczenia na stanowisku Product Owner / Product Manager
• Doświadczenie w rozwoju aplikacji mobilnych
• Znajomość produktów inwestycyjnych lub rynku finansowego
• Doświadczenie w tworzeniu i realizacji roadmapy produktowej
• Umiejętność zarządzania backlogiem i priorytetyzacją
• Silne umiejętności analityczne i biznesowe
• Bardzo dobra znajomość języka angielskiego (C1+)

praca hybrydowa 2x w tygodniu (lub rzadziej - 1x na 2 tygodnie) z biura w Warszawie / Wrocławiu / Poznaniu 

stawka: b2b 1100 - 1250 zł netto / dzień
UoP: 17-18.500 zł brutto / miesiąc 

Jeśli projekt brzmi interesująco, proszę o wysłanie CV i chętnie umówię się na rozmowę o szczegółach 😊

Zuzanna Klatt
Junior IT Recruite
"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)