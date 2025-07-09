import tkinter as tk
from tkinter import simpledialog

class ToDo:
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do List")
        self.window.geometry("500x600")
        self.window.configure(bg="#fce4ec")

        self.tasks = []
        self.last_selected = None

        self.heading = tk.Label(window, text=" To-Do List ", font=("Helvetica", 20, "bold"), bg="#fce4ec", fg="#880e4f")
        self.heading.pack(pady=15)

        self.entry = tk.Entry(window, font=("Helvetica", 13), width=25, bd=2)
        self.entry.pack(pady=5)

        self.listbox = tk.Listbox(window, font=("Helvetica", 12), width=30, height=12,
                                  selectbackground="#ce93d8", selectforeground="black", bg="#fff3e0", activestyle="none")
        self.listbox.pack(pady=10)

        self.listbox.bind('<<ListboxSelect>>', self.toggle_selection)

        self.add_btn = tk.Button(window, text="Add Task", command=self.add, bg="#81c784", fg="white", width=15)
        self.add_btn.pack(pady=4)

        self.edit_btn = tk.Button(window, text="Edit Task", command=self.edit, bg="#fff176", width=15)
        self.edit_btn.pack(pady=4)

        self.done_btn = tk.Button(window, text="Mark Done", command=self.mark_done, bg="#64b5f6", fg="white", width=15)
        self.done_btn.pack(pady=4)

        self.del_btn = tk.Button(window, text="Delete Task", command=self.delete, bg="#e57373", fg="white", width=15)
        self.del_btn.pack(pady=4)

        self.refresh_btn = tk.Button(window, text="Refresh", command=self.refresh_all, bg="#ba68c8", fg="white", width=15)
        self.refresh_btn.pack(pady=4)

    def toggle_selection(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if self.last_selected == index:
                self.clear_selection()
            else:
                self.last_selected = index

    def clear_selection(self):
        self.listbox.selection_clear(0, tk.END)
        self.last_selected = None

    def refresh_all(self):
        # Clear selection
        self.clear_selection()
        # Unmark all tasks as done
        for task in self.tasks:
            task["done"] = False
        self.refresh()

    def add(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.entry.delete(0, tk.END)
            self.refresh()

    def edit(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            current = self.tasks[index]["text"]
            updated = simpledialog.askstring("Edit Task", "Change task:", initialvalue=current)
            if updated:
                self.tasks[index]["text"] = updated
                self.refresh()

    def mark_done(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["done"] = True
            self.refresh()

    def delete(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks.pop(index)
            self.refresh()
    
    def refresh(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = f"✔️ {task['text']}" if task["done"] else task["text"]
            self.listbox.insert(tk.END, text)
root = tk.Tk()
app = ToDo(root)
root.mainloop()
