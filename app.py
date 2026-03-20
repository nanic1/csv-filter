import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione um arquivo CSV",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
    )
    
    if caminho:
        try:
            with open(caminho, newline='', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                dados = list(leitor)  # Converte para lista de listas
            label_arquivo.config(text=f"Arquivo selecionado:\n{caminho}")
            label_dados.config(text=f"Linhas do arquivo:\n{len(dados)}")
        except Exception as e:
            label_arquivo.config(text=f"Erro ao ler arquivo: {e}") 

# Criação da janela principal
janela = tk.Tk()
janela.title("CSV Filter")
janela.geometry("500x300")

# Botão para abrir o arquivo
botao_abrir = tk.Button(janela, text="Escolher arquivo CSV", command=selecionar_arquivo)
botao_abrir.pack(pady=20)

# labels para exibir dados na tela
label_arquivo = tk.Label(janela, text="Nenhum arquivo selecionado")
label_arquivo.pack(pady=10)

label_dados = tk.Label(janela)
label_dados.pack(pady=2)

# Loop principal da GUI
janela.mainloop()