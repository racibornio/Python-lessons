import sqlite3
from pathlib import Path
import pandas as pd
import base64
from getpass import getpass
from datetime import date
import instructor
from pydantic import BaseModel
from openai import OpenAI


# expose the directory path
wd_path = Path.cwd() / "akademia" / "zadania" / "mod_5" / "zad_1"
print(f'Current path: {wd_path}')
print()
print('Folder content:')
print([p.name for p in wd_path.iterdir()])
print()


# 1st part
# connect to the first data source - the db named 'zad_domowe__clients.db' and its table named 'clients'
conn = sqlite3.connect(wd_path / 'zad_domowe__clients.db')
cur = conn.cursor()
table_as_is = cur.execute("""
SELECT * FROM clients LIMIT 10
""")

print('The table first 10 rows:')
print(table_as_is.fetchall())
print()


# put the table in a data frame
clients_df = pd.read_sql("SELECT * FROM clients", conn)
print('Data frame from the table:')
print(clients_df)
conn.close()
print('Connection closed.')
print()


# 2nd part
# open csv file
products_df = pd.read_csv(wd_path / "zad_domowe__products.csv", sep=";")
print('Data frame from the csv file:')
print(products_df)



# 3rd part
openai_key = getpass("Enter your OpenAI key:")
openai_client = OpenAI(api_key=openai_key)

class InvoiceInfoItem(BaseModel):
    description: str
    product_id: int
    quantity: int
    price: float


class InvoiceInfo(BaseModel):
    company_name: str
    customer_id: int
    customer_name: str
    invoice_number: int
    date: date
    items: list[InvoiceInfoItem]


instructor_openai_client = instructor.from_openai(OpenAI(api_key=openai_key))
orders = []
for image_path in sorted(wd_path.rglob("zad_domowe__invoice_*.png")):
    print(f"Processing {image_path}")
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')


    invoice_info = instructor_openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Jesteś pomocnym asystentem, który potrafi odczytywać dane z faktur i zwracać je w postaci struktury danych JSON.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Odczytaj dane z tej faktury i zwróć je jako strukturę InvoiceInfo.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_data}"
                        },
                    },
                ],
            },
        ],
        response_model=InvoiceInfo,
        max_tokens=2000,
    )


    invoice_data = invoice_info.model_dump()
    for item in invoice_data["items"]:
        order = {
            "company_name": invoice_data["company_name"],
            "customer_id": invoice_data["customer_id"],
            "customer_name": invoice_data["customer_name"],
            "invoice_number": invoice_data["invoice_number"],
            "date": invoice_data["date"],
            "description": item["description"],
            "product_id": item["product_id"],
            "quantity": item["quantity"],
            "price": item["price"],
        }
        orders.append(order)

orders_df = pd.DataFrame(orders)
print()
print("Orders data frame:")
print(orders_df)