import pandas as pd
from pathlib import Path

json_file_path = Path(__file__).parent / "pierwszy.json"

initial_df = pd.read_json(json_file_path, convert_dates=['birthdate'])

initial_df[["model", "year"]] = pd.json_normalize(initial_df["car"])
initial_df = initial_df.drop(columns=['car'])
print(initial_df)