from faker import Faker
import pandas as pd
import random

fake = Faker()

print('Fake name:')
print(fake.name())
print()

print('Fake e-mail:')
print(fake.email())
print()

print('Fake address:')
print(fake.address())
print()

print('Fake text:')
print(fake.text())
print()

print('Fake text:')
print(fake.text(99))
print()

print('Fake phone number:')
print(fake.phone_number())
print()

print('Fake date of birth:')
print(fake.date_of_birth())
print()

print('Fake company name:')
print(fake.company())
print()

print('Fake job:')
print(fake.job())
print()

print('Fake credit card number:')
print(fake.credit_card_number())
print()

print('Fake iban:')
print(fake.iban())
print()

print('Methods containing "name":')
for attr in dir(fake):
    if "name" in attr:
        print(attr)


print()

# polish data
fake_pl = Faker('pl_PL')

print('Polish name:')
print(fake_pl.name())
print()

print('Polish address:')
print(fake_pl.address())
print()

# generate the same data set
Faker.seed(0)
print(fake_pl.name_male())
print()

# reset the above
Faker.seed()
print(fake_pl.name_male())
print()


# add data to the list
names_list = []

for dummy_entry in range(10):
    names_list.append(fake_pl.name())


for v in names_list:
    print(v)


print()
# or
names_list = [fake_pl.name_female() for _ in range(10)]


for v in names_list:
    print(v)


print()

# anonymize data
df = pd.DataFrame([
    {"name" : "John Doe", "email" : "john@real.com", "salary" : 560},
    {"name" : "Anna Smith", "email" : "anna@real.com", "salary" : 500},
    {"name" : "Will White", "email" : "will@real.com", "salary" : 450}
])

unique_emails_len = len(df['email'])
anonymized_emails = []

while len(anonymized_emails) < unique_emails_len:
    email = fake.email()
    if email not in anonymized_emails:
        anonymized_emails.append(email)


unique_names_len = len(df['name'])
anonymized_names = []
while len(anonymized_names) < unique_names_len:
    name = fake.name()
    if name not in anonymized_names:
        anonymized_names.append(name)


df['email'] = anonymized_emails
df['name'] = anonymized_names

print('New data frame with anonymized data:')
print(df)
print()


# generate data with false data
data = []
for i in range(1000):
    data.append({
        'Age' : random.randint(20, 100) if random.random() > 0.1 else None,
        'Name' : fake.first_name() + ' ' + fake.last_name() if random.random() > 0.1 else None,
        'Address' : fake.address() if random.random() > 0.1 else None,
        'Height' : random.randint(150, 200) if random.random() > 0.1 else None,
        'Weight' : random.randint(40, 110) if random.random() > 0.1 else None
    })


clients_df = pd.DataFrame(data)
print('New data frame with false data:')
print(clients_df)
print()



# generate random data do the data frame
data_to_df = {
    'name' : [fake.name() for _ in range(5)],
    'address' : [fake.address() for _ in range(5)],
    'email' : [fake.email() for _ in range(5)]
}

random_data_df = pd.DataFrame(data_to_df)
print('Data frame with totally random data:')
print(random_data_df)
print()


# a list of fake data
fake_data_list = []
for _ in range(5):
    fake_data_list.append(fake.name())


print('Random list with fake names:')
print(fake_data_list)
print()