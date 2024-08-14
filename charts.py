import matplotlib.pyplot as plt

def draw_chart():
    # Przykładowe dane
    x = [1, 2, 3]
    y = [2, 3, 4]

    # Tworzenie wykresu
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("Przykładowy wykres")
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.grid(True)

    # Wyświetlanie wykresu w nowym oknie
    plt.show()
