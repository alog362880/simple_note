import tkinter as tk
from tkinter import messagebox
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
)
""")
conn.commit()

# ================= FUNCTIONS =================
def fetch_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def add_task():
    title = entry.get()
    if title.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0))
    conn.commit()

    entry.delete(0, tk.END)
    update_listbox()

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = fetch_tasks()[selected]

        cursor.execute("DELETE FROM tasks WHERE id=?", (task[0],))
        conn.commit()

        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = fetch_tasks()[selected]

        cursor.execute("UPDATE tasks SET done=1 WHERE id=?", (task[0],))
        conn.commit()

        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def update_listbox():
    listbox.delete(0, tk.END)
    tasks = fetch_tasks()
    for task in tasks:
        status = "✔" if task[2] == 1 else "✘"
        listbox.insert(tk.END, f"[{status}] {task[1]}")

# ================= UI =================
root = tk.Tk()
root.title("To-Do App (SQLite)")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=25)
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=45, height=15)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

done_btn = tk.Button(btn_frame, text="Mark Done", command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

update_listbox()

root.mainloop()

# Close DB when app exits
conn.close()