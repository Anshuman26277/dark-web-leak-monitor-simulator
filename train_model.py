import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
df = pd.read_csv("leaks_dataset.csv")

# Convert text to features
df["Password"] = df["data_exposed"].apply(lambda x: 1 if "Password" in x else 0)
df["Phone"] = df["data_exposed"].apply(lambda x: 1 if "Phone" in x else 0)
df["CreditCard"] = df["data_exposed"].apply(lambda x: 1 if "Credit Card" in x else 0)

# Target variable
df["target"] = df["risk_level"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Features & labels
X = df[["Password", "Phone", "CreditCard"]]
y = df["target"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")