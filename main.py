import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
df = pd.read_csv("Mammals.csv")

st.title("Mammals 데이터 시각화 (범주형/수치형 자동 지원)")

# x, y 축 열 선택 (모든 열 포함)
all_cols = df.columns.tolist()
x_axis = st.selectbox("X축 선택", all_cols, index=0)
y_axis = st.selectbox("Y축 선택", all_cols, index=1)

# 그래프 타입 자동 결정
x_is_num = pd.api.types.is_numeric_dtype(df[x_axis])
y_is_num = pd.api.types.is_numeric_dtype(df[y_axis])

# 조건에 따른 그래프 그리기
if x_is_num and y_is_num:
    st.subheader("산점도 (Scatter)")
    fig = px.scatter(df, x=x_axis, y=y_axis, color="Diet", text="Mammal")
    fig.update_traces(textposition='top center')
elif not x_is_num and y_is_num:
    st.subheader("스트립 플롯 (Strip plot)")
    fig = px.strip(df, x=x_axis, y=y_axis, color="Habitat", stripmode="overlay")
    fig.update_traces(jitter=0.3, marker_size=10)
elif x_is_num and not y_is_num:
    st.subheader("수치형 → 범주형 스트립 플롯 (반대축)")
    fig = px.strip(df, x=y_axis, y=x_axis, color="Habitat", orientation="h", stripmode="overlay")
    fig.update_traces(jitter=0.3, marker_size=10)
else:
    st.subheader("두 범주형 변수 조합 빈도 막대그래프")
    count_df = df.groupby([x_axis, y_axis]).size().reset_index(name='count')
    fig = px.bar(count_df, x=x_axis, y='count', color=y_axis, barmode='group')

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
