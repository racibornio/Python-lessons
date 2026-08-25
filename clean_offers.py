import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
Cześć Patryku!
Czy interesuje Cię rola Business Data Analityka? Widzę, że obecnie działasz jako PO, więc stąd moje pytanie jakie kierunki bierzesz pod uwagę :) 
Zachęcam do zaaplikowania jeśli Cię interesuje temat analizy danych z biznesowym podejściem dla ekosystemu finansowego (są to spółki zajmujące się tematami paymentowami, finansowymi, troche krypto - projekt, który Daftcode zdecydował się rozwijać na ten moment troche bardziej niż stawianie nowych startupow :)) podrzucam link do formularza aplikacyjnego: https://daftcode.traffit.com/public/form/a/370?uid=17e82a21447bb0c4b2593e4de04eff364c62706e51584e6a4a6b6d58443775794a7642644d49786d30704a5044795a46
oczywiscie w razie pytań pisz śmiało :)
pzdr,
Eliza

Eliza Lesiak
HR Generalist || IT Recruiter || Emotionally Intelligent People Partner || Extended DISC® Consultant || Making work more human  
"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)