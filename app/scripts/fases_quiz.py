import tkinter as tk
from tkinter import ttk

def quebrar_texto(texto, palavras_por_linha=10):
    palavras = texto.split()
    linhas = [" ".join(palavras[i:i+palavras_por_linha]) for i in range(0, len(palavras), palavras_por_linha)]
    return linhas

def quiz_1():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("QUIZ FASE #01")
    root.resizable(False, False)
    root.config(bg="ORANGE", bd=10)
    
    label_title = ttk.Label(master=root, text="QUIZ FASE #01", foreground="black", background="orange", font=("Comic Sans", 13, "bold"), padding=5)
    label_title.pack()
    
    texto = "(UFMG) – A Campanha Nacional de Vacinação do Idoso, instituída pelo Ministério da Saúde do Brasil, vem-se revelando uma das mais abrangentes dirigidas à população dessa faixa etária. Além da vacina contra a gripe, os postos de saúde estão aplicando, também, a vacina contra pneumonia pneumocócica. Assinale a alternativa correta:"

    # Quebrar o texto em linhas
    linhas = quebrar_texto(texto)

    # Criar as labels para exibir as linhas
    for i, linha in enumerate(linhas):
        ttk.Label(root, text=linha, foreground="BLACK", background="ORANGE", font=("Comic Sans", 10)).pack(anchor="w")

    root.mainloop()

quiz_1()
