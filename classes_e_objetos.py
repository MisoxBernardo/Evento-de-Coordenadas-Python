import customtkinter as ctk
import tkinter as tk

# Classe Conta
class Conta:
    def __init__(self, numero, cpf, titular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
            
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente!")
        return self.saldo
                
    def gerar_extrato(self):
        return f"Número: {self.numero} \nCPF: {self.cpf} \nSaldo: {self.saldo}"

# Função para atualizar o saldo na interface gráfica
def atualizar_saldo():
    try:
        valor = float(entry_valor.get())
        if depositante_var.get() == "Joao":
            conta_joao.depositar(valor)
            saldo_joao_label.configure(text=f"Saldo de Joao: R$ {conta_joao.saldo:.2f}")
        elif depositante_var.get() == "Maria":
            conta_maria.depositar(valor)
            saldo_maria_label.configure(text=f"Saldo de Maria: R$ {conta_maria.saldo:.2f}")
        
        if recebedor_var.get() == "Joao":
            conta_joao.sacar(valor)
            saldo_joao_label.configure(text=f"Saldo de Joao: R$ {conta_joao.saldo:.2f}")
        elif recebedor_var.get() == "Maria":
            conta_maria.sacar(valor)
            saldo_maria_label.configure(text=f"Saldo de Maria: R$ {conta_maria.saldo:.2f}")
        
        # Atualiza o saldo da outra pessoa também
        if depositante_var.get() != recebedor_var.get():
            if recebedor_var.get() == "Joao":
                saldo_joao_label.configure(text=f"Saldo de Joao: R$ {conta_joao.saldo:.2f}")
            elif recebedor_var.get() == "Maria":
                saldo_maria_label.configure(text=f"Saldo de Maria: R$ {conta_maria.saldo:.2f}")
        
    except ValueError as e:
        saldo_joao_label.configure(text=str(e))
        saldo_maria_label.configure(text=str(e))

# Configuração da janela principal
janela = ctk.CTk()
janela.title("Contas Bancárias")

# Criação dos objetos Conta
conta_joao = Conta(numero=1, cpf="123.456.789-00", titular="Joao", saldo=1000)
conta_maria = Conta(numero=2, cpf="987.654.321-00", titular="Maria", saldo=1000)

# Labels para mostrar o saldo
saldo_joao_label = ctk.CTkLabel(janela, text=f"Saldo de Joao: R$ {conta_joao.saldo:.2f}")
saldo_joao_label.grid(row=0, column=0, columnspan=2, pady=10)

saldo_maria_label = ctk.CTkLabel(janela, text=f"Saldo de Maria: R$ {conta_maria.saldo:.2f}")
saldo_maria_label.grid(row=1, column=0, columnspan=2, pady=10)

# Inputs para selecionar depositante e recebedor
ctk.CTkLabel(janela, text="Depositante:").grid(row=2, column=0, padx=10, pady=5)
depositante_var = tk.StringVar(value="Joao")
ctk.CTkOptionMenu(janela, values=["Joao", "Maria"], variable=depositante_var).grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Recebedor:").grid(row=3, column=0, padx=10, pady=5)
recebedor_var = tk.StringVar(value="Maria")
ctk.CTkOptionMenu(janela, values=["Joao", "Maria"], variable=recebedor_var).grid(row=3, column=1, padx=10, pady=5)

# Input para valor
ctk.CTkLabel(janela, text="Valor:").grid(row=4, column=0, padx=10, pady=5)
entry_valor = ctk.CTkEntry(janela)
entry_valor.grid(row=4, column=1, padx=10, pady=5)

# Botão para realizar as operações
ctk.CTkButton(janela, text="Realizar Transação", command=atualizar_saldo).grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar a aplicação
janela.mainloop()
