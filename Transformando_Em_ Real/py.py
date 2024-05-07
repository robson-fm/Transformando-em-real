import tkinter as tk

def format_as_currency(value):
    # Remove caracteres indesejados e prepara a conversão para float
    value = value.replace("R$", "").replace(".", "").replace(",", "")
    if value:
        # Converte para float e divide por 100 para ajustar os centavos
        value = float(value) / 100
    else:
        value = 0.0
    # Formata com separadores de milhar e duas casas decimais
    formatted = f"R$ {value:,.2f}"
    # Substitui pontos por vírgulas e vírgulas por pontos conforme padrão brasileiro
    return formatted.replace(",", "x").replace(".", ",").replace("x", ".")

def on_value_change(event):
    # Obtém o valor atual do campo de entrada e tenta formatá-lo
    try:
        entry_value = entry.get()
        if entry_value.startswith("R$"):
            formatted_value = format_as_currency(entry_value)
            entry.delete(0, tk.END)
            entry.insert(0, formatted_value)
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "R$ ")
    except ValueError:
        pass

root = tk.Tk()
root.title("Currency Entry")

entry = tk.Entry(root, font='Arial 14')
entry.pack(padx=10, pady=10)

entry.bind("<KeyRelease>", on_value_change)

root.mainloop()

