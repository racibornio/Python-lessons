from IPython.display import Markdown
import pandas as pd
from getpass import getpass
from openai import OpenAI
from pathlib import Path
import ast
import re

openai_key = getpass("Wprowadź swój klucz OpenAI:")

openai_client = OpenAI(api_key=openai_key)

current_location = Path.cwd()
print(f'Jesteśmy w: {current_location}')

df = pd.read_csv(current_location / 'akademia' / 'LLM_czyszczenie' / 'welcome_survey.csv')


def ASK(prompt: str) -> str:
    ASK_SENIOR_DATA_SCIENTIST_PROMPT = """
    - jeteś senior data scientist w dużym przedsiębiorstwie
    - Twoim zadaniem jest pomoc i mentorowanie młodszych pracowników - takich jak ja
    - będę Cię prosił o różne rady i wskazówki, które pomogą mi w mojej pracy
    - odpowiadaj zwięźle i jeżeli się da, to przesyłąj mi kod w Pythonie
    """

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role" : "system", "content" : ASK_SENIOR_DATA_SCIENTIST_PROMPT},
            {"role" : "user", "content" : prompt}
        ]
    )

    print(response.choices[0].message.content)

    #return Markdown(response.choices[0].message.content)
    return response.choices[0].message.content


print("Pięć pierwszych wierszy:")
print(df.head())

print()
df = df.rename(columns={
    'Wiek' : 'age',
    'Płeć' : 'gender',
    'Poziom wykształcenia' : 'edu_level',
    'Liczba lat doświadczenia zawodowego' : 'years_of_experience',
    'Obecna branża' : 'industry',
    'Jak preferujesz się uczyć? (wybierz wszystkie, które pasują)' : 'learning_preferences',
    'Ile czasu tygodniowo możesz poświęcić na naukę data science i AI?' : 'weekly_study_hours',
    'Co najbardziej motywuje Cię do nauki data science i AI? (wybierz maks. 3)' : 'motivation',
    'Jak zwierzęta są Twoimi ulubionymi?' : 'fav_animals',
    'Bardziej lubisz przysmaki słodkie czy słone?' : 'sweet_or_salty',
    'Jakie jest Twoje ulubione miejsce na ziemi?' : 'fav_place',
    'Jak spędzasz wolny czas?' : 'hobbies'
})

print("Pięć pierwszych wierszy po przezwaniu kolumn:")
print(df.head())
print()

print('Info:')
print(df.info())
print()

print('Unikaty:')
print(df.nunique())
print()


########################################### WIEK ###########################################
print('Zliczenie wieku:')
print(df['age'].value_counts())
df['age_cleaned'] = df['age'].map({
    "Poniżej 18 lat" : "<18",
    "18-24" : "18-24",
    "25-34" : "25-34",
    "35-44" : "35-44",
    "45-54" : "45-54",
    "55-64" : "55-64",
    "65 i więcej" : ">=65",
    "Nie chcę podawać" : "unknown"
})
df['age_cleaned'] = df['age_cleaned'].fillna("unknown")
print()
print('Zliczenie wieku po oczyszczeniu i do stringa:')
print(df['age_cleaned'].value_counts())
print()



########################################### PŁEĆ ###########################################
print('Zliczenie płci:')
print(df['gender'].value_counts())
print()
df['gender_cleaned'] = df['gender'].map({
    "Mężczyzna" : 0,
    "Kobieta" : 1
})
print("Zliczenie płci po oczyszczeniu:")
print(df['gender_cleaned'].value_counts())
print()



########################################### DOŚWIADCZENIE ###########################################
print("Zliczenie lat doświadczenia:")
print(df['years_of_experience'].value_counts())
print()
df['years_of_experience_cleaned'] = df['years_of_experience'].map({
    "0-2 lata" : "0-2",
    "3-5 lat" : "3-5",
    "6-10 lat" : "6-10",
    "11-15 lat" : "11-15",
    "16 i więcej" : ">=16"
})
print("Zliczenie lat doświadczenia po oczyszczeniu:")
print(df['years_of_experience_cleaned'].value_counts())
print()



########################################### HOBBY ###########################################
print("Zliczenie wolnego czasu:")
print(df['hobbies'].value_counts())
print()
print('Zsumowanie połączonych fraz:')
print(df['hobbies'].str.get_dummies(sep=", ").sum().sort_values(ascending=False))

