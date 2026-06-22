import pandas as pd
import plotly.express as px

# Load cleaned dataset
df = pd.read_excel("output/Cleaned_Parking_Data.xlsx")

# -------------------------------
# Vehicle Type Distribution
# -------------------------------
fig1 = px.bar(
    df["Vehicle_Type"].value_counts().reset_index(),
    x="Vehicle_Type",
    y="count",
    title="Vehicle Type Distribution",
    labels={"Vehicle_Type": "Vehicle Type", "count": "Number of Vehicles"}
)

fig1.show()

# -------------------------------
# Payment Mode Distribution
# -------------------------------
fig2 = px.pie(
    df,
    names="Payment_Mode",
    title="Payment Mode Distribution"
)

fig2.show()

# -------------------------------
# Revenue by Vehicle Type
# -------------------------------
revenue = df.groupby("Vehicle_Type")["Fee_Rs"].sum().reset_index()

fig3 = px.bar(
    revenue,
    x="Vehicle_Type",
    y="Fee_Rs",
    title="Revenue by Vehicle Type"
)

fig3.show()

# -------------------------------
# Parking Duration Histogram
# -------------------------------
fig4 = px.histogram(
    df,
    x="Duration_Hours",
    nbins=10,
    title="Parking Duration Distribution"
)

fig4.show()