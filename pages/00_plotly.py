import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="연령별 인구현황 시각화", layout="wide")

st.title("2024년 4월 연령별 인구현황 시각화")

# 파일 업로드
st.sidebar.header("CSV 파일 업로드")
file_mf = st.sidebar.file_uploader("남/여 인구 파일 업로드", type="csv")
file_total = st.sidebar.file_uploader("전체 인구 파일 업로드", type="csv")

# 데이터 불러오기
if file_mf and file_total:
    df_mf = pd.read_csv(file_mf, encoding="utf-8")
    df_total = pd.read_csv(file_total, encoding="utf-8")

    # 데이터 구조 확인 후 컬럼명 등 정제 필요할 수 있음
    st.subheader("원본 데이터 미리보기 (남/여)")
    st.dataframe(df_mf.head())

    st.subheader("원본 데이터 미리보기 (전체)")
    st.dataframe(df_total.head())

    # 예시: 남/여 인구 피라미드
    st.header("연령별 인구 피라미드 (남/여)")

    # 남/여 구분 및 연령대, 인구수 컬럼명 지정
    # 예시: "연령", "남자", "여자" 등
    # 아래 컬럼명은 실제 데이터에 맞게 변경 필요
    age_col = "연령"   # 또는 "나이"
    male_col = "남자"
    female_col = "여자"

    # 피라미드용 데이터 준비
    df_pyramid = df_mf[[age_col, male_col, female_col]].copy()
    df_pyramid[male_col] = df_pyramid[male_col] * -1  # 좌측: 남자, 우측: 여자

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df_pyramid[age_col],
        x=df_pyramid[male_col],
        name='남자',
        orientation='h'
    ))
    fig.add_trace(go.Bar(
        y=df_pyramid[age_col],
        x=df_pyramid[female_col],
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

    # 꺾은선 그래프: 연령별 전체 인구
    st.header("연령별 전체 인구 (꺾은선 그래프)")
    st.line_chart(df_total.set_index(age_col)["총인구수"])

else:
    st.info("좌측에서 남/여, 전체 인구 CSV 파일을 모두 업로드해주세요.")

