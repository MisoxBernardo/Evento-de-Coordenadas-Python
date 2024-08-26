import customtkinter as ctk

# Função para alterar o canal
def mudar_canal(novo_canal):
    global canal_atual
    canal_atual = novo_canal
    canal_label.configure(text=f"Canal: {canal_atual}")

# Função para aumentar o canal
def canal_para_cima():
    novo_canal = canal_atual + 1
    mudar_canal(novo_canal)

# Função para diminuir o canal
def canal_para_baixo():
    novo_canal = canal_atual - 1
    mudar_canal(novo_canal)

# Função para definir um canal específico
def definir_canal():
    try:
        novo_canal = int(entry_canal.get())
        mudar_canal(novo_canal)
    except ValueError:
        canal_label.configure(text="Entrada inválida! Por favor, insira um número.")

# Configuração da janela principal
janela = ctk.CTk()
janela.title("Simulador de Canal de TV")
janela.geometry("300x400")

# Canal inicial
canal_atual = 1

# Label para mostrar o canal atual
canal_label = ctk.CTkLabel(janela, text=f"Canal: {canal_atual}", font=("Arial", 24))
canal_label.pack(pady=20)

# Entrada para definir um canal específico
entry_canal = ctk.CTkEntry(janela, font=("Arial", 18), justify='center')
entry_canal.pack(pady=10)

# Botão para definir o canal
botao_definir = ctk.CTkButton(janela, text="Definir Canal", command=definir_canal, font=("Arial", 18))
botao_definir.pack(pady=5)

# Botão para canal acima
botao_cima = ctk.CTkButton(janela, text="Canal +", command=canal_para_cima, font=("Arial", 18))
botao_cima.pack(pady=5)

# Botão para canal abaixo
botao_baixo = ctk.CTkButton(janela, text="Canal -", command=canal_para_baixo, font=("Arial", 18))
botao_baixo.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()
