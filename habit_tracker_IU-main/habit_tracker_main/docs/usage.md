# 🚀 Usage Guide – Habit Tracker CLI App

This file explains how to **run, test, and explore** the Habit Tracker CLI application built in both **Python and Java**.

It assumes you're working inside a GitHub Codespaces environment or a terminal with Python 3.10+ and Java 11+ installed.

---

## 📘 What is This File?

This guide provides:
- **Step-by-step CLI usage**
- **Run and compile instructions**
- **How to test and validate logic**
- **How to use `setup.sh`**

Keep this open as a quick reference while using the project!

---

## 🧭 Project Entry Point

Navigate into the main project folder:

```bash
cd habit_tracker_IU/habit_tracker_main
```

---

## 🛠️ What is `setup.sh`?

This is a **helper script**. When you run it, it **prints clear instructions** on how to:

- Run the app in Python
- Compile and run the Java version
- Execute Python tests

It does **not run code** — it gives you commands that are safe to copy/paste.

### How to use it:
```bash
bash setup.sh
```

Output example:
```
▶ To run Python CLI:
  cd src/python && python3 app.py

▶ To run Java CLI:
  cd src/java/cli
  javac -d ../../compiled ../model/Habit.java ../service/HabitManager.java Main.java
  cd ../../compiled && java cli.Main
```

---

## 🐍 Running the App – Python

### Run the Python CLI:
```bash
cd src/python
python3 app.py
```

Follow the menu to:
- Add habits
- Check-in
- View summaries

### Python Data Storage
Habits are saved in:
```
data/habits.json
```

---

## ☕ Running the App – Java

### Compile Java code:
```bash
cd src/java/cli
javac -d ../../compiled ../model/Habit.java ../service/HabitManager.java Main.java
```

### Run the Java CLI:
```bash
cd ../../compiled
java cli.Main
```

### Java Data Storage
Habits are saved in:
```
data/habits.txt
```

---

## 🧪 Testing – Python Unit Tests

From `habit_tracker_main/` root:

```bash
touch tests/python/__init__.py  # Ensure it's importable
python3 -m unittest discover tests/python
```

Expected output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s
OK
```

---

## 🔍 Troubleshooting Tips

- If Python tests don’t run, check file names and import paths
- If Java doesn’t compile, ensure you're inside the correct folder
- If using Codespaces, wait for it to fully initialize before running

---

## 📦 Summary Commands

| Task                      | Command                                                  |
|---------------------------|-----------------------------------------------------------|
| Run Python CLI            | `cd src/python && python3 app.py`                        |
| Run Java CLI              | `cd src/java/cli && javac ... && java cli.Main`          |
| Run Python tests          | `python3 -m unittest discover tests/python`              |
| Use the helper script     | `bash setup.sh`                                          |

---

Happy coding and habit tracking!
