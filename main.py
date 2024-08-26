# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1ME1DnWT2QphPcgUvz8UNHjRVaLyDE1oxFu0jmXXN6Yc/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="1340638719") #""" usecols=list(range(2)), """ )
st.dataframe(data)
st.subheader("Project Health Check")
sql = """
SELECT
    "Project Name",
    "Task Name",
    "Progress"
FROM 
    Sheet2
ORDER BY
    CAST(REPLACE("Progress", '%', '') AS DECIMAL) DESC;
"""

st.dataframe(conn.query(spreadsheet=url, sql=sql))
