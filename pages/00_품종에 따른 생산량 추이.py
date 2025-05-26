import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="생산량 추이 분석", layout="wide")
st.title("📈 품종별 연도별 생산량 비교")

@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRc25aFjQgue-LZpSD2-D34E1Rw2u2begSToFUevNfqINrf3Pb2ubFjVy0PJLHC1h6vLyFfD-YJeN3l/pub?gid=1788635662&single=true&output=csv"
    return pd.read_csv(url)

df = load_data()
품종목록 = df["품종"].unique().tolist()

# 검색어 필터링
검색어 = st.text_input("🔍 품종 이름 일부를 입력하세요", value="")
필터링된_품종 = [p for p in 품종목록 if 검색어 in p]

if 필터링된_품종:
    선택한_품종들 = st.multiselect("✅ 비교할 품종 선택", 필터링된_품종)

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
                      title="선택한 품종의 연도별 생산량 비교")
        fig.update_layout(xaxis=dict(dtick=1))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("✅ 하나 이상의 품종을 선택해 주세요.")
else:
    if 검색어:
        st.warning("⚠️ 일치하는 품종이 없습니다.")
