import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import json
import os

DATA_FILE = 'habits_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.data = load_data()

        self.habit_listbox = tk.Listbox(root, width=40, height=10)
        self.habit_listbox.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Adicionar Hábito", command=self.add_habit).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Marcar Como Feito", command=self.mark_done).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Mostrar Histórico", command=self.show_history).grid(row=0, column=2, padx=5)

        self.refresh_habit_listbox()

    def refresh_habit_listbox(self):
        self.habit_listbox.delete(0, tk.END)
        for habit in self.data.keys():
            self.habit_listbox.insert(tk.END, habit)

    def add_habit(self):
        habit_name = simpledialog.askstring("Adicionar Hábito", "Digite o nome do hábito:")
        if habit_name:
            if habit_name in self.data:
                messagebox.showwarning("Aviso", "Hábito já existe.")
            else:
                self.data[habit_name] = []
                save_data(self.data)
                self.refresh_habit_listbox()

    def mark_done(self):
        try:
            habit_index = self.habit_listbox.curselection()[0]
            habit_name = self.habit_listbox.get(habit_index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um hábito.")
            return
        today = datetime.now().strftime("%Y-%m-%d")
        if today in self.data[habit_name]:
            messagebox.showinfo("Info", f'Hábito "{habit_name}" já marcado hoje.')
        else:
            self.data[habit_name].append(today)
            save_data(self.data)
            messagebox.showinfo("Sucesso", f'Hábito "{habit_name}" marcado como feito hoje.')

    def show_history(self):
        try:
            habit_index = self.habit_listbox.curselection()[0]
            habit_name = self.habit_listbox.get(habit_index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um hábito para ver o histórico.")
            return
        dates = self.data.get(habit_name, [])
        if dates:
            history = "\n".join(dates)
        else:
            history = "Nenhuma realização registrada."
        messagebox.showinfo(f"Histórico de {habit_name}", history)

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
