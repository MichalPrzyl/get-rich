import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
from utils import calculate_values_for_months

def draw_chart(start_date, end_date, income_outcome_data):
    # Konwersja stringów na obiekty datetime
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Tworzenie listy miesięcy w podanym zakresie dat
    months = pd.date_range(start=start_date, end=end_date, freq='MS')
    
    # Y asis data.
    y = calculate_values_for_months(months, income_outcome_data)

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(months, y, marker='o', linestyle='-', color='b')

    # Ustawienie lokalizatorów osi X, aby linie siatki były co miesiąc
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Główne linie siatki co miesiąc
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Ustawienie gęstszej skali na osi Y
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))

    # Włączenie poziomych linii siatki
    plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7)  # Siatka na obu osiach

    plt.title(f"Wykres od {start_date.strftime('%Y-%m-%d')} do {end_date.strftime('%Y-%m-%d')}")
    plt.xlabel("Miesiące")
    plt.ylabel("Wartość")
    plt.gcf().autofmt_xdate()  # Automatyczne formatowanie dat na osi X

    # Wyświetlanie wykresu w nowym oknie
    plt.show()
