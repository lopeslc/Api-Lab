import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
class QuizApp:
    def __init__(self, master):
        self.db_name = os.path.join(os.path.dirname(__file__), "..",  "data", "database.db")
        self.master = master
        self.master.title("Quiz")
        self.master.geometry("500x700")

        self.current_question_index = 0
        self.score = 0

        self.perguntas = self.puxar_perguntas()
        self.label_pergunta = tk.Label(self.master, text="", wraplength=450)
        self.label_pergunta.pack(pady=10)

        self.respostas_frame = tk.Frame(self.master)
        self.respostas_frame.pack(pady=10)

        self.botao_resposta1 = tk.Button(self.respostas_frame, text="", command=lambda: self.check_answer(0))
        self.botao_resposta1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.botao_resposta2 = tk.Button(self.respostas_frame, text="", command=lambda: self.check_answer(1))
        self.botao_resposta2.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.botao_resposta3 = tk.Button(self.respostas_frame, text="", command=lambda: self.check_answer(2))
        self.botao_resposta3.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.botao_resposta4 = tk.Button(self.respostas_frame, text="", command=lambda: self.check_answer(3))
        self.botao_resposta4.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.update_question()

    def executar_consulta(self, query):
        db_name = "data/database.db"
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result 

    def puxar_perguntas(self):
        query = 'SELECT * FROM questoes_choice ORDER BY updated_at DESC LIMIT 10'
        lista_perguntas = self.executar_consulta(query)
        return lista_perguntas

    def update_question(self):
        if self.current_question_index < len(self.perguntas):
            pergunta_atual = self.perguntas[self.current_question_index]
            pergunta_texto = "\n".join(self.wrap_text(pergunta_atual[1]))
            self.label_pergunta.config(text=pergunta_texto)

            respostas = sorted([pergunta_atual[i] for i in range(2, 6)])  # Ordena as respostas em ordem alfabética
            for i, resposta in enumerate(respostas):
                respostas[i] = "\n".join(self.wrap_text(resposta))
                self.botao_resposta1.config(text=respostas[0])
                self.botao_resposta2.config(text=respostas[1])
                self.botao_resposta3.config(text=respostas[2])
                self.botao_resposta4.config(text=respostas[3])
                
        else:
            messagebox.showinfo("Parabéns!", f"Sua pontuação final é: {self.score}/20")

    def wrap_text(self, text, max_words=15):
        words = text.split()
        wrapped_lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if len(current_line) >= max_words:
                wrapped_lines.append(" ".join(current_line))
                current_line = []
        if current_line:
            wrapped_lines.append(" ".join(current_line))
        return wrapped_lines

    def shuffle_answers(self, respostas):
        import random
        random.shuffle(respostas)

    def check_answer(self, resposta_index):
        resposta_selecionada = self.botao_resposta1.cget('text') if resposta_index == 0 else \
                            self.botao_resposta2.cget('text') if resposta_index == 1 else \
                            self.botao_resposta3.cget('text') if resposta_index == 2 else \
                            self.botao_resposta4.cget('text')
        
        resposta_correta = self.perguntas[self.current_question_index][7]  # Obtém a resposta correta da base de dados
        
        if resposta_selecionada.startswith(resposta_correta):
            self.score += 2
        else:
            messagebox.showinfo("Jogo perdido", "Você errou! Jogo perdido!")
            self.master.destroy()
            return

        self.current_question_index += 1
        self.update_question()


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

main()
