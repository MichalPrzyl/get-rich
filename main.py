import json
import tkinter as tk


income_sources = []

def save_income_sources():
    with open("income_sources.json", "w") as file:
        json.dump(income_sources, file)

def load_income_sources():
    global income_sources
    with open("income_sources.json", "r") as file:
        income_sources = json.load(file)


# Income source template
# {
#     "name": "Pensja MP",
#     "amount": 100,
#     "start_date": "2021-01-01",
# }

def add_new_income(name, amount, start_dt, window):
    income_sources.append({
        "name": name,
        "amount": amount,
        "start_date": start_dt,
    })
    save_income_sources()
    window.destroy()

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj źródło przychodu")
    new_window.geometry("400x400")
    
    source_count = len(income_sources) + 1

    name_label = tk.Label(new_window, text=f"Nazwa źródła {source_count}:")
    name_label.pack()
    
    name_entry = tk.Entry(new_window, width=30)
    name_entry.pack()

    amount_label = tk.Label(new_window, text=f"Kwota źródła {source_count}:")
    amount_label.pack()
    
    amount_entry = tk.Entry(new_window, width=30)
    amount_entry.pack()

    start_date_label = tk.Label(new_window, text=f"Data rozpoczęcia źródła {source_count}:")
    start_date_label.pack()
    
    start_date_entry = tk.Entry(new_window, width=30)
    start_date_entry.pack()
    
    add_income_button = tk.Button(
        new_window, 
        text="Dodaj źródło przychodu1", 
        command=lambda: add_new_income(
            name_entry.get(), amount_entry.get(), start_date_entry.get(), new_window)
        )
    add_income_button.pack(side=tk.TOP, anchor="w", pady=0)

# Main app window.
root = tk.Tk()
root.title("GetRich")
root.geometry("400x400")
load_income_sources()
new_window_button = tk.Button(root, text="Dodaj źródło przychodu", command=open_new_window)
new_window_button.pack(side=tk.TOP, anchor="w", pady=0)

# Display income sources.
label = tk.Label(root, text="Źródła przychodu", font=("Helvetica", 16, "bold"))
label.pack(anchor='w')
for income_source in income_sources:
    src_income = tk.Label(root, text=f"{income_source['name']}: {income_source['amount']}")
    src_income.pack(anchor='w')

root.mainloop()
