import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

class InvestmentSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Symulacja Inwestora")
        
        # Etykiety
        tk.Label(root, text="Miesięczne wpływy:").grid(row=0, column=0)
        tk.Label(root, text="Miesięczne koszta:").grid(row=1, column=0)
        
        # Pola do wprowadzania danych
        self.entry_inflow = tk.Entry(root)
        self.entry_inflow.grid(row=0, column=1)
        
        self.entry_cost = tk.Entry(root)
        self.entry_cost.grid(row=1, column=1)
        
        # Przycisk do uruchomienia symulacji
        tk.Button(root, text="Symuluj", command=self.simulate).grid(row=2, columnspan=2)
        
    def simulate(self):
        try:
            inflow = float(self.entry_inflow.get())
            cost = float(self.entry_cost.get())
            monthly_balance = inflow - cost
            
            # Symulacja przez 20 lat (240 miesięcy)
            months = 240
            balance = [0]
            for month in range(1, months + 1):
                balance.append(balance[-1] + monthly_balance)
            
            self.show_results(balance)
        
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić poprawne wartości liczbowe.")

    def show_results(self, balance):
        # Tworzenie wykresu
        plt.figure(figsize=(10, 6))
        plt.plot(balance, label="Saldo konta")
        plt.title("Saldo konta przez 20 lat")
        plt.xlabel("Miesiąc")
        plt.ylabel("Saldo (PLN)")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentSimulator(root)
    root.mainloop()
