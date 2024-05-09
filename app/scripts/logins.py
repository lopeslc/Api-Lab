import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

class LoginWindow:
    db_name = "app/data/database.db"
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        
        # Variáveis de controle
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        # Label e Entry para email
        tk.Label(root, text="Email Institucional:").pack()
        tk.Entry(root, textvariable=self.email_var).pack()
        
        # Label e Entry para senha
        tk.Label(root, text="Senha:").pack()
        tk.Entry(root, textvariable=self.password_var, show="*").pack()
        
        # Botão de login
        tk.Button(root, text="Login", command=self.login).pack(pady=10)
        
    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()
        
        # Verificar credenciais na base de dados
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Usuarios WHERE email = ? AND password = ?", (email, password))
            user = cursor.fetchone()
            cursor.close()
        
        if user:
            role = user[3]
            if role == "ESTUDANTES":
                self.open_student_profile_window()
            elif role == "ADMINISTRADORES":
                self.open_admin_profile_window()
            elif role == "PROFESSORES":
                self.open_teacher_profile_window()
        else:
            messagebox.showerror("Erro de Login", "Credenciais inválidas.")
            
    def open_student_profile_window(self):
        # Implemente a janela do perfil do estudante aqui
        messagebox.showinfo("Perfil de Estudante", "Bem-vindo! Este é o perfil do estudante.")
        
    def open_admin_profile_window(self):
        # Implemente a janela do perfil do administrador aqui
        messagebox.showinfo("Perfil de Administrador", "Bem-vindo! Este é o perfil do administrador.")
        
    def open_teacher_profile_window(self):
        # Implemente a janela do perfil do professor aqui
        messagebox.showinfo("Perfil de Professor", "Bem-vindo! Este é o perfil do professor.")

def chama_login():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()


chama_login()