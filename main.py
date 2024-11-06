import pandas as pd
import numpy as np
import streamlit as st
import Preprocessor

# Reading the data
df = pd.read_csv("data.csv")

# Creatiing time features
df = Preprocessor.fetch_time_features(df)

# sidebar
st.sidebar.title("Filters")



# Financial Year Filter
selected_year=st.sidebar.multiselect("Select Financial Year",df["Financial_Year"].unique())
st.text(selected_year)

unique_year=df["Financial_Year"].unique()
year_checkbox=st.checkbox("Select All",value=False)
if year_checkbox==True:
    year_selected=unique_year
else:
    year_selected=selected_year
st.text(year_selected)
# # Retailer Filter
# st.sidebar.multiselect("Select Retailer",df["Retailer"].unique())
# # Company Filter
# st.sidebar.multiselect("Select Company",df["Company"].unique())
# # Financial month filter
# st.sidebar.multiselect("Select Finacial Month",df["Financial_Month"].unique())

