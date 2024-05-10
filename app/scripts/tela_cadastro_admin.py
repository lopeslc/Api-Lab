import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from uuid import uuid4

class CadastroAdmin:
    
    def __init__(self, root):
        self.db_name = os.path.join(os.path.dirname(__file__), "..",  "data", "database.db")
        
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Cadastrar Admin")
        self.root.resizable(False, False)
        self.root.config(bg="#fff", bd=10)
        
        # Titulo da pagina
        title_page = Label(root, text="AppLab Estudantes", fg="ORANGE", font=("Comic Sans", 13, "bold"), pady=5)
        title_page.pack()

        # Carregar logo da App
        imagen_registro = Image.open("assets/images/logo.png")
        nova_imagem = imagen_registro.resize((40,40))
        render = ImageTk.PhotoImage(nova_imagem)
        label_imagen = Label(root, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)
        
        # Marco
        marco = LabelFrame(root, text="dados del Admin", font=("Roboto", 10, "bold"))
        marco.config(bd=2, pady=5)
        marco.pack()

        # Formulário Cadastro de Estudantes
        label_email_institucional = Label(marco, text="Email Institucional: ", font=("Comic Sans", 10, "bold"))
        label_email_institucional.grid(row=0, column=0, sticky='e', padx=5, pady=8)
        self.email_institucional = Entry(marco, width=25)
        self.email_institucional.focus()
        self.email_institucional.grid(row=0, column=1, padx=5, pady=8)

        label_username = Label(marco, text="Username: ", font=("Comic Sans", 10, "bold"))
        label_username.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.username = Entry(marco, width=25)
        self.username.grid(row=1, column=1, padx=5, pady=8)

        label_password = Label(marco, text="Senha: ", font=("Comic Sans", 10, "bold"))
        label_password.grid(row=2, column=0, sticky='e', padx=5, pady=8)
        self.password = Entry(marco, width=25, show="*")
        self.password.grid(row=2, column=1, padx=5, pady=8)

        label_password_repetir = Label(marco, text="Repetir Senha: ", font=("Comic Sans", 10, "bold"))
        label_password_repetir.grid(row=3, column=0, sticky='e', padx=5, pady=8)
        self.repetir_password = Entry(marco, width=25, show="*")
        self.repetir_password.grid(row=3, column=1, padx=5, pady=8)
        
        # Marco pergunta
        marco_recovery_question = LabelFrame(root, text="Recuperar Senha", font=("Comic Sans", 10, "bold"), pady=10)
        marco_recovery_question.config(bd=2, pady=5)
        marco_recovery_question.pack()
        
        # Pergunta
        label_recovery_question = Label(marco_recovery_question, text="Pergunta para recuperar senha: ", font=("Comic Sans", 10, "bold"))
        label_recovery_question.grid(row=0, column=0, sticky='e', padx=5, pady=8)
        self.recovery_question = ttk.Combobox(marco_recovery_question, values=["Nome do seu PET?", "Nome da sua mãe?", "Cidade de nascimento?", "Time de Futebol Favorito?"], width=30, state="readonly")
        self.recovery_question.current(0)
        self.recovery_question.grid(row=0, column=1, padx=5, pady=8)
  
        label_recovery_answer = Label(marco_recovery_question, text="Resposta escolhida: ", font=("Comic Sans", 10, "bold"))
        label_recovery_answer.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.recovery_answer = Entry(marco_recovery_question, width=33)
        self.recovery_answer.grid(row=1, column=1, padx=5, pady=8)        
        
        label_advice = Label(marco_recovery_question, text="*A resposta inserida será sua chave de recuperação!", font=("Comic Sans", 9, "bold"), foreground="blue")
        label_advice.grid(row=2, column=0, columnspan=2, sticky='e', padx=5, pady=8)
        
        # Botões
        marco_botones = Frame(root)
        marco_botones.config(bg="#fff")
        marco_botones.pack(pady=10)

        button_cadastrar = Button(marco_botones, text="Cadastrar", bg="green", fg="white", font=("Comic Sans", 10, "bold"), command=self.registrar_estudante)
        button_cadastrar.grid(row=0, column=0, padx=5, pady=10)

        button_salir = Button(marco_botones, text="Sair", bg="red", fg="white", font=("Comic Sans", 10, "bold"), command=self.root.destroy)
        button_salir.grid(row=0, column=1, padx=5, pady=10)
    
    def validar_formulario_completo(self):
        # Verifica se todos os campos foram preenchidos
        if (self.email_institucional.get() == "" or self.username.get() == "" or
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

    def validar_email_institucional(self):
        # Verifica se o email institucional tem o formato correto
        email = self.email_institucional.get()
        if not email.endswith("@secretaria.piaget.com.br"):
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
        self.email_institucional.delete(0, END)
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.repetir_password.delete(0, END)
        self.recovery_answer.delete(0, END)
        self.email_institucional.focus()

    def registrar_estudante(self):
        if self.validar_formulario_completo() and self.validar_password() and self.validar_email_institucional():
            # Gerar um UUID4 para o usuario_id
            usuario_id = str(uuid4())
            usuario_id_estudante = str(uuid4())  # Gerar um UUID4 para o usuario_id_estudante
            role = "ADMINISTRADORES"

            # Definir transação para garantir a atomicidade das operações
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                try:
                    # Iniciar a transação
                    conn.execute("BEGIN TRANSACTION")

                    # Query para inserir dados na tabela Usuarios
                    query_usuarios = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)'
                    parameters_usuarios = (usuario_id,
                                        self.email_institucional.get(),
                                        self.username.get(),
                                        self.password.get(),
                                        self.recovery_question.get(),
                                        self.recovery_answer.get(),
                                        role)
                    cursor.execute(query_usuarios, parameters_usuarios)

                    # Query para inserir dados na tabela usuario_estudante
                    query_usuario_estudante = 'INSERT INTO usuario_admin VALUES(?, ?, ?)'
                    parameters_usuario_estudante = (usuario_id_estudante, usuario_id, is_active)  # Definir is_active como 1
                    cursor.execute(query_usuario_estudante, parameters_usuario_estudante)


                    # Commit da transação
                    conn.commit()

                    messagebox.showinfo("ADMIN CADASTRADO", f"""
                                        Username: {self.username.get()}
                                        Email institucional: {self.email_institucional.get()}
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
