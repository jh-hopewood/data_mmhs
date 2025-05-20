import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, timedelta

# 시가총액 기준 글로벌 Top 5 기업 티커 (2024년 기준, 대표적)
top5_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 사우디 증권거래소
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL"
}

st.title("글로벌 시가총액 TOP 5 최근 1년 주가 변동")
st.write("데이터 소스: 야후파이낸스 (yfinance)")

# 최근 1년 날짜 계산
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Plotly 그래프 준비
fig = go.Figure()

for name, ticker in top5_tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        st.warning(f"{name}({ticker}) 데이터를 불러올 수 없습니다.")
        continue
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Close"],
        mode='lines',
        name=name
    ))

fig.update_layout(
    title="글로벌 시가총액 TOP 5 기업의 최근 1년간 주가 변화",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    legend_title="기업"
)

st.plotly_chart(fig, use_container_width=True)
