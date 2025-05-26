import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.features import CustomIcon

# CSV 불러오기
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTLDdqQiCnYKjmGeqpUKowalBQRjCZgR0PGrjZ6eVyTs6v2Z-NCzL88neYl-w1S_iuhRJgVOGAbwvnx/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

# 지도 중심 설정
center = [df["위도"].mean(), df["경도"].mean()]
m = folium.Map(location=center, zoom_start=8)

# 사용자 아이콘 경로
icon_path = "images/point.png"

# 마커 추가
for _, row in df.iterrows():
    icon = CustomIcon(
        icon_image=icon_path,
        icon_size=(30, 30)  # 아이콘 크기 조절
    )
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=row["갯벌명"],
        icon=icon
    ).add_to(m)

# 지도 표시
st.title("📍 우리나라 갯벌 위치")
st_folium(m, width=800, height=600)
