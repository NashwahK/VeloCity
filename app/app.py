import streamlit as st
from views import congestion_monitoring

st.set_page_config(page_title="VeloCity - Traffic Monitoring", layout="wide")
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Traffic Congestion Heatmap", "Data Visualization", "Traffic Signal Management"])

if page == "Traffic Congestion Heatmap":
    congestion_monitoring.show_page() 
elif page == "Data Visualization":
    st.title("Module 1")  
elif page == "Traffic Signal Management":
    st.title("Module 4")
