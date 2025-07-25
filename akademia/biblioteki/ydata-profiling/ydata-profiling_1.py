import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path

cwd = Path.cwd()
print(f'Current path is {cwd}')

hf_dir = cwd / 'akademia' / 'biblioteki' / 'ydata-profiling'

hm_2024_df = pd.read_csv(hf_dir / 'halfmarathon_wroclaw_2024__final.csv', sep=';')
hm_2023_df = pd.read_csv(hf_dir / 'halfmarathon_wroclaw_2023__final.csv', sep=';')

hm_2024_report = ProfileReport(hm_2024_df, title='Analiza danych z półmaratonu Wrocław 2024')
hm_2024_report.to_file(hf_dir / 'hm_2024_report.html')

hm_2023_report = ProfileReport(hm_2023_df, title='Analiza danych z półmaratonu Wrocław 2023')
hm_2023_report.to_file(hf_dir / 'hm_2023_report.html')

comparison_report = hm_2023_report.compare(hm_2024_report)
comparison_report.to_file(hf_dir / 'comparison_report.html')