import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_price(df, stock):
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(df.index, df["Close"], label="Close Price")

    ax.set_title(f"{stock} Price Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()

    # Format X-axis dates as DD-MM-YYYY
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()

    return fig
