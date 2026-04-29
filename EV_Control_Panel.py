import streamlit as st
from utils import set_bg_and_glass, glass_open, glass_close

set_bg_and_glass(r"C:\Users\HP\OneDrive\Desktop\programs\Project FY\assets\03_bg.jpg")

#st.markdown(glass_open(), unsafe_allow_html=True)
st.set_page_config(page_title="EV Control Panel",page_icon="⚡",
    layout="wide")
st.sidebar.title("EV Control Panel")


st.set_page_config(page_title="EV Charging System", layout="wide")



#st.markdown(glass_open(), unsafe_allow_html=True)

st.title("⚡ EV Charging Demand Prediction System")
st.markdown("""
###  Welcome to Smart EV Infrastructure Dashboard

This system provides:
- Charging demand prediction
- Cost and charging time estimation
- Queue waiting time analysis
- Station map visualization
- Decision support alerts
""")

st.info("👈 Open the sidebar and select a dashboard.")

#

