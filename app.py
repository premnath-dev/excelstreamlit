import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Establish the Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from the Google Sheets worksheet "Sheet2"
data = conn.read(worksheet="Sheet2")

# Convert the data to a Pandas DataFrame for local manipulation
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.dataframe(df)

st.subheader("Project Health Check")

# Define a SQL query to retrieve and order data by progress
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

# Display the queried data
st.dataframe(conn.query(sql=sql))

# Add a divider for better separation of sections
st.divider()
st.write("CRUD Operations:")

# Implement CRUD Operations using buttons

# Create a new worksheet and insert the existing data
if st.button("New Worksheet"):
    conn.create(worksheet="Sheet2", data=df)
    st.success("Worksheet Created 🎉")

# Update the worksheet with the current data
if st.button("Update Worksheet"):
    conn.update(worksheet="Sheet2", data=df)
    st.success("Worksheet Updated 🤓")

# Clear the data in the worksheet
if st.button("Clear Worksheet"):
    conn.clear(worksheet="Sheet2")
    st.success("Worksheet Cleared 🧹")

# Additional operation: Calculate the sum of a column if needed
if st.button("Calculate Total Progress Sum"):
    sum_sql = 'SELECT SUM("Progress") as "TotalProgress" FROM Sheet2;'
    total_progress = conn.query(sql=sum_sql)
    st.dataframe(total_progress)
