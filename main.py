import pandas as pd
import numpy as np
import streamlit as st
import Preprocessor
# Reading the data
df = pd.read_csv("data.csv")
# Creatiing time features
df = Preprocessor.fetch_time_features(df)
df['Financial_Year'] = df.apply(lambda x: f'{x['Year']} - {x['Year'] + 1}' if x['Month'] >= 4 else f'{x['Year'] - 1} - {x['Year']}', axis = 1)
# sidebar
st.sidebar.title("Filters")
selected_year = Preprocessor.multiselect('Select Year', df['Financial_Year'].unique())
selected_retailer = Preprocessor.multiselect('Select Retailer', df['Retailer'].unique())
selected_company = Preprocessor.multiselect('Select Company', df['Company'].unique())
selected_month = Preprocessor.multiselect('Select Month', df['Financial_Month'].unique())
filtered_df = df[(df['Financial_Year'].isin(selected_year)& df['Retailer'].isin(selected_retailer) & df['Company'].isin(selected_company) & df['Financial_Month'].isin(selected_month))]
st.title('Sales Dashboard')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label= 'Total Sales', value= int(filtered_df['Amount'].sum()))
with col2:
    st.metric(label= 'Total Margin', value= int(filtered_df['Margin'].sum()))
with col3:
    st.metric(label= 'Total Transactions', value= len(filtered_df['Margin']))
with col4:
    st.metric(label= 'Margin Percentage (in %)', value= int((filtered_df['Margin'].sum()/filtered_df['Amount'].sum())*100))
yearly_sales = filtered_df[['Financial_Year', 'Financial_Month','Amount']].groupby(['Financial_Year', 'Financial_Month']).sum().reset_index().pivot(index = 'Financial_Month', columns = 'Financial_Year', values = 'Amount')
st.line_chart(yearly_sales, x_label = 'Financial Month', y_label= 'Total Sales')

col5, col6 = st.columns(2)
#retailers revenue
with col5:
    st.title("Retailers count by revenue %")
    retailer_count = Preprocessor.fetch_top_revenue_retailers(filtered_df)
    retailer_count.set_index("percentage revenue", inplace = True)
    st.bar_chart(retailer_count, x_label = "percentage revenue",y_label = "retailer_count")

with col6:
    st.title("Companies count by revenue %")
    company_count = Preprocessor.fetch_top_revenue_companies(filtered_df)
    company_count.set_index("percentage revenue", inplace = True)
    st.bar_chart(company_count, x_label = "percentage revenue",y_label = "company_count")
    