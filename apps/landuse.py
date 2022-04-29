import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    m = leafmap.Map()
    url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?"
    m.add_wms_layer(
        url,
        layers="NLCD_2016_Land_Cover_L48",
        name="NLCD 2016 CONUS Land Cover",
        format="image/png",
        transparent=True,
    )
    m.add_legend(builtin_legend='NLCD')
    m.to_streamlit(height=700)
