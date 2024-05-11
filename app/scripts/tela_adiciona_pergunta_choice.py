from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class CadastroQuestaoChoice:
    
    db_name = "data/database.db"
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x700")
        self.root.title("Cadastrar Questão")
        self.root.resizable(False, False)
        self.root.config(bg="#fff", bd=10)
        
        # Titulo da pagina
        title_page = Label(root, text="AppLab Banco de Questões", fg="ORANGE", font=("Comic Sans", 13, "bold"), pady=5)
        title_page.pack()

        # Carregar logo da App
        self.logo = PhotoImage(file="assets/images/logo.png")
        label_imagen = Label(root, image=self.logo)
        label_imagen.pack(pady=5)
        
        # Marco
        marco = LabelFrame(root, text="Dados da Questão", font=("Roboto", 10, "bold"))
        marco.config(bd=2, pady=5, bg="#fff")
        marco.pack()

        # Formulário Cadastro de Estudantes
        label_email_institucional = Label(marco, text="Email Institucional Professor: ", font=("Comic Sans", 10, "bold"))
        label_email_institucional.grid(row=0, column=0, sticky='e', padx=2, pady=8)
        self.email_institucional = Entry(marco, width=25)
        self.email_institucional.focus()
        self.email_institucional.grid(row=0, column=1, padx=5, pady=8)

        label_enunciado = Label(marco, text="Enunciado da Questão: ", font=("Comic Sans", 10, "bold"))
        label_enunciado.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.enunciado = Entry(marco, width=25)
        self.enunciado.grid(row=1, column=1, padx=5, pady=8)

        label_correta = Label(marco, text="Resposta Correta: ", font=("Comic Sans", 10, "bold"))
        label_correta.grid(row=2, column=0, sticky='e', padx=5, pady=8)
        self.correta = Entry(marco, width=25)
        self.correta.grid(row=2, column=1, padx=5, pady=8)
        
        label_alternativa_a = Label(marco, text="alternativa A: ", font=("Comic Sans", 10, "bold"))
        label_alternativa_a.grid(row=3, column=0, sticky='e', padx=5, pady=8)
        self.alternativa_a = Entry(marco, width=25)
        self.alternativa_a.grid(row=3, column=1, padx=5, pady=8)

        label_alternativa_b = Label(marco, text="alternativa B: ", font=("Comic Sans", 10, "bold"))
        label_alternativa_b.grid(row=4, column=0, sticky='e', padx=5, pady=8)
        self.alternativa_b = Entry(marco, width=25)
        self.alternativa_b.grid(row=4, column=1, padx=5, pady=8)
        
        label_alternativa_c = Label(marco, text="alternativa C: ", font=("Comic Sans", 10, "bold"))
        label_alternativa_c.grid(row=5, column=0, sticky='e', padx=5, pady=8)
        self.alternativa_c = Entry(marco, width=25)
        self.alternativa_c.grid(row=5, column=1, padx=5, pady=8)
        
        label_alternativa_d = Label(marco, text="alternativa D: ", font=("Comic Sans", 10, "bold"))
        label_alternativa_d.grid(row=6, column=0, sticky='e', padx=5, pady=8)
        self.alternativa_d = Entry(marco, width=25)
        self.alternativa_d.grid(row=6, column=1, padx=5, pady=8)
        
        label_alternativa_e = Label(marco, text="alternativa E: ", font=("Comic Sans", 10, "bold"))
        label_alternativa_e.grid(row=7, column=0, sticky='e', padx=5, pady=8)
        self.alternativa_e = Entry(marco, width=25)
        self.alternativa_e.grid(row=7, column=1, padx=5, pady=8)
        
        label_verdadeiro_falso = Label(marco, text="Verdadeiro ou Falso: ", font=("Comic Sans", 10, "bold"))
        label_verdadeiro_falso.grid(row=8, column=0, sticky='e', padx=5, pady=8)
        self.verdadeiro_falso = ttk.Combobox(marco, values=["Não se aplica", "Verdadeiro", "Falso"], width=30, state="readonly")
        self.verdadeiro_falso.current(0)
        self.verdadeiro_falso.grid(row=8, column=1, padx=5, pady=8)
        
        # Frame botões
        frame_botoes = Frame(root)
        frame_botoes.pack()

        # Botões
        botao_registrar = Button(frame_botoes, text="CADASTRAR", command=self.registrar_questao, height=2, width=10, bg="green", fg="white", font=("Comic Sans", 10, "bold"))
        botao_registrar.grid(row=0, column=0, padx=5, pady=15)
        botao_limpar = Button(frame_botoes, text="LIMPAR", command=self.limpar_formulario, height=2, width=10, bg="gray", fg="white", font=("Comic Sans", 10, "bold"))
        botao_limpar.grid(row=0, column=1, padx=5, pady=15)
    
    def limpar_formulario(self):
        self.email_institucional.delete(0, END)
        self.enunciado.delete(0, END)
        self.correta.delete(0, END)
        self.alternativa_a.delete(0, END)
        self.alternativa_b.delete(0, END)
        self.alternativa_c.delete(0, END)
        self.alternativa_d.delete(0, END)
        self.alternativa_e.delete(0, END)
        self.verdadeiro_falso.current(0)
    
    def recuperar_id_professor(self, email_institucional):
        query = """
        SELECT usuario_professor.id 
        FROM usuario_professor
        INNER JOIN usuarios
        ON usuario_professor.usuario_id = usuarios.id
        WHERE usuarios.email_institucional = ?
        """
        # Adicione um try-except para lidar com possíveis erros na execução da consulta
        try:
            # Execute a consulta SQL e recupere o resultado
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute(query, (email_institucional,))
                # Use fetchone() para obter a primeira linha do resultado
                professor_id = cursor.fetchone()
                # Se professor_id não for None, retorne o primeiro elemento da tupla
                if professor_id:
                    return professor_id[0]
                else:
                    messagebox.showerror("Erro", "Professor não encontrado")
                    return None
        except sqlite3.Error as e:
            # Em caso de erro, exiba uma mensagem de erro
            messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro ao acessar o banco de dados: {e}")
            return None



    
    def validar_formulario_completo(self):
        if (
            len(self.email_institucional.get()) !=0 and 
            len(self.enunciado.get()) !=0 and 
            (
                (self.verdadeiro_falso.get() == "Verdadeiro" or self.verdadeiro_falso.get() == "Falso") or
                (len(self.correta.get()) !=0 and len(self.alternativa_a.get()) !=0 and len(self.alternativa_b.get()) !=0 and len(self.alternativa_c.get()) !=0 and len(self.alternativa_d.get()) !=0 and len(self.alternativa_e.get()) !=0)
            )
        ):
            return True
        else:
            messagebox.showerror("Erro", "Complete todos os campos do formulário")
            return False
    
    def registrar_questao(self):
        if self.validar_formulario_completo():
            professor_id = self.recuperar_id_professor(self.email_institucional.get())
            if professor_id:
                if self.verdadeiro_falso.get() == "Verdadeiro" or self.verdadeiro_falso.get() == "Falso":
                    if self.correta.get() == "" or self.alternativa_a.get() == "" or self.alternativa_b.get() == "" or self.alternativa_c.get() == "" or self.alternativa_d.get() == "" or self.alternativa_e.get() == "":
                        messagebox.showerror("Erro", "Complete todos os campos do formulário")
                    else:
                        query = 'INSERT INTO questoes_choice (enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, correta, usuario_professor_id, explicacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                        parameters = (self.enunciado.get(), self.alternativa_a.get(), self.alternativa_b.get(), self.alternativa_c.get(), self.alternativa_d.get(), self.alternativa_e.get(), self.correta.get(), professor_id, "")
                        self.executar_consulta(query, parameters)
                        messagebox.showinfo("Sucesso", "Questão cadastrada com sucesso")
                        self.limpar_formulario()
                elif self.verdadeiro_falso.get() == "Não se aplica":
                    query = 'INSERT INTO questoes_verdadeiro_ou_falso (enunciado, is_correta, usuario_professor_id, explicacao) VALUES (?, ?, ?, ?)'
                    parameters = (self.enunciado.get(), None, professor_id, "")
                    self.executar_consulta(query, parameters)
                    messagebox.showinfo("Sucesso", "Questão cadastrada com sucesso")
                    self.limpar_formulario()
                else:
                    if self.correta.get() == "":
                        messagebox.showerror("Erro", "Complete todos os campos do formulário")
                    else:
                        query = 'INSERT INTO questoes_choice (enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, correta, usuario_professor_id, explicacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                        parameters = (self.enunciado.get(), self.alternativa_a.get(), self.alternativa_b.get(), self.alternativa_c.get(), self.alternativa_d.get(), self.alternativa_e.get(), self.correta.get(), professor_id, "")
                        self.executar_consulta(query, parameters)
                        messagebox.showinfo("Sucesso", "Questão cadastrada com sucesso")
                        self.limpar_formulario()


    def executar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
        return result


root = tk.Tk()
app = CadastroQuestao(root)
root.mainloop()