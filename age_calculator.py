import streamlit as st
from datetime import datetime

# Streamlit app title
st.title('Age Calculator')

# User input for date of birth
dob = st.date_input('Enter Date of Birth')

# Calculate age
if dob:
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Your age is: {age} years")
