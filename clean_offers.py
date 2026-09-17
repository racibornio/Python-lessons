import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """






Szukam Business Analityka (4–6 lat doświadczenia, EN/FR, do 410 EUR MD) dla producenta dóbr luksusowych!
Dzień dobry Patryk, 

pozwoliłem sobie na kontakt, ponieważ szukam Business Analityka dla jednego z największych producentów dóbr luksusowych na świecie (fashion/jewelry/watches), do programu Retail Transformation (IT / Digital). Stawka do 410 EUR dziennie.

To stanowisko jest przeznaczone dla osoby z konkretnym doświadczeniem w branży dóbr luksusowych / retail oraz kilkuletnią praktyką w analizie biznesowej – klient oczekuje realnego backgroundu w pracy z markami luksusowymi lub dużym retail. 

Zakres roli / projekt:
• wsparcie Retail Transformation Program – analiza procesów sprzedaży, retail operations, omnichannel
• zbieranie i doprecyzowywanie wymagań biznesowych (workshopy, wywiady, dokumentacja)
• przygotowywanie user stories, use cases, specyfikacji funkcjonalnych dla zespołów IT / Digital
• współpraca z interesariuszami biznesowymi (Maisons, retail, e‑commerce) oraz zespołami technicznymi
• udział w projektowaniu i optymalizacji procesów retail / store / clienteling / omnichannel
• wsparcie w testach biznesowych (UAT), walidacja rozwiązań względem potrzeb biznesu 
Kluczowe oczekiwania:
• min. 4–6 lat doświadczenia jako Business Analyst w obszarze retail / dóbr luksusowych / e‑commerce
• praktyka w business analysis: zbieranie wymagań, mapowanie procesów (AS‑IS/TO‑BE), gap analysis
• bardzo dobre umiejętności komunikacji i pracy z interesariuszami (warsztaty, prezentacje, dokumentacja)
• doświadczenie w pracy w środowisku Agile (Scrum / Kanban)
• biegła znajomość języka angielskiego i francuskiego 

W przypadku zainteresowania proszę o aktualne CV lub numer telefonu do krótkiej rozmowy.
Będę też wdzięczny za polecenia Koleżanek i Kolegów z podobnym profilem.

Pozdrawiam/Best regards 
Dominik Buśkiewicz
Technical Recruiter
Phone: +48 795 670 470
dbuskiewicz@amaris.com



"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)