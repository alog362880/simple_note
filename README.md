# To-Do App (SQLite + Tkinter)

A simple desktop to-do list app built with Python. Tasks are saved to a local SQLite database so they persist between sessions.

---

## Features

- Add tasks via a text input
- Mark tasks as done (✔)
- Delete tasks
- All tasks are stored in a local `tasks.db` SQLite file — nothing is lost when you close the app

---

## Requirements

- Python 3.x
- `tkinter` (bundled with most Python installations)
- `sqlite3` (bundled with Python — no install needed)

No third-party packages required.

---

## Usage

```bash
python todo.py
```

This will open the app window and create a `tasks.db` file in the same directory on first run.

---

## How It Works

- **Add a task** — type into the input box and click "Add Task"
- **Mark as done** — select a task in the list and click "Mark Done"
- **Delete a task** — select a task in the list and click "Delete Task"

Tasks are displayed with a status indicator:
- `[✔]` — completed
- `[✘]` — pending

---

## Project Structure

```
todo.py        # Main application file
tasks.db       # SQLite database (auto-created on first run)
```
