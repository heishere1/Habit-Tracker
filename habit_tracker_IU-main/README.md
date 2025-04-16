# Habit Tracker CLI (Python + Java)

A cross-platform command-line habit tracking application built for educational purposes, using both Python and Java.  
This project helps learners understand object-oriented programming (OOP), CLI design, unit testing, and GitHub-based workflows.

---

## 📌 Project Description

The Habit Tracker allows users to define personal habits, track their completion over time, and review analytics such as streaks and success rates.  
The project is CLI-only (no GUI) and designed to run in GitHub Codespaces or on any local machine with Java and Python installed.

It’s ideal for:

- Students learning Java and Python
- Developers practicing clean architecture and CLI tools
- Classroom or workshop projects

---

## ✨ Features

- Add new habits with categories and frequency
- Predefined habits (e.g., Drink Water, Morning Stretching)
- Manual daily check-ins
- Streak and completion tracking
- CLI-based interface (menu-driven)
- Implementation in both Python and Java
- Simple file-based storage (no database)
- Python unit tests using `unittest`

---

## 📁 Project Structure

```
habit_tracker_IU/
├── habit_tracker_main/                   # Core application folder
│
│   ├── src/                              # Source code (split into Python and Java)
│   │   ├── python/                       # Python version of the Habit Tracker
│   │   │   ├── app.py                    # Main CLI interface for Python
│   │   │   └── modules/                  # Core logic and classes
│   │   │       ├── habit.py              # Habit class (Python)
│   │   │       └── habit_manager.py      # HabitManager class (Python)
│   │   │
│   │   └── java/                         # Java version of the Habit Tracker
│   │       ├── model/                    # Core model: Habit class (Java)
│   │       │   └── Habit.java
│   │       ├── service/                  # Business logic layer: HabitManager class (Java)
│   │       │   └── HabitManager.java
│   │       ├── cli/                      # Java CLI entry point
│   │       │   └── Main.java
│   │       └── compiled/                 # Compiled .class files (optional output folder)
│
│   ├── tests/                            # All test files
│   │   ├── python/                       # Python tests
│   │   │   └── test_habit_manager.py     # Python unittest class
│   │   └── java/                         # (Optional) Java test stubs
│   │       └── TestHabitManager.java
│
│   ├── data/                             # Data storage (auto-generated)
│   │   ├── habits.json                   # JSON used by Python for saving/loading habits
│   │   └── habits.txt                    # Plain text used by Java (optional format)
│
│   ├── docs/                             # Markdown documentation
│   │   ├── requirements.md               # Full functional and non-functional specs
│   │   ├── architecture.md               # Folder and class structure + design logic
│   │   ├── usage.md                      # How to run everything: Python + Java
│   │   └── oop_explained.md              # Explanation of OOP principles in both languages
│
│   ├── setup.sh                          # Bash script that prints out how to run and test everything
│   └── README.md                         # Short intro to habit_tracker_main folder
│
├── README.md                             # 🔥 Main project overview and entry point

```

- **Python** code is inside `src/python/`
- **Java** code is inside `src/java/`
- **Docs** are in `docs/` and explain usage, architecture, OOP principles

---

## ⚙️ Setup & Running the Project

This project includes a setup helper script:

### `setup.sh`

This script prints clear terminal instructions on how to:

- Run the Python CLI
- Run the Python unit tests
- Compile and run the Java CLI

### 🔧 How to use it:

```bash
bash setup.sh
```

> 💡 The script does not execute the code directly — it tells you **exactly what to run**.

---

## ▶ How to Use the App

See [`docs/usage.md`](./habit_tracker_main/docs/usage.md) for full instructions.

Quick overview:

### Python:

```bash
cd habit_tracker_main/src/python
python3 app.py
```

Run tests:
```bash
python3 -m unittest discover ../tests/python
```

### Java:

```bash
cd habit_tracker_main/src/java/cli
javac -d ../../compiled ../model/Habit.java ../service/HabitManager.java Main.java
cd ../../compiled
java cli.Main
```

---

## 🔍 Learn OOP by Example

This project is a practical exercise in OOP design:

- Encapsulation (private data, public methods)
- Composition (managing multiple habits)
- Modularity (separate files/classes)
- Works identically in both Python and Java

👉 See [`docs/oop_explained.md`](./habit_tracker_main/docs/oop_explained.md)

---

## 📘 Educational Value

This project is part of a university-level software engineering course.  
It teaches:

- Python & Java CLI app building
- Unit testing
- GitHub best practices
- Modular clean code structure
- Cross-language thinking

---

