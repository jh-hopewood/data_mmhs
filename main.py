import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 읽기 (같은 폴더에 mammals.csv가 있어야 합니다)
df = pd.read_csv('Mammals.csv')

st.title("Mammals 데이터 분석 및 시각화")

# 데이터 미리보기
st.subheader("포유류 데이터 미리보기")
st.dataframe(df)

# 그래프 선택
st.subheader("그래프 그리기")
graph_type = st.selectbox("그래프 유형을 선택하세요", ['수명/속도 산점도', '키/몸무게 산점도', '식성별 평균 키 막대그래프'])

if graph_type == '수명/속도 산점도':
    fig = px.scatter(
        df, x='Speed (km/h)', y='LifeSpan (years)', text='Mammal',
        color='Diet', size='Mass (kg)',
        title='포유류 속도 vs. 수명 (식성, 몸무게별)'
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

elif graph_type == '키/몸무게 산점도':
    fig = px.scatter(
        df, x='Height (meters)', y='Mass (kg)', text='Mammal',
        color='Order',
        title='포유류 키 vs. 몸무게 (분류군별)'
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

elif graph_type == '식성별 평균 키 막대그래프':
    avg_height = df.groupby('Diet')['Height (meters)'].mean().reset_index()
    fig = px.bar(
        avg_height, x='Diet', y='Height (meters)',
        title='식성별 평균 키'
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("예시: csv 파일명은 'mammals.csv'로 저장해 주세요.")
