import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CSV 파일 불러오기
df = pd.read_csv('Mammals.csv')

st.title("Mammals 데이터 분석: 사용자 선택형 그래프")

# 데이터 미리보기
st.subheader("포유류 데이터 미리보기")
st.dataframe(df)
