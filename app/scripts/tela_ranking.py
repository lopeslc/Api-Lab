from tkinter import *
import tkinter as tk
import sqlite3
import os

class TelaRanking(tk.Frame):  # Modificando para herdar de tk.Frame
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("AppLab-RANKING")
        self.master.geometry("500x500")
        self.master.config(bg="orange")
        self.master.resizable(False, False)

        self.label_titulo = tk.Label(self, text="AppLab-RANKING", fg="orange", font=("Poppins", 32))
        self.label_titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.frame_ranking = tk.Frame(self, bg="orange")
        self.frame_ranking.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9)  # Defina o relwidth para 90%

        self.scrollbar = Scrollbar(self.frame_ranking)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.table = Listbox(self.frame_ranking, yscrollcommand=self.scrollbar.set, width=50, bg="white")  # Defina a largura da tabela para 50
        self.table.pack(expand=YES, fill=BOTH)
        self.scrollbar.config(command=self.table.yview)

        self.button_ordenar = tk.Button(self, text="Ordenar por Score", font=("Poppins", 12), bg="green", fg="orange", command=self.ordenar_score)
        self.button_ordenar.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.entry_busca = tk.Entry(self, font=("Poppins", 12))
        self.entry_busca.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.button_busca = tk.Button(self, text="Buscar", font=("Poppins", 12), bg="white", fg="orange", command=self.buscar_username)
        self.button_busca.place(relx=0.8, rely=0.85, anchor=tk.CENTER)

        self.carregar_ranking()

    def db(self, query, parameters=()):
        db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
        # Conectar-se ao banco de dados e executar a consulta
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters).fetchall()  # Use fetchall() to retrieve all records
            conn.commit()
            return result

    def consulta_ranking(self):
        consulta = """SELECT usuarios.email_institucional, usuarios.username, score_total.total_score
                      FROM usuarios
                      INNER JOIN usuario_estudante
                          ON usuario_estudante.usuario_id = usuarios.id
                      RIGHT JOIN score_total
                          ON score_total.usuario_id_estudante = usuario_estudante.id
                      WHERE usuario_estudante.is_active = 1
                      ORDER BY score_total.total_score DESC;"""
        return self.db(consulta)

    def carregar_ranking(self):
        resultado_formatado = self.consulta_ranking()

        self.table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

        # Adiciona cabeçalhos das colunas
        self.table.insert(END, "Email Institucional     Username     Score Total")
        self.table.insert(END, "-" * 60)

        # Adiciona os dados formatados à tabela
        for linha in resultado_formatado:
            email_institucional, username, total_score = linha
            self.table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")

    def ordenar_score(self):
        resultado_formatado = self.consulta_ranking()

        # Ordena os resultados pelo total_score
        resultado_formatado.sort(key=lambda x: x[2], reverse=True)

        self.table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

        # Adiciona cabeçalhos das colunas
        self.table.insert(END, "Email Institucional     Username     Score Total")
        self.table.insert(END, "-" * 60)

        # Adiciona os dados formatados à tabela
        for linha in resultado_formatado:
            email_institucional, username, total_score = linha
            self.table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")

    def buscar_username(self):
        username = self.entry_busca.get()

        resultado_formatado = self.consulta_ranking()

        resultado_filtrado = [linha for linha in resultado_formatado if username.lower() in linha[1].lower()]

        self.table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

        # Adiciona cabeçalhos das colunas
        self.table.insert(END, "Email Institucional     Username     Score Total")
        self.table.insert(END, "-" * 60)

        # Adiciona os dados formatados à tabela
        for linha in resultado_filtrado:
            email_institucional, username, total_score = linha
            self.table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")


root = Tk()
app = TelaRanking(root)  # Passando a raiz como argumento
app.pack(fill="both", expand=True)  # Expandindo o widget para preencher a janela
app.mainloop()