def categorize_hobbies(hobbies):
    if not isinstance(hobbies, str):
        return[]
    
    cleaned = []
    for hobby in hobbies.split(", "):
        if hobby == "Filmy / Seriale":
            cleaned.append("hobby_movies")
        elif hobby == "Sport":
            cleaned.append("hobby_sport")
        elif hobby == "Książki":
            cleaned.append("hobby_books")
        elif hobby == "Gry komputerowe":
            cleaned.append("hobby_video_games")
        elif hobby == "Sztuka":
            cleaned.append("hobby_art")
        else:
            cleaned.append("hobby_other")

    return ", ".join(cleaned)


df['hobbies_cleaned'] = df['hobbies'].apply(categorize_hobbies)

print(df['hobbies_cleaned'].str.get_dummies(sep=", ").sum().sort_values(ascending=False))

hobbies_df = df['hobbies_cleaned'].str.get_dummies(sep=", ")
hobbies_df = hobbies_df.drop(columns=["[]"])
print("Nowy data frame po oczyszczeniu:")
print(hobbies_df)
print()

print("Połączone data framey:")
df = pd.concat([df, hobbies_df], axis=1)
print(df)
print()



########################################### SMAKI ###########################################
print("Przysmaki - zliczenie:")
print(df['sweet_or_salty'].value_counts())
df['sweet_or_salty_cleaned'] = df['sweet_or_salty'].map({
    "Słone" : "salty",
    "Słodkie" : "sweet"
})
print()
print("Przysmaki po czyszczeniu - zliczenie:")
print(df['sweet_or_salty_cleaned'].value_counts())
print()



########################################### ULUBIONE MIEJSCA ###########################################
print("Ulubione miejsce:")
print(df['fav_place'].value_counts())
print()
print(", ".join(df['fav_place'].dropna().unique().tolist()))

print()
print("Funkcja - START:")
print()
# ASK("""
# W kolumnie "Jakie jest Twoje ulubione miejsce na ziemi?' mam różńe wartości. Niektóry można by zgrupować w jedną kategorię, np. "Nad wodą", "W górach" etc.
#     Oto wartości:
#     Morze, Las, Góry, las i jezioro, Zielona oaza siedliskowa nad wodą., Miasto, ruch, spacer nad morzem, dom, we wszystkich miejscach czuje sie dobrze, Jezioro, Dom, Góry połączone z jeziorem, wieś, Morze Las , góry, morze, las, Teren nad rzeką , Albania , Mazury, Góry, Morze, Las, miejsca, gdzie jest mało ludzi, teren gdzie temperatura nie spada do 20 stopni, góry + zbiornik wodny (np. Jezioro Garda), Każde z powyższych, Wyspy / Ocean, Las i jezioro

#     Jak zgrupować te wartości do mniejszej liczby kategorii?
# """)
print()
print("Funkcja - END")
print()



########################################### WYKSZTAŁCENIE ###########################################
print("Poziom wykształcenia - zliczenie:")
print(df['edu_level'].value_counts())
print()
print('Ile unikatowych poziomów wykształcenia:')
print(len(df['edu_level'].dropna().unique()))
print()
print("Posklejaj unikatowe wartości dla poziomu wykształcenia:")
print(", ".join(df['edu_level'].dropna().unique().tolist()))
print()
print("Funkcja - START:")
print()
# ASK("""
# W kolumnie 'Poziom wykształcenia' mam różne wartości. Niektóre można by zgrupować w jedną kategorię, np. 'Podstawowe', 'Średnie' czy 'Wyższe'
#     Oto wartości w tej kolumnie:
#     Szkoła podstawowa, Szkoła średnia / Technikum, Magister, Inżynier, Doktorat, mgr inż., Licencjat, Studia podyplomowe, Szkoła zawodowa, inżynier, Inżynier , magister inżynier, W szkole doktorskiej, Inżynierskie + podyplomowe
#     Jak zgrupować te wartości w mniej kategorii?
# """)
print()
print("Funkcja - END")
print()



