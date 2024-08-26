import customtkinter as ctk

# Função para capturar e exibir as coordenadas do mouse
def on_mouse_move(event):
    x, y = event.x, event.y
    coordenadas_var.set(f"Coordenadas: X={x}, Y={y}")

# Criar a janela principal
janela = ctk.CTk()
janela.title("Evento de Coordenadas do Mouse")

# Variável para armazenar as coordenadas
coordenadas_var = ctk.StringVar()
coordenadas_var.set("Coordenadas: X=0, Y=0")

# Criar um label para exibir as coordenadas
label_coordenadas = ctk.CTkLabel(janela, textvariable=coordenadas_var)
label_coordenadas.pack(padx=20, pady=20)

# Bind do evento de movimento do mouse para a janela
janela.bind('<Motion>', on_mouse_move)

# Iniciar a aplicação
janela.mainloop()
