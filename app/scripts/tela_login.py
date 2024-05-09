import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
import os
from tkinter import messagebox
class TelaLogin(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.db_name = os.path.join(os.path.dirname(__file__), "..",  "data", "database.db")
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
        self.label_image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

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

    def validar_conta(self):
        input_email_institucional = self.entry_email.get() 
        input_password = self.entry_password.get()

    def executar_consulta(self, query, parameters=()):
        # Conectar-se ao banco de dados e executar a consulta
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def executar_consulta1(self):
        input_email_institucional = self.entry_email.get() 
        input_password = self.entry_password.get()
        consulta1 = f"SELECT id, email_institucional, password, role FROM usuarios WHERE email_institucional = '{input_email_institucional}' AND password = '{input_password}'"
        return self.executar_consulta(consulta1)

    def executar_consulta2(self):
        

    def loguear(self):
        if self.validar_formulario_completo():
            result = self.executar_consulta1()
            if result:
                if result[0][2] == 'ESTUDANTES':
                    messagebox.showinfo("Login", "Login efetuado com sucesso!")
                    self.master.destroy()
                elif result[0][2] == 'ADMINISTRADORES':
                    messagebox.showinfo("Login", "Login efetuado com sucesso!")
                    self.master.destroy()
                elif result[0][2] == 'PROFESSORES':
                    messagebox.showinfo("Login", "Login efetuado com sucesso!")
                    self.master.destroy()
                else:
                    messagebox.showerror("Erro", "Email ou senha inválidos. Tente novamente.")
            else:
                messagebox.showerror("Erro", "Email ou senha inválidos. Tente novamente.")