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
import matplotlib.pyplot as plt

class gasBillInfo(BaseModel):
    okres_rozliczeniowy_od: date
    okres_rozliczeniowy_do: date
    zuzycie_m3: float
    zuzycie_kWh: float
    do_zaplaty: float
    termin_platnosci: date



bill = gasBillInfo(
    okres_rozliczeniowy_od=date(2025, 1, 1),
    okres_rozliczeniowy_do=date(2025, 1, 31),
    zuzycie_m3=100.0,
    zuzycie_kWh=1000.0,
    do_zaplaty=1000.0,
    termin_platnosci=date(2025, 2, 15)
)

print(bill)



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


instructor_open_ai_client = instructor.from_openai(OpenAI(api_key=openai_key))

for image_path in RAW_DATA_PATH.glob('*.png'):
    print(f'Processing {image_path}')

    gas_bill = instructor_open_ai_client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=gasBillInfo,
        messages=[
            {
                "role" : "user",
                "content" : [
                    {
                        "type" : "text",
                        "text" : "Pobierz szczegóły rachunku za gaz"
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
    with open(PROCESSED_DATA_PATH / f"{image_path.stem}.json", "w") as f:
        f.write(gas_bill.model_dump_json())



# outcome to data frame
data = []
for json_path in PROCESSED_DATA_PATH.glob('*.json'):
    if "simple" in json_path.name:
        continue

    with open(json_path) as f:
        data.append(json.loads(f.read()))


df = pd.DataFrame(data)
print('The outcome data frame:')
print(df)
df.sort_values("termin_platnosci").plot(x="termin_platnosci", y="do_zaplaty", kind="bar")
plt.show()