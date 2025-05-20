import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 글로벌 시가총액 TOP5 미국기업(2024)
top5_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN"
}

st.title("글로벌 시가총액 TOP 5 최근 1년 주가 변동")
st.write("데이터 소스: 야후파이낸스 (yfinance)")

end_date = datetime.today() + timedelta(days=1)
start_date = end_date - timedelta(days=365)

fig = go.Figure()

for name, ticker in top5_tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty or len(data) < 10:
        st.warning(f"{name}({ticker}) 데이터가 없습니다.")
        continue
    st.write(f"{name} ({ticker}) 데이터 예시:", data.head())  # 불러온 데이터 일부 확인용
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
