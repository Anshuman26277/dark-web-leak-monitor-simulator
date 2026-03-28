history = []

from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load dataset
df = pd.read_csv("leaks_dataset.csv")

# Load ML model (keep for future use)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


# 🔹 Risk function
def calculate_risk(data_exposed):
    score = 0

    if "Password" in data_exposed:
        score += 30
    if "Phone" in data_exposed:
        score += 20
    if "Credit Card" in data_exposed:
        score += 50
    if "Full Identity" in data_exposed:
        score += 70

    return min(score, 100)


# 🔹 Recommendation function
def get_recommendation(threat):
    if threat == "High":
        return [
            "Change your password immediately",
            "Enable Two-Factor Authentication (2FA)",
            "Check bank and financial accounts",
            "Avoid using same password on multiple sites"
        ]

    elif threat == "Medium":
        return [
            "Update your password",
            "Enable 2FA",
            "Monitor your account activity"
        ]

    else:
        return [
            "No immediate action needed",
            "Stay alert and use strong passwords"
        ]


# 🔹 Main route
@app.route("/check", methods=["POST"])
def check():
    emails = request.form["email"].split(",")

    results = []

    # Clean dataset emails
    df["email"] = df["email"].str.strip().str.lower()

    for email in emails:
        email = email.strip().lower()
        history.append(email)

        result = df[df["email"] == email]

        if not result.empty:
            breach_count = len(result)
            records = result.to_dict(orient="records")

            for r in records:
                data_exposed = r.get("data_exposed", "")

                # 🔹 Risk score
                score = calculate_risk(data_exposed)
                r["breach_count"] = breach_count
                r["risk_score"] = score

                # ✅ FIXED THREAT (BASED ON SCORE)
                if score <= 30:
                    r["threat"] = "Low"
                elif score <= 70:
                    r["threat"] = "Medium"
                else:
                    r["threat"] = "High"

                # 🔹 Recommendations
                r["recommendation"] = get_recommendation(r["threat"])

            results.extend(records)

    if len(results) == 0:
        return render_template("result.html", status="safe")
    else:
        return render_template("result.html", status="breach", data=results)


@app.route("/history")
def show_history():
    return render_template("history.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)