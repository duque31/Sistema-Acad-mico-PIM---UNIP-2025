"""
gui.py
Interface Gráfica (Tkinter) do Sistema Acadêmico - PIM II
-----------------------------------------------------------
Responsável por exibir os alunos cadastrados em formato de
tabela e permitir atualização visual dos dados armazenados
no arquivo JSON.
-----------------------------------------------------------"""

import tkinter as tk
from tkinter import ttk
import storage

# Caminho do arquivo de dados JSON
DB_FILE = "dados.json"


# === Classe Principal da Interface ===
class SistemaGUI(tk.Tk):
    """
    Classe que representa a janela principal do sistema acadêmico.
    Exibe uma lista de alunos com suas médias e status de aprovação.
    """
    def __init__(self):
        super().__init__()

        # Configurações básicas da janela
        self.title("Sistema Acadêmico - PIM II")
        self.geometry("600x400")
        self.config(bg="#f0f0f0")

        # Título principal
        tk.Label(
            self,
            text="Alunos Cadastrados",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        # Tabela (Treeview) 
        self.tree = ttk.Treeview(self, columns=("nome", "media", "status"), show="headings")

        # Cabeçalhos e formatação das colunas
        for col, text in zip(("nome", "media", "status"), ("Nome", "Média", "Status")):
            self.tree.heading(col, text=text)
            self.tree.column(col, anchor="center", width=180)

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Botão de atualização
        tk.Button(
            self,
            text="🔄 Atualizar",
            command=self.atualizar,
            bg="#007acc",
            fg="white"
        ).pack(pady=10)

        # Atualiza a tabela ao iniciar
        self.atualizar()


    # === Função para atualizar os dados da tabela ===
    def atualizar(self):
        """
        Recarrega os dados do arquivo JSON e atualiza a tabela
        com as informações mais recentes dos alunos.
        """
        db = storage.carregar_json(DB_FILE)

        # Limpa a tabela antes de inserir novos dados
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insere os dados atualizados
        for aluno in db["alunos"]:
            self.tree.insert("", "end", values=(aluno.nome, f"{aluno.media:.2f}", aluno.status))


# === Execução manual para teste ===
if __name__ == "__main__":
    print("= Teste manual da Interface Gráfica (Tkinter) =")
    app = SistemaGUI()
    app.mainloop()
