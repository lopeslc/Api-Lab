import tkinter as tk
from scripts.tela_inicial import TelaInicial
from scripts.tela_login import TelaLogin
from scripts.tela_cadastro_aluno import CadastroEstudante

def main():
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()
