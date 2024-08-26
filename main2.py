# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Sheet2")
st.dataframe(data)
st.subheader("Project Health Check")
sql = """
SELECT
    "Project Name",
    "Task Name",
    "Assigned to",
    "Start Date",
    "End Date",
    "Days Required",
    "Progress"
FROM 
    Sheet2
ORDER BY
    "Progress" DESC;
"""

st.dataframe(conn.query(sql=sql))
