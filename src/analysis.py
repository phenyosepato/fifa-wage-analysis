import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/fifaplayers/players_22.csv", low_memory=False)

columns_needed = [
    "short_name",
    "age",
    "overall",
    "potential",
    "club_name",
    "value_eur",
    "wage_eur",
    "player_positions"
]

df = df[columns_needed]

# Check missing values
print(df.isnull().sum())

df = df.dropna()

print("Remaining rows:", len(df))

correlation = df["overall"].corr(df["wage_eur"])
print("Correlation between overall rating and wage:", correlation)

plt.figure()
plt.scatter(df["overall"], df["wage_eur"])
plt.xlabel("Overall Rating")
plt.ylabel("Weekly Wage (EUR)")
plt.title("Player Rating vs Wage")
plt.show()

plt.savefig("../images/wage_vs_rating.png")

plt.show()