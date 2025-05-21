import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
df = pd.read_csv("Mammals.csv")

# 타이틀
st.title("포유류 서식지별 속도 분포")

# 그래프 생성
fig = px.strip(
    df,
    x="Habitat",
    y="Speed (km/h)",
    color="Habitat",
    stripmode='overlay'
)
fig.update_traces(jitter=0.3, marker_size=10)

# 출력
st.plotly_chart(fig)
