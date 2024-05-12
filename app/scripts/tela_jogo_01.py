import tkinter as tk
from consultas import consulta_jogador  # Supondo que consulta_jogador está definido neste módulo
from consultas import separa_tupla_em_lista
from consultas import consulta_perguntas_vf

def mostrar_tela_quiz():
    root = tk.Tk()
    tela_quiz(root, "eu-estudante@estudante.piaget.com.br")
    root.mainloop()  # Adicionando mainloop() para manter a janela aberta

def tela_quiz(root, usernameJogador):
    root.geometry("500x700")
    root.config(bg="ORANGE")
    root.resizable(width=False, height=False)
    jogador = consulta_jogador(usernameJogador)
    lista_jogador = separa_tupla_em_lista(jogador)
    lista_perguntas = consulta_perguntas_vf()
    
    

    label_titulo = tk.Label(root, text=f"quiz do {(lista_jogador[2])}", fg="black", bg="orange" ,font=("Poppins", 32))
    label_score = tk.Label(root, text=f"SCORE TOTAL PRE-JOGO: {(lista_jogador[3])}", fg="black", bg="orange" ,font=("Poppins", 15))
    label_titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    label_score.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    
    for i in range(len(lista_perguntas)):
        label_pergunta = tk.Label(root, text=f"{(lista_perguntas[i][0])}", fg="black", bg="orange" ,font=("Poppins", 15))
        label_pergunta.place(relx=0.5, rely=0.3+(i*0.1), anchor=tk.CENTER)
        
        

mostrar_tela_quiz()
