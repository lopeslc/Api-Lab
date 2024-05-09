import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from uuid import uuid4
class CadastroProfessor:
    
    db_name = "data/database.db"
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Cadastrar PROFESSORES")
        self.root.resizable(False, False)
        self.root.config(bg="#fff", bd=10)
        
        # Titulo da pagina
        title_page = Label(root, text="AppLab PROFESSORES", fg="ORANGE", font=("Comic Sans", 13, "bold"), pady=5)
        title_page.pack()

        # Carregar logo da App
        imagen_registro = Image.open("assets/images/logo.png")
        nova_imagem = imagen_registro.resize((40,40))
        render = ImageTk.PhotoImage(nova_imagem)
        label_imagen = Label(root, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)
        
        # Marco
        marco = LabelFrame(root, text="dados do PROFESSOR", font=("Roboto", 10, "bold"))
        marco.config(bd=2, pady=5)
        marco.pack()

        # Formulário Cadastro de PROFESSORES
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
        self.recovery_question = ttk.Combobox(marco_recovery_question, values=["Nome do seu PET?", "Nome da sua mãe?", "Cidade de nacimento?", "Time de Futebol Favorito?"], width=30, state="readonly")
        self.recovery_question.current(0)
        self.recovery_question.grid(row=0, column=1, padx=5, pady=8)
  
        label_recovery_answer = Label(marco_recovery_question, text="Resposta escolhida: ", font=("Comic Sans", 10, "bold"))
        label_recovery_answer.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.recovery_answer = Entry(marco_recovery_question, width=33)
        self.recovery_answer.grid(row=1, column=1, padx=5, pady=8)        
        
        label_advice = Label(marco_recovery_question, text="*A resposta inserida será sua chave de recuperação!", font=("Comic Sans", 9, "bold"), foreground="blue")
        label_advice.grid(row=2, column=0, columnspan=2, sticky='e', padx=5)
        
        # Frame botões
        frame_botoes = Frame(root)
        frame_botoes.pack()

        # Botões
        botao_registrar = Button(frame_botoes, text="CADASTRAR", command=self.registrar_estudante, height=2, width=10, bg="green", fg="white", font=("Comic Sans", 10, "bold"))
        botao_registrar.grid(row=0, column=0, padx=5, pady=15)
        botao_limpar = Button(frame_botoes, text="LIMPAR", command=self.limpar_formulario, height=2, width=10, bg="gray", fg="white", font=("Comic Sans", 10, "bold"))
        botao_limpar.grid(row=0, column=1, padx=5, pady=15)
        botao_login = Button(frame_botoes, text="LOGIN", command=self.pagina_login_estudante, height=2, width=10, bg="red", fg="white", font=("Comic Sans", 10, "bold"))
        botao_login.grid(row=0, column=2, padx=5, pady=15)
   
    def pagina_login_estudante(self):
        pass
    
    def limpar_formulario(self):
        self.email_institucional.delete(0, END)
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.repetir_password.delete(0, END)
        self.recovery_question.set('')
        self.recovery_answer.delete(0, END)
    
    def executar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
        return result 
    
    def validar_formulario_completo(self):
        if len(self.email_institucional.get()) !=0 and len(self.username.get()) !=0 and len(self.password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.recovery_answer.get()) !=0:
            return True
        else:
            messagebox.showerror("⚠️ATENÇÃO ERRO AO COMPLETAR FORMULÁRIO!", "Complete Todos os campos do Formulário")
            return False
    
    def validar_password(self):
        if self.password.get() == self.repetir_password.get():
            return True
        else:
            messagebox.showerror("⚠️ATENÇÃO ERRO DE SENHA", "As senhas inseridas não coincidem")
            return False  

    def validar_email_institucional(self):
        email_institucional = self.email_institucional.get()
        # Adicione a função Buscar_email_institucional aqui se necessário
        dado = False  # A função Buscar_email_institucional ainda não está definida, então apenas defina dado como False temporariamente
        if not dado:
            return True
        else:
            messagebox.showerror("⚠️ATENÇÃO ERRO DE E-MAIL INSTITUCIONAL", "Email institucional para ESTUDANTE é inválido")
            return False  
    
    def registrar_estudante(self):
        if self.validar_formulario_completo() and self.validar_password() and self.validar_email_institucional():
            # Gerar um UUID4 para o id_usuario
            id = str(uuid4())
            role="PROFESSORES"
            # Query para inserir dados na tabela
            query = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)'
            parameters = (id, 
                          self.email_institucional.get(), 
                          self.username.get(), 
                          self.password.get(), 
                          self.recovery_question.get(), 
                          self.recovery_answer.get(),
                          role)
            
            # Executar a consulta
            self.executar_consulta(query, parameters)
            
            messagebox.showinfo("PROFESSOR CADASTRADO", f"""
                                Username: {self.username.get()}
                                Email institucional: {self.email_institucional.get()}
                                Senha: {self.password.get()}
                                Recuperação: {self.recovery_question.get()}
                                Resposta: {self.recovery_answer.get()}                       
                                """)
            print('USUARIO CRIADO')
            self.limpar_formulario()



def tela_cadastro_professor():
    root = Tk()
    app = CadastroProfessor(root)
    root.mainloop()
    
    
# tela_cadastro_estudante()
# tela_cadastro_admin()
# tela_cadastro_professor()