import customtkinter as ctk
import numpy as np

# Função para calcular as raízes da equação quadrática
def calcular_raizes():
    try:
        # Obtém os coeficientes a, b e c
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        if a == 0:
            resultado_label.configure(text="Erro: Coeficiente 'a' não pode ser zero!")
            return
        
        # Coeficientes do polinômio
        coeficientes = [a, b, c]
        
        # Calcula as raízes usando numpy
        raizes = np.roots(coeficientes)
        
        # Exibe as raízes
        if len(raizes) == 2:
            resultado_label.configure(text=f"Raízes: {raizes[0]:.2f} e {raizes[1]:.2f}")
        elif len(raizes) == 1:
            resultado_label.configure(text=f"Raiz dupla: {raizes[0]:.2f}")
        else:
            resultado_label.configure(text="Não há raízes reais.")
    except ValueError:
        resultado_label.configure(text="Erro: Entrada inválida!")

# Configurações iniciais do CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "dark", "light"
ctk.set_default_color_theme("blue")  # Cores: "blue", "green", "dark-blue"

# Criação da janela principal
janela = ctk.CTk()
janela.title("Calculadora de Raízes Quadráticas")
janela.geometry("400x300")

# Widgets usando CustomTkinter e grid
label_a = ctk.CTkLabel(janela, text="Coeficiente a:")
label_a.grid(row=0, column=0, padx=10, pady=10)

entry_a = ctk.CTkEntry(janela)
entry_a.grid(row=0, column=1, padx=10, pady=10)

label_b = ctk.CTkLabel(janela, text="Coeficiente b:")
label_b.grid(row=1, column=0, padx=10, pady=10)

entry_b = ctk.CTkEntry(janela)
entry_b.grid(row=1, column=1, padx=10, pady=10)

label_c = ctk.CTkLabel(janela, text="Coeficiente c:")
label_c.grid(row=2, column=0, padx=10, pady=10)

entry_c = ctk.CTkEntry(janela)
entry_c.grid(row=2, column=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_raizes)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=20)

resultado_label = ctk.CTkLabel(janela, text="Resultado:")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Inicia o loop principal da janela
janela.mainloop()
