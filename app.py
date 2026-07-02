import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=8)
plt.title("Sales Histogram")
plt.show()

plt.figure(figsize=(6,5))
sns.boxplot(y=df["Sales"])
plt.title("Sales Box Plot")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("Data Visualization Completed Successfully!")
