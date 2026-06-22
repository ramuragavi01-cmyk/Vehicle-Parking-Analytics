import os
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("output/Cleaned_Parking_Data.xlsx")

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

# -------------------------------
# Chart 1 - Vehicle Type Distribution
# -------------------------------
plt.figure(figsize=(6,4))
df["Vehicle_Type"].value_counts().plot(kind="bar")
plt.title("Vehicle Type Distribution")
plt.xlabel("Vehicle Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/1_Vehicle_Type_Distribution.png")
plt.close()

# -------------------------------
# Chart 2 - Payment Mode
# -------------------------------
plt.figure(figsize=(6,6))
df["Payment_Mode"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Payment Mode Distribution")
plt.tight_layout()
plt.savefig("charts/2_Payment_Mode.png")
plt.close()

# -------------------------------
# Chart 3 - Revenue by Vehicle Type
# -------------------------------
plt.figure(figsize=(6,4))
df.groupby("Vehicle_Type")["Fee_Rs"].sum().plot(kind="bar")
plt.title("Revenue by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Revenue (Rs)")
plt.tight_layout()
plt.savefig("charts/3_Revenue_By_Vehicle.png")
plt.close()

# -------------------------------
# Chart 4 - Parking Duration Histogram
# -------------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Duration_Hours"], bins=10)
plt.title("Parking Duration Distribution")
plt.xlabel("Duration (Hours)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/4_Duration_Histogram.png")
plt.close()

# -------------------------------
# Chart 5 - Top Parking Slots
# -------------------------------
plt.figure(figsize=(8,4))
df["Parking_Slot"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Most Used Parking Slots")
plt.xlabel("Parking Slot")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/5_Top_Parking_Slots.png")
plt.close()

# -------------------------------
# Chart 6 - Status Distribution
# -------------------------------
plt.figure(figsize=(6,6))
df["Status"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Parking Status")
plt.tight_layout()
plt.savefig("charts/6_Status.png")
plt.close()

# -------------------------------
# Chart 7 - Daily Parking Trend
# -------------------------------
daily = df.groupby("Entry_Date").size()

plt.figure(figsize=(10,5))
daily.plot()
plt.title("Daily Parking Trend")
plt.xlabel("Date")
plt.ylabel("Vehicles")
plt.tight_layout()
plt.savefig("charts/7_Daily_Trend.png")
plt.close()

# -------------------------------
# Chart 8 - Parking Fee Distribution
# -------------------------------
plt.figure(figsize=(6,4))
plt.boxplot(df["Fee_Rs"])
plt.title("Parking Fee Distribution")
plt.ylabel("Fee (Rs)")
plt.tight_layout()
plt.savefig("charts/8_Fee_Boxplot.png")
plt.close()

# -------------------------------
# Chart 9 - Duration vs Fee
# -------------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Duration_Hours"], df["Fee_Rs"])
plt.title("Duration vs Parking Fee")
plt.xlabel("Duration (Hours)")
plt.ylabel("Fee (Rs)")
plt.tight_layout()
plt.savefig("charts/9_Duration_vs_Fee.png")
plt.close()

# -------------------------------
# Chart 10 - Revenue by Payment Mode
# -------------------------------
plt.figure(figsize=(6,4))
df.groupby("Payment_Mode")["Fee_Rs"].sum().plot(kind="bar")
plt.title("Revenue by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Revenue (Rs)")
plt.tight_layout()
plt.savefig("charts/10_Revenue_Payment_Mode.png")
plt.close()

print("="*50)
print("All charts generated successfully!")
print("Saved inside the 'charts' folder.")
print("="*50)