import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def quebrar_texto(texto, palavras_por_linha=10):
    palavras = texto.split()
    linhas = [" ".join(palavras[i:i+palavras_por_linha]) for i in range(0, len(palavras), palavras_por_linha)]
    return linhas

texto = "Sabemos que as vacinas são capazes de estimular a produção de anticorpos pelo corpo, protegendo-nos, portanto, de doenças. Graças a essa capacidade, dizemos que as vacinas garantem-nos:"
lista_alternativas = ["a) uma imunização passiva.", "b) uma imunização imediata.", "c) uma imunização prolongada.", "d) uma imunização ativa."]
explicacao = "Graças à capacidade da vacina de estimular a produção de anticorpos, dizemos que essa é uma forma de imunização ativa."
correta = "d"

def click_button(alternativa, correta):
    alternativa_questao = alternativa[0].lower()  # Corrigindo aqui
    if alternativa_questao == correta:  # Corrigindo aqui
        messagebox.showinfo("Resposta Correta", "Parabéns! Você acertou!\n\n" + explicacao)
    else:
        messagebox.showerror("Resposta Incorreta\n\n", "Ops! Você errou. Tente novamente!")

def quiz_1(texto, alternativas, correta, explicacao):
    root = tk.Tk()
    root.geometry("500x500")
    root.title("QUIZ FASE #01")
    root.resizable(False, False)
    root.config(bg="orange", bd=10)

    label_title = ttk.Label(root, text="QUIZ FASE #01", foreground="black", background="orange", font=("Comic Sans", 13, "bold"), padding=5)
    label_title.pack()

    linhas = quebrar_texto(texto)
    for linha in linhas:
        ttk.Label(root, text=linha, foreground="black", background="orange", font=("Comic Sans", 10)).pack(anchor="w")

    for alternativa in alternativas:
        ttk.Button(root, text=alternativa, command=lambda a=alternativa: click_button(a, correta)).pack()

    root.mainloop()

quiz_1(texto, lista_alternativas, correta, explicacao)
