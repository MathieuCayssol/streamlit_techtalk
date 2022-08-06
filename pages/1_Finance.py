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

st.text(type(df_eco["date"][0]))

st.header("Dataframe")

st.dataframe(df_eco)

st.header("Line Chart to visualize indicators")

start_date = pd.Timestamp(year=1980, month=1, day=1)
end_date = pd.Timestamp(year=2022,month=5, day=1)

st.text(start_date)

"""st.slider(
    label="Date Range :",
    min_value=start_date, 
    value=end_date,
    max_value=end_date
)"""

st.line_chart(df_eco[["date", macro_eco_metric]].set_index("date"))
