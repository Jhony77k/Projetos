import tkinter as tk
from tkinter import ttk

class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de kcal/h para TR")
        self.root.geometry("1366x768")
        self.historico = []

        # Entrada de valor
        self.label_valor = ttk.Label(root, text="Valor em kcal/h:")
        self.label_valor.grid(row=0, column=0, padx=5, pady=5)
        self.entry_valor = ttk.Entry(root)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5)

        # Botão de conversão
        self.btn_converter = ttk.Button(root, text="Converter", command=self.converter)
        self.btn_converter.grid(row=0, column=2, padx=5, pady=5)
        

        # Lista de histórico
        self.label_hist = ttk.Label(root, text="Histórico de Conversões:")
        self.label_hist.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.listbox_hist = tk.Listbox(root, width=50)
        self.listbox_hist.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def converter(self):
        valor = self.entry_valor.get()
        try:
            valor_float = float(valor)
            
            # Fator de conversão para kcal/h -> TR (Toneladas de Refrigeração)
            fator = 0.000330693393277316  # Fator de conversão

            resultado = valor_float * fator  # Conversão de kcal/h para TR
            texto = f"{valor_float} kcal/h equivale a {resultado:.6f} TR"
            
            # Adiciona ao histórico e na lista
            self.historico.append(texto)
            self.listbox_hist.insert(tk.END, texto)
        except ValueError:
            self.listbox_hist.insert(tk.END, "Valor inválido!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()
