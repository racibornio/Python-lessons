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

openai_key = getpass()
openai_client = OpenAI(api_key = openai_key)

RAW_DATA_PATH = Path('dane.gaz') / 'raw'
PROCESSED_DATA_PATH = Path('dane.gaz') / 'processed'