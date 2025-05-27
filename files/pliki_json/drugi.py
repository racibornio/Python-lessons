import json
import pandas as pd
from pathlib import Path

json_file_path = Path(__file__).parent / "drugi.json"

with open(json_file_path, 'r', encoding='utf-8') as f:
    data_file = json.load(f)


print(data_file)
print(len(data_file))

# with open(json_file_path, 'w') as f:
#     f.write(json.dumps(data, indent=4))