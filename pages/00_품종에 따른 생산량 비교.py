import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="품종별 생산량 분석", layout="wide")
st.title("🐟 품종별 생산량 데이터 분석")

# 📥 데이터 불러오기
@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRc25aFjQgue-LZpSD2-D34E1Rw2u2begSToFUevNfqINrf3Pb2ubFjVy0PJLHC1h6vLyFfD-YJeN3l/pub?gid=1788635662&single=true&output=csv"
    return pd.read_csv(url)

df = load_data()

# ========================================
# ✅ 1. 생산량 상위 Top10 막대그래프
# ========================================
st.subheader("📊 전체 품종 중 총 생산량 Top 10")

# 전체 품종 총 생산량 계산
총생산량_리스트 = []
for i, row in df.iterrows():
    품종 = row["품종"]
    생산량합 = row.iloc[2:].sum()  # 연도별 합계
    총생산량_리스트.append({"품종": 품종, "총생산량": 생산량합})

총생산량_df = pd.DataFrame(총생산량_리스트)
top10_df = 총생산량_df.sort_values(by="총생산량", ascending=False).head(10)

# 막대그래프 출력
fig_top10 = px.bar(top10_df, x="품종", y="총생산량", title="총 생산량 상위 10개 품종",
                   labels={"총생산량": "총합 (톤)"})
st.plotly_chart(fig_top10, use_container_width=True)

# ========================================
# ✅ 2. 품종별 연도별 변화 추이 그래프
# ========================================
st.subheader("📈 선택 품종의 연도별 생산량 추이")

# 품종 선택
품종목록 = df["품종"].unique().tolist()
선택한_품종들 = st.multiselect("🎯 분석할 품종 선택 (검색 가능)", 품종목록)

if 선택한_품종들:
    plot_df = pd.DataFrame()
    for 품종 in 선택한_품종들:
        행 = df[df["품종"] == 품종].iloc[0, 2:]
        년도 = 행.index.str.replace("년", "").astype(int)
        생산량 = 행.values
        tmp = pd.DataFrame({
            "연도": 년도,
            "생산량": 생산량,
            "품종": 품종
        })
        plot_df = pd.concat([plot_df, tmp], ignore_index=True)

    fig = px.line(plot_df, x="연도", y="생산량", color="품종", markers=True,
                  title="선택한 품종의 연도별 생산량 추이")
    fig.update_layout(xaxis=dict(dtick=1))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("✅ 하나 이상의 품종을 선택해 주세요.")
