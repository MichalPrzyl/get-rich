import json
import tkinter as tk
from helpers import ensure_json_file_exists
from charts import draw_chart

ensure_json_file_exists('sources.json')
sources = []

def save_sources():
    with open("sources.json", "w") as file:
        json.dump(sources, file)

def load_sources():
    global sources
    with open("sources.json", "r") as source_file:
        sources = json.load(source_file)


def refresh_sources_display():
    for widget in root.winfo_children():
        widget.destroy()

def delete_income(index):
    del sources['income_sources'][index]
    save_sources()
    refresh_sources_display()
    display_all()

def delete_outcome(index):
    del sources['outcome_sources'][index]
    save_sources()
    refresh_sources_display()
    display_all()

def add_new_income(name, amount, start_dt, window):
    sources['income_sources'].append({
        "name": name,
        "amount": amount,
        "start_date": start_dt,
    })
    save_sources()
    refresh_sources_display()
    display_all()
    window.destroy()

def add_new_outcome(name, amount, start_dt, window):
    sources['outcome_sources'].append({
        "name": name,
        "amount": amount,
        "start_date": start_dt,
    })
    save_sources()
    refresh_sources_display()
    display_all()
    window.destroy()

def open_new_source_income_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj źródło przychodu")
    new_window.geometry("200x200")
    
    name_label = tk.Label(new_window, text=f"Nazwa źródła:")
    name_label.pack(anchor='w')
    
    name_entry = tk.Entry(new_window, width=30)
    name_entry.pack(anchor='w')

    amount_label = tk.Label(new_window, text=f"Kwota źródła:")
    amount_label.pack(anchor='w')
    
    amount_entry = tk.Entry(new_window, width=30)
    amount_entry.pack(anchor='w')

    start_date_label = tk.Label(new_window, text=f"Data rozpoczęcia źródła:")
    start_date_label.pack(anchor='w')
    
    start_date_entry = tk.Entry(new_window, width=30)
    start_date_entry.pack(anchor='w')
    
    add_income_button = tk.Button(
        new_window, 
        text="Dodaj źródło przychodu", 
        command=lambda: add_new_income(
            name_entry.get(), amount_entry.get(), start_date_entry.get(), new_window)
        )
    add_income_button.pack(side=tk.TOP, anchor="w", pady=0)

def open_new_source_outcome_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj źródło rozchodu")
    new_window.geometry("200x200")
    
    name_label = tk.Label(new_window, text=f"Nazwa źródła:")
    name_label.pack(anchor='w')
    
    name_entry = tk.Entry(new_window, width=30)
    name_entry.pack(anchor='w')

    amount_label = tk.Label(new_window, text=f"Kwota źródła:")
    amount_label.pack(anchor='w')
    
    amount_entry = tk.Entry(new_window, width=30)
    amount_entry.pack(anchor='w')

    start_date_label = tk.Label(new_window, text=f"Data rozpoczęcia źródła:")
    start_date_label.pack(anchor='w')
    
    start_date_entry = tk.Entry(new_window, width=30)
    start_date_entry.pack(anchor='w')
    
    add_outcome_button = tk.Button(
        new_window, 
        text="Dodaj źródło rozchodu", 
        command=lambda: add_new_outcome(
            name_entry.get(), amount_entry.get(), start_date_entry.get(), new_window)
        )
    add_outcome_button.pack(side=tk.TOP, anchor="w", pady=0)

def save_chart_settings(start_date, end_date):
    with open("chart_settings.json", "w") as file:
        json.dump({
            "start_date": start_date,
            "end_date": end_date
        }, file)

def load_chart_settings(start_date_entry, end_date_entry):
    try:
        with open("chart_settings.json", "r") as file:
            settings = json.load(file)
            start_date_entry.delete(0, tk.END)
            start_date_entry.insert(0, settings["start_date"])
            end_date_entry.delete(0, tk.END)
            end_date_entry.insert(0, settings["end_date"])
    except FileNotFoundError:
        pass

def open_show_chart_window():
    new_window = tk.Toplevel(root)
    new_window.title("Stwórz wykres")
    # new_window.geometry("500x500")
    
    # Start date label.
    start_date_label = tk.Label(new_window, text=f"Data początkowa wykresu:")
    start_date_label.pack(anchor='w')
    # Start date input.
    start_date_entry = tk.Entry(new_window, width=30)
    start_date_entry.pack(anchor='w')

    # End date label.
    end_date_label = tk.Label(new_window, text=f"Data końcowa wykresu:")
    end_date_label.pack(anchor='w')
    # End date input.
    end_date_entry = tk.Entry(new_window, width=30)
    end_date_entry.pack(anchor='w')

    create_chart_button = tk.Button(
        new_window, 
        text="Stwórz wykres", 
        command=lambda: draw_chart(start_date_entry.get(), end_date_entry.get(), sources)
    )
    create_chart_button.pack(side=tk.TOP, anchor="w", pady=0)

    save_chart_settings_button = tk.Button(
        new_window, 
        text="Zapisz ustawienia wykresu", 
        command=lambda: save_chart_settings(start_date_entry.get(), end_date_entry.get())
    )
    save_chart_settings_button.pack(side=tk.TOP, anchor="w", pady=0)
    
    load_chart_settings_button = tk.Button(
        new_window, 
        text="Załaduj ustawienia wykresu", 
        command=lambda: load_chart_settings(start_date_entry, end_date_entry)
    )
    load_chart_settings_button.pack(side=tk.TOP, anchor="w", pady=0)


# Main app window.
root = tk.Tk()
root.title("GetRich")
root.geometry("400x400")

load_sources()

def display_all():
    # New income source button.
    new_window_button = tk.Button(root, text="Dodaj źródło przychodu", command=open_new_source_income_window)
    new_window_button.pack(side=tk.TOP, anchor="w", pady=0)
    # New outcome source button.
    new_window_button = tk.Button(root, text="Dodaj źródło rozchodu", command=open_new_source_outcome_window)
    new_window_button.pack(side=tk.TOP, anchor="w", pady=0)
    # Draw chart button.
    new_window_button = tk.Button(root, text="Wykres", command=lambda: open_show_chart_window())
    new_window_button.pack(side=tk.TOP, anchor="w", pady=0)


    # Display income sources.
    label = tk.Label(root, text="Źródła przychodu", font=("Helvetica", 16, "bold"))
    label.pack(anchor='w')

    for index, income_source in enumerate(sources['income_sources']):
        frame = tk.Frame(root)
        frame.pack(anchor='w', fill='x')

        src_income = tk.Label(frame, text=f"{income_source['name']}: {income_source['amount']}")
        src_income.pack(side=tk.LEFT)

        delete_button = tk.Button(frame, text="Usuń", command=lambda i=index: delete_income(i))
        delete_button.pack(side=tk.RIGHT)

    # Display wydatki
    label = tk.Label(root, text="Źródła rozchodu", font=("Helvetica", 16, "bold"))
    label.pack(anchor='w')

    for index, outcome_source in enumerate(sources['outcome_sources']):
        frame = tk.Frame(root)
        frame.pack(anchor='w', fill='x')

        src_income = tk.Label(frame, text=f"{outcome_source['name']}: {outcome_source['amount']}")
        src_income.pack(side=tk.LEFT)

        delete_button = tk.Button(frame, text="Usuń", command=lambda i=index: delete_outcome(i))
        delete_button.pack(side=tk.RIGHT)

display_all()
root.mainloop()
