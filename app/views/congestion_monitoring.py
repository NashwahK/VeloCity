import streamlit as st
import folium
from folium.plugins import HeatMap
import pandas as pd
from streamlit_folium import st_folium
from datetime import datetime, timedelta

def show_page():
    st.title("Interactive Traffic Congestion Heatmap")
    def generate_congestion_heatmap():
        data = pd.DataFrame({
            'latitude': [40.748817, 40.748217, 40.748617, 40.758817, 40.748917],
            'longitude': [-73.985428, -73.984428, -73.986428, -73.985928, -73.987428],
            'congestion_level': [3, 5, 1, 4, 2],
            'vehicle_count': [100, 250, 50, 180, 120], 
            'timestamp': [datetime.now() - timedelta(hours=i) for i in range(5)]  
        })

        st.sidebar.header("Filter by Time")
        time_options = ["Current Time", "1 Hour Ago", "2 Hours Ago", "3 Hours Ago", "4 Hours Ago"]
        selected_time = st.sidebar.selectbox("Select Time Frame", time_options)

        if selected_time != "Current Time":
            hours_ago = int(selected_time.split(" ")[0])
            selected_timestamp = datetime.now() - timedelta(hours=hours_ago)
            data = data[data['timestamp'] <= selected_timestamp]
        map_center = [40.748817, -73.985428]
        folium_map = folium.Map(location=map_center, zoom_start=13)

        heat_data = [[row['latitude'], row['longitude'], row['congestion_level']] for _, row in data.iterrows()]
        HeatMap(heat_data, min_opacity=0.2, max_val=5, radius=15, blur=25, gradient={
            0.0: 'green',
            0.5: 'yellow',
            1.0: 'red'
        }).add_to(folium_map)
        for _, row in data.iterrows():
            congestion_level = row['congestion_level']
            color = "red" if congestion_level >= 4 else "yellow" if congestion_level >= 2 else "green"
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=8,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                tooltip=f"Vehicle Count: {row['vehicle_count']}"
            ).add_to(folium_map)

        return folium_map
    folium_map = generate_congestion_heatmap()
    st_folium(folium_map, width=700, height=500)
