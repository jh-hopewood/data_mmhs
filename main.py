import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("입력한 위치를 지도에 표시하기 (Folium)")

# 기본값: 하회마을 좌표
default_lat = 36.538167
default_lon = 128.518611

# 위도/경도 입력
lat = st.number_input('위도(Latitude)', value=default_lat, format="%.6f")
lon = st.number_input('경도(Longitude)', value=default_lon, format="%.6f")

# 지도 생성
m = folium.Map(location=[lat, lon], zoom_start=15)

# 마커 추가
folium.Marker(
    location=[lat, lon],
    popup=f"위치: ({lat}, {lon})",
    tooltip="여기에 마커!"
).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

# 하회마을 위치 정보 안내
st.info(f"안동 하회마을 위치: 위도 36.538167, 경도 128.518611")
