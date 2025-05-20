import streamlit as st
import folium
from streamlit_folium import st_folium

# 안동 하회마을 위도, 경도
hahoemaeul = [36.538167, 128.518611]

st.title("안동 하회마을 위치 지도")

# Folium 지도 생성
m = folium.Map(location=hahoemaeul, zoom_start=15)

# 마커 추가
folium.Marker(
    location=hahoemaeul,
    popup="안동 하회마을",
    tooltip="안동 하회마을"
).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

