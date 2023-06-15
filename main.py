""" Test na multy môj script  MiroR 062023"""

import tkinter as tk

# Okno sa otvorí uprostred Windows obrazovky
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}") 


def search_ports():
    from comport_search import COMPorts
    # Volanie statickej metódy pre získanie COM portov
    com_ports = COMPorts.get_com_ports().data
    # Získanie obsahu premenných com a comdescript
    com = [port.device for port in com_ports]
    comdescript = [port.description for port in com_ports]
    # Výpis obsahu premenných
    print("ports:", com, "popis:", comdescript)


# Vytvorenie hlavného okna
root = tk.Tk()

# Vytvorenie tlačidla
search_button = tk.Button(root, text="Search port", command=search_ports)
search_button.pack()

# Vytvorenie labelu pre zobrazenie výsledku
result_label = tk.Label(root, text="COM:")
result_label.pack()

# Vykreslenie okna uprostred Windows
center_window(root)
# Spustenie hlavného smyčky aplikácie
root.mainloop()
