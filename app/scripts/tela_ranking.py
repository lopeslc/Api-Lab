from tkinter import *
import tkinter as tk

def tela_ranking(root, email_institucional, role):
    
    root.geometry("500x500")
    root.config(bg="orange")
    root.resizable(width=False, height=False)
    
    label_titulo = tk.Label(root, text="AppLab-RANKING", fg="white", bg="orange", font=("Poppins", 32))	
    label_titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    

    root.mainloop()
    