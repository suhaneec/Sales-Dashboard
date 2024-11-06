import pandas as pd

# Fetching the date features
def fetch_time_features(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    # Financial month
    month_dict = {4:1,5:2,6:3,7:4,8:5,9:6,10:7,11:8,12:9,1:10,2:11,3:12}
    df["Financial_Month"] = df["Month"].map(month_dict)
    # Financial year
    df["Financial_Year"] = df.apply(lambda x: f"{x["Year"]} - {x["Year"]+1}" if x["Month"]>=4 else f"{x["Year"]-1} - {x["Year"]}", axis = 1)
    return df