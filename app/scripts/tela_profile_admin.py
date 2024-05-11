from tkinter import *
import tkinter as tk

def tela_admin(root, email_institucional, role):
    
    root.geometry("500x700")
    root.config(bg="BLUE")
    root.resizable(width=False, height=False)
    
    label_titulo = tk.Label(root, text="ADMINISTRADORES")
    label_titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    root.mainloop()
    
