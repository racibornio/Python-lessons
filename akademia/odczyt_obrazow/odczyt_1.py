from pydantic import BaseModel
from datetime import date
import json
from pathlib import Path
import base64
from getpass import getpass
from IPython.display import Image
import instructor
from openai import OpenAI
import pandas as pd
import os
from PIL import Image as PILImage



# upload file, analyze and save result in JSON file

current_location = os.getcwd()
print(f'Current location is {current_location}')

openai_key = getpass()
openai_client = OpenAI(api_key = openai_key)

RAW_DATA_PATH = Path('akademia/odczyt_obrazow/dane_gaz/raw')
PROCESSED_DATA_PATH = Path('akademia/odczyt_obrazow/dane_gaz/processed')

print(f'RAW_DATA points to {RAW_DATA_PATH.resolve()}')

for image_path in RAW_DATA_PATH.glob('*.png'):
    print(image_path)


# Image(RAW_DATA_PATH / 'gaz_2023_12.png')
# img = PILImage.open(RAW_DATA_PATH / 'gaz_2023_12.png')
# img.show()

image_path = RAW_DATA_PATH / 'gaz_2023_12.png'

with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')


print(image_data[:100])

def prepare_image_for_open_ai(image_path):
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    return f"data:image/png;base64, {image_data}"


prepare_image_for_open_ai(image_path)


for image_path in RAW_DATA_PATH.glob("*.png"):
    print(f'Processing {image_path}')

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role" : "user",
                "content" : [
                    {
                        "type" : "text",
                        "text" : """
wyciągnij wszystkie informacje zawarte na fakturze.
Dane przedstaw w formacie JSON.
Oczekuję następujących informacji:
{
    "razem_sprzedaz_okres_rozliczeniowy_data_od" : ...,
    "razem_sprzedaz_okres_rozliczeniowy_data_do" : ...,
    "zuzycie_m3": ...,
    "zuzycie_kWh": ...,
    "do_zaplaty": ...,
    "termin_platnosci" : ...
}
tylko dane jako JSON, bez żadnych komentarzy.
"""
                    },
                    {
                        "type" : "image_url",
                        "image_url" : {
                            "url" : prepare_image_for_open_ai(image_path),
                            "detail" : "high"
                        }
                    }
                ]
            }
        ]
    )

    
result = response.choices[0].message.content.replace("```jwon", "").replace("```", "").strip()
with open(PROCESSED_DATA_PATH / f"{image_path.stem}__simple.json", "w") as f:
    f.write(result)


print(response.choices[0].message.content)