import streamlit as st
import pandas as pd
import datetime as dt

with st.sidebar:
    macro_eco_metric = st.radio(
        label="Chose the metric :",
        options=("CPI", "Mortgage_rate", "NASDAQ"),
        index=0
    )
    #date_slider = st.select_slider()
    st.text("You have selected : {}".format(macro_eco_metric))

# Read the data
def read_clean_df(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


df_eco = read_clean_df("data/US_macroeconomics.csv")

st.header("Dataframe")

st.dataframe(df_eco)

st.header("Line Chart to visualize indicators")

start_date = dt.datetime(1980,5,1)
end_date = dt.datetime(2022,5,1)

st.text(start_date)

slider_date = st.slider(
    label="Date Range :",
    min_value=start_date, 
    value=(start_date, end_date),
    max_value=end_date
)

df_eco_range = df_eco[df_eco["date"].between(slider_date[0], slider_date[1])]

st.line_chart(df_eco_range[["date", macro_eco_metric]].set_index("date"))