########################################### BRANŻA ###########################################
print("Zlicz Obecna branża:")
print(df['industry'].value_counts())
print()
print("Długość wszystkich wpisów dot. branży:")
print(len(df['industry'].dropna().unique()))
print("Branże do listy:")
print(", ".join(df['industry'].dropna().unique().tolist()))
print()
print("Funkcja - START:")
print()
# ASK("""
# Dla każdej z podanych nazw przypisz branżę:
#     IT, Edukacja, Energetyka, Automotvie, Automatyzacja, Energetyka zawodowa, Zdrowie, Kadry (HR), Marketing, Produkcja, Wellness, Chemia, Nieruchomości, poligrafia, Administracja publiczna, chemik branża automotive, usługi, obsługa klienta, brak, Budowlana, Automatyka i robotyka, Bezrobotny, Finanse, izynier GPS, Opieka, emeryt, Hotelarstwo, Budowa maszyn , energetyka, Logistyka, Branża Produkcyjno Usługowa , Motoryzacja, Media, fotografia, wideo dron, ..., Bez pracy, ostatnio HR, logistyka, zakupy w dystrybucji IT, R&D, przemysł - zarządzanie jakością, Inżyniera , Pracownik naukowy: Nawigacja samolotowa, systemy nawigacji satelitarnej, , administrator sieci i systemów w służbie zdrowia, FMCG , produkcja, fundusze europejskie, Administracja , Projektowanie mebli na wymiar, Logistyka , Ochrona Środowiska, Automotiv, Pomoc Społeczna (Asystent osobisty osoby z niepełnosprawnością), Zabezpieczenia transportowe, Logistyka i Produkcja, Transport, Property Management, księgowość, Bezpieczeństwo, Produkcja , Mechanik, Logistyka i Transport, handel, budownictwo/architektura, Usługi, Transport Międzynarodowy, Chłodnictwo, Marketing, SEO, logistyka, usługi elektryczne, Architektura/Urbansityka, Inżynieria, e-commerce, Budownictwo, fotowoltaika, Mechanik Samochodowy, Gastronomia, Pracuję przy projektach związanych z sieciami gazowymi, Spedycja
#     Odpowiedź zwróć jako słownik Pythona, gdzie kluczem jest podana przeze mnie nazwa, a wartością przypisana branża.
# """)
print()
print("Funkcja - END")
print()



########################################### ZWIERZĘ ########################################### 
print("Ulubione zwierzęta:")
print(df['fav_animals'].value_counts())
print()
print("Zlicz unikatowe:")
print(len(df['fav_animals'].dropna().unique()))

def categorize_animals(animal_name):
    if not isinstance(animal_name, str):
        return "Brak ulubionych"
    
    animal_name = animal_name.lower()
    if "Nie mam" in animal_name or "brak" in animal_name or "nie lubię" in animal_name:
        return "Brak ulubionych"
    elif "koty" in animal_name and "psy" in animal_name:
        return "Koty i Psy"
    elif "koty" in animal_name:
        return "Koty"
    elif "psy" in animal_name:
        return "Psy"
    else:
        return "Inne"
    

df['fav_animals_cleaned'] = df['fav_animals'].apply(categorize_animals)
print("Oczyszczone dane dot. zwięrząt:")
print(df['fav_animals_cleaned'])
print()
print("Zliczenie po oczyszczeniu:")
print(df['fav_animals_cleaned'].value_counts())
print()



########################################### UCZENIE SIĘ ###########################################
print("Zlicz dane nt. jak się uczysz:")
print(df['learning_preferences'].value_counts())

learning_pref_df = df['learning_preferences'].str.replace(", stacjonarnie", ", Kursy stacjonarne").str.get_dummies(sep=", ")
learning_pref_df = learning_pref_df.rename(columns={
    "Książki" : "learning_pref_books",
    "Kursy online" : "learning_pref_online_courses",
    "Kursy stacjonarne" : "learning_pref_offline_courses",
    "Praca z ChatGPT" : "learning_pref_chatgpt",
    "Praca zespołowa" : "learning_pref_teamwork",
    "Samodzielne projekty" : "learning_pref_personal_projects",
    "Uczenie innych osób" : "learning_pref_teaching",
    "Warsztaty" : "learning_pref_workshops"
})
df = pd.concat([df, learning_pref_df], axis=1)
print()
print("Dane po oczyszczeniu:")
print(df.head())
print()



