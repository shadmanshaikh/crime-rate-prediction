import streamlit as st
import folium as f
from folium import plugins
from folium.plugins import HeatMap
# import leafmap
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.write('## :rocket:Crime Hotspot Detection Using Geospatial Methods')

lats_long = ["long" , "lat"]
crimedf = pd.read_csv("crime.csv")

st.write(crimedf.head())

lats_longs_weight = list(map(list, zip(crimedf["lat"],
                          crimedf["long"]
                         )
               )
           )
# lats_longs_weight[:5]

# st.write(lats_longs_weight[:5])
m = leafmap.Map(zoom_start = 5, tiles="stamentoner")
m.add_heatmap(
        crimedf,
        latitude="lat",
        longitude="long",
        value="totalcrime",
        # name="Heat map",
        radius=20,
    )
m.to_streamlit(width=1000, height=500)