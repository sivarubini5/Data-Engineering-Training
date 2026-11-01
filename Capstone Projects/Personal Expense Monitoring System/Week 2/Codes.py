import pandas as pd
import numpy as np

df = pd.read_csv("expenses.csv")

df["amount"] = pd.to_numeric(
    df["amount"].astype(str).str.replace(r"[₹$,]", "", regex=True).str.strip(),
    errors="coerce",
)
iso = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
other = pd.to_datetime(df["date"], format="mixed", dayfirst=True, errors="coerce")
df["date"] = iso.fillna(other)
df["category"] = df["category"].str.strip().str.title()
df = df.dropna(subset=["amount", "date"])
df["month"] = df["date"].dt.to_period("M")

df.to_csv("cleaned_expenses.csv", index=False)

summary = []
for m in sorted(df["month"].unique()):
    amounts = df.loc[df["month"] == m, "amount"].to_numpy()
    summary.append({"month": str(m), "total": np.sum(amounts), "average": round(np.mean(amounts), 2)})
monthly_summary = pd.DataFrame(summary)
monthly_summary.to_csv("monthly_summary.csv", index=False)
print(monthly_summary)

monthly_expense = df.groupby(["month", "category"])["amount"].sum().unstack().fillna(0)
print(monthly_expense)