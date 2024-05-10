import tkinter as tk
import sqlite3
import os

class TelaProfile(tk.Frame):
    def __init__(self, master=None, email_institucional=None):
        super().__init__(master)
        self.db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
        self.master = master
        self.email_institucional = email_institucional

        # Fetch user details from the database based on email_institucional
        user_data = self.get_user_data(email_institucional)

        # Render profile based on user role
        if user_data:
            role = user_data[3]
            if role == 'ESTUDANTES':
                self.render_estudante_profile(user_data)
            elif role == 'ADMINISTRADORES':
                self.render_admin_profile(user_data)
            elif role == 'PROFESSORES':
                self.render_professor_profile(user_data)

    def get_user_data(self, email_institucional):
        query = "SELECT * FROM usuarios WHERE email_institucional = ?"
        result = self.executar_consulta(query, (email_institucional,))
        return result.fetchone()

    def render_estudante_profile(self, user_data):
        # Implement rendering logic for student profile
        self.master.destroy()
        root = tk.Tk()
        root.resizable(False, False)
        root.config(bg="#fff", bd=10)
        root.geometry("500x500")
        label_profile_estudantes = tk.Label(text="profile estudantes", font=("Comic Sans", 13, "bold"), pady=5).pack()
                

    def render_admin_profile(self, user_data):
        # Implement rendering logic for admin profile
        pass

    def render_professor_profile(self, user_data):
        # Implement rendering logic for professor profile
        pass

    def executar_consulta(self, query, parameters=()):
        # Connect to the database and execute the query
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
