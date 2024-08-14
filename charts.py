import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def draw_chart():
    # Obecna data
    today = datetime.today()

    # Tworzenie listy miesięcy na 3 lata do przodu
    months = pd.date_range(today, periods=36, freq='MS')  # MS oznacza początek miesiąca

    # Przykładowe dane na osi Y
    y = range(1, 37)  # Przykładowe dane od 1 do 36

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(months, y, marker='o', linestyle='-', color='b')

    # Formatowanie osi X, aby pokazywała miesiące
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Pokazuje co trzeci miesiąc

    plt.title("Wykres z miesiącami na osi X (3 lata do przodu)")
    plt.xlabel("Miesiące")
    plt.ylabel("Wartość")
    plt.grid(True)

    plt.gcf().autofmt_xdate()  # Automatyczne formatowanie dat na osi X

    # Wyświetlanie wykresu w nowym oknie
    plt.show()
