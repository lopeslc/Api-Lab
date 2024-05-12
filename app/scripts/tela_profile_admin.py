from tkinter import *
import tkinter as tk
from scripts.tela_ranking import mostrar_ranking
def click_ranking():
    root = tk.Tk()
    root.destroy()
    mostrar_ranking()
    
    

def tela_admin(root, email_institucional, role):
    
    
    root.geometry("500x700")
    root.config(bg="BLUE")
    root.resizable(width=False, height=False)
    
    label_titulo = tk.Label(root, text="ADMINISTRADORES")
    label_titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    btn_ranking = tk.Button(root, text="Ranking", command=click_ranking)
    btn_ranking.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    root.mainloop()
    
