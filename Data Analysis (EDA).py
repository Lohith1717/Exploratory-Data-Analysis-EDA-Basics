import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Load Dataset
# ==============================

df = pd.read_csv("matplotlib_practice_dataset.csv")

print("First 5 rows of dataset")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ==============================
# Pattern 1
# Temperature vs Ice Cream Sales
# ==============================

plt.scatter(df["Temperature_C"], df["IceCream_Sales"])

plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature (C)")
plt.ylabel("Ice Cream Sales")

plt.show()


# ==============================
# Pattern 2
# Visitors Trend Over Days
# ==============================

plt.plot(df["Day"], df["Visitors"], marker='o')

plt.title("Visitors Trend Over Days")
plt.xlabel("Day")
plt.ylabel("Number of Visitors")

plt.show()


# ==============================
# Pattern 3
# Cold Drink Sales Distribution
# ==============================

plt.hist(df["ColdDrink_Sales"], bins=10)

plt.title("Cold Drink Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()


# ==============================
# Pattern 4
# Rainfall vs Visitors
# ==============================

plt.scatter(df["Rainfall_mm"], df["Visitors"])

plt.title("Rainfall vs Visitors")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Visitors")

plt.show()