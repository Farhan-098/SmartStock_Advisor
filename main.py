import streamlit as st
from data_fetcher import fetch_stock_data
from predictor import predict
from plotter import plot_price

st.title("📊 SmartStock Advisor (Safe & Stable)")
st.write("Free live stock tracker that predicts **Buy / Hold / Sell** using Yahoo Finance data.")

stocks = st.text_input(
    "Enter stock symbols (comma-separated):",
    "AAPL,GOOG,MSFT,TSLA,AMZN"
)

stock_list = [s.strip().upper() for s in stocks.split(",")]
period = st.selectbox("Select time period:", ["1mo", "3mo", "6mo", "1y"], index=0)

if st.button("Fetch and Predict"):
    st.info("📡 Fetching live data and predicting... please wait ⏳")
    results = {}

    for stock in stock_list:
        try:
            df, error = fetch_stock_data(stock, period)

            if error:
                st.warning(error)
                continue

            change, decision, color = predict(df)
            results[stock] = {
                "change": change,
                "decision": decision,
                "color": color
            }

            fig = plot_price(df, stock)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error fetching {stock}: {e}")

    if results:
        st.subheader("📊 Predictions and Recommendations")

        for stock, info in results.items():
            st.markdown(
                f"**{stock}** → Predicted Change: **{info['change']}%** → "
                f"<span style='color:{info['color']}; font-weight:bold'>"
                f"{info['decision']}</span>",
                unsafe_allow_html=True
            )

        best_stock = max(results, key=lambda x: results[x]["change"])
        st.success(
            f"💡 Best BUY candidate: **{best_stock}** "
            f"({results[best_stock]['change']}%)"
        )
