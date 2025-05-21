import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 불러오기
df = pd.read_csv('Mammals.csv')

st.title("Mammals 데이터 분석 및 시각화")

# 데이터 미리보기
st.subheader("포유류 데이터 미리보기")
st.dataframe(df)

# ---------------------- 필터링 -----------------------
st.subheader("필터링 조건 선택")

# 서식지(Habitat) 필터
habitat_options = df['Habitat'].unique().tolist()
selected_habitats = st.multiselect("서식지(Habitat) 선택", habitat_options, default=habitat_options)

# 식습관(Diet) 필터
diet_options = df['Diet'].unique().tolist()
selected_diets = st.multiselect("식습관(Diet) 선택", diet_options, default=diet_options)

# 수치형 범위 필터
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
num_filter_col = st.selectbox("범위 필터할 수치 속성 선택", options=numeric_cols, index=0)
min_val, max_val = float(df[num_filter_col].min()), float(df[num_filter_col].max())
selected_range = st.slider(
    f"{num_filter_col} 값 범위 선택", min_value=min_val, max_value=max_val,
    value=(min_val, max_val)
)

# 필터 적용
filtered_df = df[
    (df['Habitat'].isin(selected_habitats)) &
    (df['Diet'].isin(selected_diets)) &
    (df[num_filter_col] >= selected_range[0]) &
    (df[num_filter_col] <= selected_range[1])
]

st.markdown(f"**필터링 결과: {len(filtered_df)}종**")
st.dataframe(filtered_df)

# ---------------------- 그래프 -----------------------
st.subheader("산점도 그래프 그리기")

x_axis = st.selectbox("X축 선택", options=numeric_cols, index=0)
y_axis = st.selectbox("Y축 선택", options=numeric_cols, index=1)

if not filtered_df.empty:
    fig = px.scatter(
        filtered_df, x=x_axis, y=y_axis, text='Mammal',
        color='Diet', size='Mass (kg)',
        title=f"{x_axis} vs. {y_axis} (필터링 적용됨)"
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("조건에 맞는 데이터가 없습니다. 필터를 조정해 주세요.")
