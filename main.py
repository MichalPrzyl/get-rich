import json
import tkinter as tk


income_sources = []
outcome_sources = []

def save_income_sources():
    with open("income_sources.json", "w") as file:
        json.dump(income_sources, file)

def load_income_sources():
    global income_sources
    with open("income_sources.json", "r") as file:
        income_sources = json.load(file)

def save_outcome_sources():
    with open("outcome_sources.json", "w") as file:
        json.dump(outcome_sources, file)

def load_outcome_sources():
    global outcome_sources
    with open("outcome_sources.json", "r") as file:
        outcome_sources = json.load(file)


# Income source template
# {
#     "name": "Pensja MP",
#     "amount": 100,
#     "start_date": "2021-01-01",
# }

def refresh_sources():
# Clear all existing income source widgets
    for widget in root.winfo_children():
        # if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
        widget.destroy()

def delete_income(index):
    del income_sources[index]
    save_income_sources()
    refresh_sources()
    display_all()

def delete_outcome(index):
    del outcome_sources[index]
    save_outcome_sources()
    refresh_sources()
    display_all()

def add_new_income(name, amount, start_dt, window):
    income_sources.append({
        "name": name,
        "amount": amount,
        "start_date": start_dt,
    })
    save_income_sources()
    refresh_sources()
    display_all()
    window.destroy()

def add_new_outcome(name, amount, start_dt, window):
    outcome_sources.append({
        "name": name,
        "amount": amount,
        "start_date": start_dt,
    })
    save_outcome_sources()
    refresh_sources()
    display_all()
    window.destroy()

def open_new_source_income_window():
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

def open_new_source_outcome_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj źródło rozchodu")
    new_window.geometry("400x400")
    
    source_count = len(outcome_sources) + 1

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
    
    add_outcome_button = tk.Button(
        new_window, 
        text="Dodaj źródło przychodu1", 
        command=lambda: add_new_outcome(
            name_entry.get(), amount_entry.get(), start_date_entry.get(), new_window)
        )
    add_outcome_button.pack(side=tk.TOP, anchor="w", pady=0)

# Main app window.
root = tk.Tk()
root.title("GetRich")
root.geometry("400x400")

load_income_sources()
load_outcome_sources()

def display_all():
    new_window_button = tk.Button(root, text="Dodaj źródło przychodu", command=open_new_source_income_window)
    new_window_button.pack(side=tk.TOP, anchor="w", pady=0)
    new_window_button = tk.Button(root, text="Dodaj źródło rozchodu", command=open_new_source_outcome_window)
    new_window_button.pack(side=tk.TOP, anchor="w", pady=0)

    # Display income sources.
    label = tk.Label(root, text="Źródła przychodu", font=("Helvetica", 16, "bold"))
    label.pack(anchor='w')

    for index, income_source in enumerate(income_sources):
        frame = tk.Frame(root)
        frame.pack(anchor='w', fill='x')

        src_income = tk.Label(frame, text=f"{income_source['name']}: {income_source['amount']}")
        src_income.pack(side=tk.LEFT)

        delete_button = tk.Button(frame, text="Usuń", command=lambda i=index: delete_income(i))
        delete_button.pack(side=tk.RIGHT)

    # Display wydatki
    label = tk.Label(root, text="Źródła rozchodu", font=("Helvetica", 16, "bold"))
    label.pack(anchor='w')

    for index, outcome_source in enumerate(outcome_sources):
        frame = tk.Frame(root)
        frame.pack(anchor='w', fill='x')

        src_income = tk.Label(frame, text=f"{outcome_source['name']}: {outcome_source['amount']}")
        src_income.pack(side=tk.LEFT)

        delete_button = tk.Button(frame, text="Usuń", command=lambda i=index: delete_outcome(i))
        delete_button.pack(side=tk.RIGHT)

display_all()
root.mainloop()
