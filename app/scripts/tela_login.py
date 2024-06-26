import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import os
from scripts.tela_profile_estudante import tela_estudante
from scripts.tela_profile_admin import tela_admin
from scripts.tela_profile_professor import tela_professor

class TelaLogin(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
        self.master = master
        self.master.geometry("500x500")
        self.master.title("AppLab - Login")
        self.master.resizable(False, False)
        self.master.config(bg="#fff", bd=10)
        
        self.frame = tk.Frame(self.master, width=500, height=500, bg="orange")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.widget_1 = tk.Label(self.frame, text="AppLab Login", font=("Poppins", 32), bg="orange", fg="white")
        self.widget_1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        image = Image.open("assets/images/logo.png")
        resized_image = image.resize((220, 240))
        self.render = ImageTk.PhotoImage(resized_image)
        self.label_image = tk.Label(self.frame, image=self.render, bg="orange")
        self.label_image.image = self.render
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.label_email = tk.Label(self.frame, text="Email Institucional:", font=("Poppins", 12), bg="orange", fg="white")
        self.label_email.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        
        self.entry_email = tk.Entry(self.frame, font=("Poppins", 12))
        self.entry_email.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
        
        self.label_password = tk.Label(self.frame, text="Senha:", font=("Poppins", 12), bg="orange", fg="white")
        self.label_password.place(relx=0.3, rely=0.6, anchor=tk.CENTER)
        
        self.entry_password = tk.Entry(self.frame, font=("Poppins", 12), show="*")
        self.entry_password.place(relx=0.7, rely=0.6, anchor=tk.CENTER)
        
        self.button_submit = tk.Button(self.frame, text="Entrar", font=("Poppins", 12), bg="white", fg="orange", command=self.loguear)
        self.button_submit.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def validar_formulario_completo(self):
        # Verifica se todos os campos foram preenchidos
        if self.entry_email.get() == "" or self.entry_password.get() == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return False
        return True

    def executar_consulta(self, query, parameters=()):
        # Conectar-se ao banco de dados e executar a consulta
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters).fetchone()  # Use fetchone() to retrieve only one record
            conn.commit()
        return result

    def loguear(self):
        if self.validar_formulario_completo():
            result = self.executar_consulta1()  # Corrected function call
            if result:
                email_institucional = self.entry_email.get()
                messagebox.showinfo("Login", "Login efetuado com sucesso!")
                self.master.destroy()  # Switch to TelaProfile upon successful login
                myroot = tk.Tk()
                role = result[3]  # Access role from the result tuple
                if role == "ESTUDANTES":
                    tela_estudante(myroot, email_institucional, role)
                elif role == "ADMINISTRADORES":
                    tela_admin(myroot, email_institucional, role)
                elif role == "PROFESSORES":
                    tela_professor(myroot, email_institucional, role)
                else:
                    messagebox.showerror("Erro", "Email ou senha inválidos. Tente novamente.")
            else:
                messagebox.showerror("Erro", "Email ou senha inválidos. Tente novamente.")

    def executar_consulta1(self):
        input_email_institucional = self.entry_email.get()
        input_password = self.entry_password.get()
        consulta1 = "SELECT id, email_institucional, password, role FROM usuarios WHERE email_institucional = ? AND password = ?"
        parameters = (input_email_institucional, input_password)
        return self.executar_consulta(consulta1, parameters)
