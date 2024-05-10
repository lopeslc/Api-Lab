import tkinter as tk
from  scripts.tela_inicial import TelaInicial

def main():
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()
