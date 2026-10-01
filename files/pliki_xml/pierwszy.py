import pandas as pd
from pathlib import Path

# xml_file_path = Path(__file__).parent / 'pierwszy.xml'

# # with open('pierwszy.xml', 'r') as f:
# #     f.read

# print('Czy plik istnieje - ', xml_file_path.exists())

# df = pd.read_xml('pierwszy.xml')

cwd = Path.cwd()
print(f'Jesteśmy w {cwd}')
target_file_location = cwd / "files" / "pliki_xml" / "drugi.xml"

with open(target_file_location, 'w') as f:
    f.write("""
        <clients>
            <client>
                <name>John Doe</name>
                <age>25</age>
                <city>San Francisco</city>
            </client>
            <client>
                <name>Jane Doe</name>
                <age>22</age>
                <city>Los Angeles</city>
            </client>
        </clients>
    """)