########################################### MOTYWACJA ###########################################
print('Co Cię motywuje:')
print(df['motivation'].str.get_dummies(sep=", ").columns.tolist())
values = df['motivation'].str.get_dummies(sep=", ").columns.tolist()
print(",".join(values))

response_text = ASK("""
W kolumnie 'Co najbardziej motywuje Cię do nauki data science i AI' ma różne wartości. Niektóre można by zgrupować w jedną kategorię.
    Oto wartości w tej kolumnie:
    'Chęć zmiany zawodu', 'Dodanie kompetencji Data Science do obecnego profilu IT', 'Fascynacja możliwościami jakie daje nam AI', 'Pasja do analizy danych', 'Pomoc w realizacji swoich pomysłów', 'Rozwiązywanie rzeczywistych problemów', 'Rozwój kariery', 'Swoboda pracy', 'Wynagrodzenie', 'Wyzwania intelektualne', 'Zagadnienia w doktoracie', 'jako dźwigni zwiększającej mój projektowy zasięg (getting out of the box).', 'możliwośc tworzenia narzędzi AI', 'możliwość pracy zdalnej', 'odnalezieniesię na rynku pracy  ', 'pasja do AI', 'poznawanie nowych rzeczy', 'praca z AI', 'praca zdalna', 'rozwój osobisty', 'tworzenie aplikacji AI', 'własny projekt', 'zdobycie nowych umiejętności', 'znalezienie właściwej dla siebie drogi dla zmiany sytuacji zawodowej'
    Jak zgrupować te wartości w mniej kategorii? Stwórz słownik Pythona, gdzie kluczem jest podana przeze mnie nazwa, a wartością przypisana motywacja.
""")


# wyciągnięce danych ze słownika
match = re.search(r"\{[\s\S]+\}", response_text)

if match:
    motywacje = ast.literal_eval(match.group())
else:
    raise ValueError("Nie znaleziono słownika motywacji w odpowiedzi.")



# poniższa funkcja nie zadziała - w programie nie jest zapisywany słownik wynikowy
def categorize_motivation(motivation):
    if not isinstance(motivation, str):
        return[]
    
    cleaned_motivation = []
    for key, value in motywacje.items():
        for value in values:
            if value in motivation:
                cleaned_motivation.append(key)

    return ", ".join(cleaned_motivation)


df['motivation_cleaned'] = df['motivation'].apply(categorize_motivation)
motivations_df = df['motivation_cleaned'].str.get_dummies(sep=", ")
motivations_df = motivations_df.drop(columns=["[]"])
print()
print("Początek tabeli po oczyszczeniu:")
print(motivations_df.head())
print()
df = pd.concat([df, motivations_df], axis=1)
print('Po złączeniu w pierwotnym data framem:')
print(df)
print()
print("Kolumny z nowego:")
print(df.columns)


# dynamicznie pobierz kolumny z motywacji
motivation_columns = list(motywacje.keys())

cleaned_df = df[[
    'age',
    'gender',
    'edu_level',
    'years_of_experience',
    'industry',
    'learning_preferences',
    'weekly_study_hours',
    'motivation',
    'fav_animals',
    'sweet_or_salty',
    'fav_place',
    'hobbies',
    'age_cleaned',
    'gender_cleaned',
    'years_of_experience_cleaned',
    'hobbies_cleaned',
    'hobby_art',
    'hobby_books',
    'hobby_movies',
    'hobby_other',
    'hobby_sport',
    'hobby_video_games',
    'sweet_or_salty_cleaned',
    'fav_animals_cleaned',
    'learning_pref_books',
    'learning_pref_online_courses',
    'learning_pref_offline_courses',
    'learning_pref_chatgpt',
    'learning_pref_teamwork',
    'learning_pref_personal_projects',
    'Uczenie innych osób.',
    'learning_pref_workshops',
    'motivation_cleaned',
] + motivation_columns].copy()


print()
print('Ostateczny data frame: - pierwszych pięć wierszy:')
print(cleaned_df.head())

# zrzut to pliku csv
cleaned_df.to_csv(current_location / 'akademia' / 'LLM_czyszczenie' /  'Welcome_survey_cleaner_2025_06_05.csv', index=False, sep=";")