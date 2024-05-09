import tkinter as tk
from PIL import ImageTk, Image
from scripts.cadastros import CadastroEstudante
from scripts.tela_login import TelaLogin

class TelaInicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("AppLab")
        self.master.resizable(False, False)
        self.master.config(bg="#fff", bd=10)

        self.frame = tk.Frame(self.master, width=500, height=500, bg="orange")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.widget_1 = tk.Label(self.frame, text="AppLab", font=("Poppins", 32), bg="orange", fg="white")
        self.widget_1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        image = Image.open("assets/images/logo.png")
        resized_image = image.resize((220, 240))
        self.render = ImageTk.PhotoImage(resized_image)
        self.label_image = tk.Label(self.frame, image=self.render, bg="orange")
        self.label_image.image = self.render
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button_login = tk.Button(self.frame, text="Login", font=("Poppins", 16), bg="white", fg="orange", command=self.trocar_tela_login)
        self.button_login.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
        self.button_login = tk.Button(self.frame, text="Cadastrar Aluno", font=("Poppins", 16), bg="white", fg="orange", command=self.tela_cadastro_estudante)
        self.button_login.place(relx=0.6, rely=0.8, anchor=tk.CENTER)

    def trocar_tela_login(self):
        self.master.destroy()
        root = tk.Tk()
        app = TelaLogin(root)
        root.mainloop()
    
    def tela_cadastro_estudante(self):
         self.master.destroy()
         root = tk.Tk()
         app = CadastroEstudante(root)
         root.mainloop()
