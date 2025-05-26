import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="생산량 추이 분석", layout="wide")

# 제목
st.title("📈 품종별 연도별 생산량 추이")

# 데이터 로딩 함수
@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRc25aFjQgue-LZpSD2-D34E1Rw2u2begSToFUevNfqINrf3Pb2ubFjVy0PJLHC1h6vLyFfD-YJeN3l/pub?gid=1788635662&single=true&output=csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# 품종 선택
품종목록 = df["품종"].unique().tolist()

# 🔍 텍스트 입력으로 품종 필터링
검색어 = st.text_input("🔎 품종 이름 일부를 입력하세요", value="")
필터링된_품종 = [품종 for 품종 in 품종목록 if 검색어 in 품종]

if not 필터링된_품종:
    st.warning("일치하는 품종이 없습니다.")
else:
    선택한품종 = st.selectbox("✅ 품종 선택", 필터링된_품종)

# 해당 품종 데이터 추출
품종데이터 = df[df["품종"] == 선택한품종].iloc[0, 2:]  # 연도 컬럼만 추출

# 연도 및 생산량 데이터프레임 변환
년도 = 품종데이터.index.str.replace("년", "").astype(int)
생산량 = 품종데이터.values

plot_df = pd.DataFrame({
    "연도": 년도,
    "생산량": 생산량
})

# Plotly 그래프 출력
fig = px.line(plot_df, x="연도", y="생산량", markers=True, title=f"{선택한품종} 연도별 생산량")
fig.update_layout(xaxis=dict(dtick=1))  # 연도 간격 1년
st.plotly_chart(fig, use_container_width=True)
