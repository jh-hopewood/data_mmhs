import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="연령별 인구현황 시각화", layout="wide")
st.title("2024년 4월 연령별 인구현황 시각화")

# 파일 이름(같은 폴더에 두어야 함)
남여파일 = '202504_202504_연령별인구현황_월간_남여.csv'
전체파일 = '202504_202504_연령별인구현황_월간_계.csv'

# 한글 인코딩으로 파일 읽기 (깨질 경우 cp949로 변경)
try:
    df_mf = pd.read_csv(남여파일, encoding="utf-8-sig")
    df_total = pd.read_csv(전체파일, encoding="utf-8-sig")
except:
    df_mf = pd.read_csv(남여파일, encoding="cp949")
    df_total = pd.read_csv(전체파일, encoding="cp949")

st.subheader("남/여 인구 데이터 미리보기")
st.dataframe(df_mf.head())

st.subheader("전체 인구 데이터 미리보기")
st.dataframe(df_total.head())

# --- 연령별 인구 피라미드(남/여) ---
st.header("연령별 인구 피라미드 (남/여)")

# CSV 컬럼명에 맞게 수정(아래는 예시, 필요시 미리보기로 확인)
연령컬럼 = "연령"
남자컬럼 = "남자"
여자컬럼 = "여자"

df_pyramid = df_mf[[연령컬럼, 남자컬럼, 여자컬럼]].copy()
df_pyramid = df_pyramid.sort_values(by=연령컬럼)
df_pyramid[남자컬럼] = df_pyramid[남자컬럼] * -1

fig = go.Figure()
fig.add_trace(go.Bar(
    y=df_pyramid[연령컬럼],
    x=df_pyramid[남자컬럼],
    name='남자',
    orientation='h'
))
fig.add_trace(go.Bar(
    y=df_pyramid[연령컬럼],
    x=df_pyramid[여자컬럼],
    name='여자',
    orientation='h'
))
fig.update_layout(
    barmode='relative',
    title='연령별 인구 피라미드 (2024.04)',
    xaxis=dict(title='인구수'),
    yaxis=dict(title='연령'),
    height=700
)
st.plotly_chart(fig, use_container_width=True)

# --- 연령별 전체 인구(꺾은선 그래프) ---
st.header("연령별 전체 인구 (꺾은선 그래프)")

전체_연령컬럼 = "연령"
전체_총인구수 = "총인구수"

df_total = df_total.sort_values(by=전체_연령컬럼)
st.line_chart(df_total.set_index(전체_연령컬럼)[전체_총인구수])
