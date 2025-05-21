import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
df = pd.read_csv('Mammals.csv')

st.title("Mammals 데이터 분석: 사용자 선택형 그래프")

# 데이터 미리보기
st.subheader("포유류 데이터 미리보기")
st.dataframe(df)

# 수치형 컬럼만 추출 (산점도용)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# x축, y축 선택 위젯
st.subheader("그래프 축 선택")
x_axis = st.selectbox("X축으로 사용할 속성", options=numeric_cols, index=0)
y_axis = st.selectbox("Y축으로 사용할 속성", options=numeric_cols, index=1)

# 그래프 출력
st.subheader(f"{x_axis} vs. {y_axis} 산점도")
fig = px.scatter(
    df, x=x_axis, y=y_axis, text='Mammal',
    color='Diet', size='Mass (kg)',
    title=f"{x_axis}과(와) {y_axis} 관계 시각화"
)
fig.update_traces(textposition='top center')
st.plotly_chart(fig, use_container_width=True)
