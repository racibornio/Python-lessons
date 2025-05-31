from IPython.display import Markdown
import pandas as pd
from getpass import getpass
from openai import OpenAI

openai_key = getpass("Entery key:")

openai_client = OpenAI(api_key=openai_key)

def ASK(prompt: str):
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

    print(response)

    return Markdown(response.choices[0].message.content)



ASK("Jakie sortowania można zrobić na obiekcie Data Frame?")