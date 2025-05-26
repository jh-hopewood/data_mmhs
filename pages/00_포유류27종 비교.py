import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# 📁 데이터 파일 경로 설정
csv_path = Path(__file__).parent.parent / "data_set" / "Mammals.csv"
df = pd.read_csv(csv_path)

# 🏷️ 페이지 제목
st.title("🦣 Mammals 데이터 시각화 (범주형/수치형 자동 지원 + 동물 이름 표시)")

# 🔧 X축, Y축 선택
all_cols = df.columns.tolist()
x_axis = st.selectbox("X축 선택", all_cols, index=0)
y_axis = st.selectbox("Y축 선택", all_cols, index=1)

# 📌 그래프에 텍스트 표시 여부
show_text = st.checkbox("점 위에 동물 이름 항상 표시하기", value=False)

# 🔍 열 타입 판단
x_is_num = pd.api.types.is_numeric_dtype(df[x_axis])
y_is_num = pd.api.types.is_numeric_dtype(df[y_axis])

# 📌 선택된 축 정보 출력
st.markdown(f"✅ 선택된 X축: **{x_axis}** ({'수치형' if x_is_num else '범주형'})")
st.markdown(f"✅ 선택된 Y축: **{y_axis}** ({'수치형' if y_is_num else '범주형'})")

# 📊 그래프 공통 설정
common_args = {
    "hover_name": "Mammal",
    "title": f"{x_axis} vs. {y_axis} 시각화"
}

# 📉 그래프 그리기
if x_is_num and y_is_num:
    st.subheader("산점도 (Scatter)")
    fig = px.scatter(df, x=x_axis, y=y_axis, color="Diet", **common_args)

elif not x_is_num and y_is_num:
    st.subheader("스트립 플롯 (범주형 → 수치형)")
    fig = px.strip(df, x=x_axis, y=y_axis, color="Habitat", stripmode="overlay", **common_args)
    fig.update_traces(jitter=0.3, marker_size=10)

elif x_is_num and not y_is_num:
    st.subheader("스트립 플롯 (수치형 → 범주형)")
    fig = px.strip(df, x=y_axis, y=x_axis, color="Habitat", stripmode="overlay", orientation="h", **common_args)
    fig.update_traces(jitter=0.3, marker_size=10)

else:
    st.subheader("두 범주형 변수 조합 → 빈도 막대그래프")
    count_df = df.groupby([x_axis, y_axis]).size().reset_index(name="count")
    fig = px.bar(count_df, x=x_axis, y="count", color=y_axis, barmode="group", title="범주 조합 빈도")

# 🏷️ 텍스트 표시 (가능한 경우만)
if show_text and "Mammal" in df.columns:
    try:
        fig.update_traces(text=df["Mammal"], textposition='top center')
    except Exception:
        st.warning("⚠️ 이 그래프에서는 동물 이름을 점 위에 표시할 수 없습니다.")

# 📈 그래프 출력
st.plotly_chart(fig, use_container_width=True)
