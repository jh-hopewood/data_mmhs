import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# CSV 데이터 불러오기
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTLDdqQiCnYKjmGeqpUKowalBQRjCZgR0PGrjZ6eVyTs6v2Z-NCzL88neYl-w1S_iuhRJgVOGAbwvnx/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

# 중심 좌표 설정 (임의로 첫 번째 갯벌로)
center = [df['위도'][0], df['경도'][0]]

# 지도 객체 생성
m = folium.Map(location=center, zoom_start=8)

# 각 지점 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=row["갯벌명"]
    ).add_to(m)

# Streamlit에 지도 표시
st.title("📍 우리나라 갯벌 위치")
st_data = st_folium(m, width=800, height=600)
