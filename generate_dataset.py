import pandas as pd
import random
from datetime import datetime, timedelta

country_data = {
    "India": {
        "first": ["Rohan", "Priya", "Aman", "Sneha", "Rahul", "Anjali"],
        "last": ["Sharma", "Verma", "Patel", "Gupta", "Singh", "Kumar"],
        "domains": ["gmail.com", "outlook.in", "yahoo.in"]
    },
    "USA": {
        "first": ["John", "Emily", "Michael", "Olivia", "David", "Sophia"],
        "last": ["Smith", "Johnson", "Williams", "Brown", "Davis", "Miller"],
        "domains": ["gmail.com", "yahoo.com", "outlook.com"]
    },
    "UK": {
        "first": ["Oliver", "Harry", "George", "Isla", "Amelia", "Jack"],
        "last": ["Taylor", "Wilson", "Evans", "Thomas", "Roberts", "Walker"],
        "domains": ["gmail.co.uk", "outlook.co.uk"]
    },
    "Germany": {
        "first": ["Lukas", "Leon", "Anna", "Emma", "Noah", "Mia"],
        "last": ["Müller", "Schneider", "Fischer", "Weber", "Meyer", "Wagner"],
        "domains": ["gmx.de", "web.de"]
    },
    "Canada": {
        "first": ["Liam", "Noah", "Emma", "Ava", "William", "Charlotte"],
        "last": ["Martin", "Lee", "Clark", "Lewis", "Walker", "Hall"],
        "domains": ["gmail.com", "outlook.ca"]
    },
    "Australia": {
        "first": ["Ethan", "Lucas", "Mason", "Grace", "Chloe", "Zoe"],
        "last": ["White", "Harris", "Martin", "Thompson", "Moore", "King"],
        "domains": ["gmail.com", "outlook.com.au"]
    }
}

platforms = [
    "Facebook", "Instagram", "LinkedIn", "Twitter",
    "Amazon", "Flipkart", "Netflix", "Paytm",
    "Snapchat", "Adobe", "Dropbox", "Yahoo"
]

data_types = [
    "Email+Password",
    "Email+Phone",
    "Email+Password+Phone",
    "Email+Credit Card",
    "Email+Address",
    "Full Identity Data"
]

risk_levels = ["Low", "Medium", "High"]

def random_date():
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)

data = []

for i in range(4000):
    country = random.choice(list(country_data.keys()))
    first = random.choice(country_data[country]["first"])
    last = random.choice(country_data[country]["last"])
    domain = random.choice(country_data[country]["domains"])

    email = f"{first.lower()}.{last.lower()}{random.randint(10,999)}@{domain}"
    platform = random.choice(platforms)
    leak_date = random_date().strftime("%Y-%m-%d")
    exposed = random.choice(data_types)
    risk = random.choice(risk_levels)

    data.append([email, platform, leak_date, exposed, risk, country])

df = pd.DataFrame(data, columns=[
    "email",
    "platform",
    "leak_date",
    "data_exposed",
    "risk_level",
    "country"
])

df.to_csv("leaks_dataset.csv", index=False)

print("Professional country-based dataset generated with 4000 rows!")