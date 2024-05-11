import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from uuid import uuid4

class AdicionaPerguntaVf:
    
    def __init__(self, root):
        self.db_name = os.path.join(os.path.dirname(__file__), "..",  "data", "database.db")
        
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Cadastrar Verdadeiro ou Falso")
        self.root.resizable(False, False)
        self.root.config(bg="#fff", bd=10)
        
        # Titulo da pagina
        title_page = Label(root, text="AppLab Banco de Questões", fg="ORANGE", font=("Comic Sans", 13, "bold"), pady=5)
        title_page.pack()

        # Carregar logo da App
        imagen_registro = Image.open("assets/images/logo.png")
        nova_imagem = imagen_registro.resize((40,40))
        render = ImageTk.PhotoImage(nova_imagem)
        label_imagen = Label(root, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)
        
        # Marco
        marco = LabelFrame(root, text="dados da questao", font=("Roboto", 10, "bold"))
        marco.config(bd=2, pady=5)
        marco.pack()

        # Formulário Cadastro de Estudantes
        label_enunciado = Label(marco, text="Enunciado: ", font=("Comic Sans", 10, "bold"))
        label_enunciado.grid(row=0, column=0, sticky='e', padx=5, pady=8)
        self.enunciado = Entry(marco, width=25)
        self.enunciado.focus()
        self.enunciado.grid(row=0, column=1, padx=5, pady=8)
        # Pergunta
        label_recovery_question = Label(marco, text="Resposta da Pergunta: ", font=("Comic Sans", 10, "bold"))
        label_recovery_question.grid(row=3, column=0, sticky='e', padx=5, pady=8)
        self.recovery_question = ttk.Combobox(marco, values=["Falso", "Verdadeiro"], width=30, state="readonly")
        self.recovery_question.current(0)
        self.recovery_question.grid(row=3, column=1, padx=5, pady=8)
  
        label_explicacao = Label(marco, text="Justificativa da Resposta: ", font=("Comic Sans", 10, "bold"))
        label_explicacao.grid(row=5, column=0, sticky='e', padx=5, pady=8)
        self.explicacao = Entry(marco, width=25)
        self.explicacao.focus()
        self.explicacao.grid(row=6, column=0, padx=5, pady=8)
        # Botões
        marco_botones = Frame(root)
        marco_botones.config(bg="#fff")
        marco_botones.pack(pady=10)

        button_cadastrar = Button(marco_botones, text="Cadastrar", bg="green", fg="white", font=("Comic Sans", 10, "bold"), command=self.registrar_verdadeiro_ou_falso)
        button_cadastrar.grid(row=0, column=0, padx=5, pady=10)

        button_salir = Button(marco_botones, text="Sair", bg="red", fg="white", font=("Comic Sans", 10, "bold"), command=self.root.destroy)
        button_salir.grid(row=0, column=1, padx=5, pady=10)
    
    def validar_formulario_completo(self):
        # Verifica se todos os campos foram preenchidos
        if (self.enunciado.get() == "" or self.username.get() == "" or
            self.password.get() == "" or self.repetir_password.get() == "" or
            self.recovery_answer.get() == ""):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return False
        return True

    def validar_password(self):
        # Verifica se a senha e a repetição da senha são iguais
        if self.password.get() != self.repetir_password.get():
            messagebox.showerror("Erro", "As senhas não correspondem.")
            return False
        return True

    def validar_enunciado(self):
        # Verifica se o email institucional tem o formato correto
        email = self.enunciado.get()
        if not email.endswith("@estudante.piaget.com.br"):
            messagebox.showerror("Erro", "O email institucional deve ser de estudantes PIAGET.")
            return False
        return True

    def executar_consulta(self, query, parameters=()):
        # Conectar-se ao banco de dados e executar a consulta
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def limpar_formulario(self):
        # Limpa todos os campos do formulário
        self.enunciado.delete(0, END)
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.repetir_password.delete(0, END)
        self.recovery_answer.delete(0, END)
        self.enunciado.focus()

    def registrar_verdadeiro_ou_falso(self):
        if self.validar_formulario_completo() and self.validar_password() and self.validar_enunciado():
            # Gerar um UUID4 para o usuario_id
            usuario_id = str(uuid4())
            usuario_id_estudante = str(uuid4())  # Gerar um UUID4 para o usuario_id_estudante
            role = "ESTUDANTES"

            # Definir transação para garantir a atomicidade das operações
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                try:
                    # Iniciar a transação
                    conn.execute("BEGIN TRANSACTION")

                    # Query para inserir dados na tabela Usuarios
                    query_usuarios = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)'
                    parameters_usuarios = (usuario_id,
                                        self.enunciado.get(),
                                        self.username.get(),
                                        self.password.get(),
                                        self.recovery_question.get(),
                                        self.recovery_answer.get(),
                                        role)
                    cursor.execute(query_usuarios, parameters_usuarios)

                    # Query para inserir dados na tabela usuario_estudante
                    query_usuario_estudante = 'INSERT INTO usuario_estudante VALUES(?, ?, ?)'
                    parameters_usuario_estudante = (usuario_id_estudante, 1, usuario_id)  # Definir is_active como 1
                    cursor.execute(query_usuario_estudante, parameters_usuario_estudante)

                    # Query para inserir dados na tabela score_total
                    query_score_total = 'INSERT INTO score_total VALUES(?, ?, ?)'
                    parameters_score_total = (str(uuid4()), 0, usuario_id_estudante)  # Definir total_score como 0 e usar usuario_id_estudante
                    cursor.execute(query_score_total, parameters_score_total)

                    # Commit da transação
                    conn.commit()

                    messagebox.showinfo("ESTUDANTE CADASTRADO", f"""
                                        Username: {self.username.get()}
                                        Email institucional: {self.enunciado.get()}
                                        Senha: {self.password.get()}
                                        Recuperação: {self.recovery_question.get()}
                                        Resposta: {self.recovery_answer.get()}                       
                                        """)
                    print('USUARIO CRIADO')
                    self.limpar_formulario()

                except Exception as e:
                    # Em caso de erro, rollback da transação
                    conn.rollback()
                    messagebox.showerror("Erro", f"Erro ao cadastrar o estudante: {e}")
