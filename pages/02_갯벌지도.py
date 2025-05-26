import streamlit as st
import pandas as pd
import pydeck as pdk

# CSV 데이터 불러오기
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTLDdqQiCnYKjmGeqpUKowalBQRjCZgR0PGrjZ6eVyTs6v2Z-NCzL88neYl-w1S_iuhRJgVOGAbwvnx/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

st.title("📍 우리나라 갯벌 위치")

# Pydeck 차트 생성
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=df["위도"].mean(),
        longitude=df["경도"].mean(),
        zoom=7,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[경도, 위도]',
            get_radius=3000,
            get_fill_color='[0, 100, 200, 160]',
            pickable=True,
        ),
    ],
    tooltip={"text": "{갯벌명}"},
))
