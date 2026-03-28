import pandas as pd

# load dataset
df = pd.read_csv("leaks_dataset.csv")

print("===== Cyber Leak Detection System =====")

email = input("Enter email to check breach: ")

result = df[df["email"] == email]

if result.empty:
    print("\nNo Breach Found. Your email is safe.")
else:
    print("\nALERT! Email Found in Data Breach!\n")
    
    for index, row in result.iterrows():
        print("Platform:", row["platform"])
        print("Leak Date:", row["leak_date"])
        print("Data Exposed:", row["data_exposed"])
        print("Risk Level:", row["risk_level"])
        print("Country:", row["country"])
        print("------------------------")