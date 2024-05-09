from tkinter import *
from tkinter import ttk, messagebox

class CadastroEstudante:
    
    db_name = "app/data/database.db"
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x700")
        self.root.title("Cadastrar Estudante")
        self.root.resizable(False, False)
        self.root.config(bg="#fff", bd=10)
        
        # Titulo da pagina
        title_page = Label(root, text="AppLab Estudantes", fg="ORANGE", font=("Comic Sans", 13, "bold"), pady=5)
        title_page.pack()

        # Carregar logo da App
        self.logo = PhotoImage(file="assets/images/logo.png")
        label_imagen = Label(root, image=self.logo)
        label_imagen.pack(pady=5)
        
        # Marco
        marco = LabelFrame(root, text="dados del Alumno", font=("Roboto", 10, "bold"))
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
            messagebox.showerror("⚠️ATENÇÃO ERRO NAS SENHAS", "As senhas não são iguais. Tente novamente.")
            return False
    
    def registrar_estudante(self):
        if self.validar_formulario_completo():
            if self.validar_password():
                query = 'INSERT INTO usuarios (email_institucional, username, password, question_recovery, answer_recovery) VALUES (?, ?, ?, ?, ?)'
                parameters = (self.email_institucional.get(), self.username.get(), self.password.get(), self.recovery_question.get(), self.recovery_answer.get())
                self.executar_consulta(query, parameters)
                messagebox.showinfo("✅ CADASTRO REALIZADO", "Cadastro Realizado com Sucesso!")
                self.limpar_formulario()
                self.pagina_login_estudante()

root = Tk()
app = CadastroEstudante(root)
root.mainloop()