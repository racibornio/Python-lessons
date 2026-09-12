import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """




B2B | Zdalnie | QA Lead z WMS Manhattan
Cześć Patryk,

Tu Eliza z emagine. 
Chciałam zapytać, czy rozważasz obecnie nowe możliwości zawodowe.

Jeden z naszych klientów poszukuje Test Managera / QA Leada z doświadczeniem w Manhattan Active WMS. To dość niszowy profil, dlatego szukamy osoby, która dobrze odnajdzie się w roli o charakterze bardziej liderskim i koordynacyjnym niż hands-on.

Poniżej przesyłam szczegóły:
Kontrakt: B2B, pierwsza umowa na 12 miesięcy z możliwością przedłużenia.
Stawka: Jesteśmy otwarci na Twoje oczekiwania finansowe.
Model pracy: Pełny etat, 100% zdalnie.

Na czym polega rola?
Osoba na tym stanowisku będzie odpowiedzialna za zarządzanie testami w ramach trójstronnej integracji pomiędzy Foot Locker, Manhattan Associates oraz systemem CiCT.
Zakres obejmuje definiowanie strategii testów, przygotowanie planów testowych i kryteriów wejścia/wyjścia, prowadzenie SIT, UAT, regression, cutover i hypercare, koordynację działań pomiędzy biznesem, IT i dostawcami, prowadzenie defect triage oraz raportowanie statusu testów do kierownictwa projektu.

Główne obowiązki:
Definiowanie i wdrażanie strategii testów dla integracji Manhattan WMS. 
Przygotowanie planów testowych z jasno określonymi kryteriami wejścia i wyjścia. 
Koordynacja faz SIT, UAT, regression i hypercare. 
Prowadzenie procesu defect triage oraz raportowanie statusu testów do liderów projektu. 
Nadzór nad współpracą interesariuszy i governance jakości. 

Kluczowe wymagania:
Duże doświadczenie w testowaniu Manhattan WMS. 
Szersze doświadczenie w testach integracyjnych WMS / supply chain. 
Umiejętność zarządzania governance i współpracy z interesariuszami. 
Doświadczenie w testach funkcjonalnych i wydajnościowych. 

Czy taka rola mogłaby Cię zainteresować?

Jeśli tak, chętnie porozmawiam o szczegółach. Możesz przesłać mi CV w odpowiedzi na tę wiadomość.

Pozdrawiam!

Eliza Danda
IT Recruiter @ emagine | Looking for a job? I’m hiring!


"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)