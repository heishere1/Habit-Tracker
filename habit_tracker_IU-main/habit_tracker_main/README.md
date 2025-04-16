# 📂 habit_tracker_main – Habit Tracker Core Project

Welcome! This is the main working folder for your **Habit Tracker CLI** application.  
It contains all the code, data, tests, and instructions to build and run your habit tracking app in both **Python** and **Java**.

---

## 🧠 What is This Project?

You are building a **Habit Tracker** – an app that helps users create habits (like "Drink Water"), check them off every day, and see their progress over time.

This version is:
- **CLI-based** (Command Line Interface – text-only)
- Made for learning **object-oriented programming (OOP)**
- Uses **Python** and **Java** to show how code works in two languages
- Runs in **GitHub Codespaces** or any terminal

---

## 🗂 Folder Overview

Here’s what’s inside `habit_tracker_main/`:

```
habit_tracker_main/
├── src/                  # Your main code (Python and Java)
├── tests/                # Unit tests for Python and Java
├── data/                 # Saved user habits (as JSON or TXT files)
├── docs/                 # Helpful documentation and learning notes
├── setup.sh              # Helper script that prints how to run everything
└── README.md             # You're reading this!
```

---

## 🛠 What is setup.sh?

This file is a **helper script**.

### What it does:
- Prints the commands you need to **run the Python app**
- Explains how to **compile and run Java**
- Shows how to **run tests**

### How to use it:
In the terminal (bottom of Codespaces), type:

```bash
bash setup.sh
```

💡 It will **not run the app for you** – it just prints the correct steps so you can understand and copy/paste them.

---

## 💡 What Do These Terms Mean?

- **CLI**: A Command Line Interface – you type things and see text back (no mouse or buttons)
- **Terminal**: A black/white window at the bottom of Codespaces where you type commands
- **Python**: A beginner-friendly language used for writing the app
- **Java**: Another popular programming language (used in Android, etc.)
- **Codespaces**: A cloud tool from GitHub that lets you code in a browser (no installs)
- **OOP**: Object-Oriented Programming – a way to build apps using objects and classes

---

## ✅ What You Should Do First

1. Open a terminal (in Codespaces, press **Ctrl + `** or use bottom panel)
2. Enter this folder:
```bash
cd habit_tracker_main
```
3. Run this to see what to do next:
```bash
bash setup.sh
```

---

## 📘 Where to Learn More

Inside the `docs/` folder:

| File                  | What It Explains                              |
|-----------------------|-----------------------------------------------|
| `requirements.md`     | What the app must do                          |
| `usage.md`            | How to run it and test it                     |
| `architecture.md`     | What files do what (structure overview)       |
| `oop_explained.md`    | Learn OOP with examples in Python and Java    |

---

## 📦 Want to Modify the App?

Edit these files:

- Python logic: `src/python/modules/`
- Java logic: `src/java/model/` and `src/java/service/`
- CLI menus: `src/python/app.py` or `src/java/cli/Main.java`
- Tests: `tests/python/test_habit_manager.py`

---

## 📣 Final Notes

- This is your practice ground! Try, break, and learn.
- Everything is designed to be beginner-friendly.
- If you're stuck, read the docs or run `setup.sh` again!

Happy learning 👩‍💻👨‍💻
