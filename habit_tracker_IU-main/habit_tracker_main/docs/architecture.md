# 🧱 Architecture & Design – Habit Tracker CLI App

This document describes the folder layout, class design, and storage structure of the Habit Tracker CLI application, implemented in both Python and Java.

---

## 🗂 Folder Structure

```
habit_tracker_IU/
├── habit_tracker_main/
│   ├── src/
│   │   ├── python/
│   │   │   ├── app.py                    # CLI launcher
│   │   │   └── modules/
│   │   │       ├── habit.py              # Habit class
│   │   │       └── habit_manager.py      # HabitManager logic
│   │   └── java/
│   │       ├── model/                    # Java Habit class
│   │       ├── service/                  # Java HabitManager class
│   │       ├── cli/                      # Java Main CLI
│   │       └── compiled/                 # Optional compiled .class output
│   │
│   ├── tests/
│   │   ├── python/
│   │   │   └── test_habit_manager.py     # Python unit tests
│   │   └── java/                         # (optional) Java JUnit tests
│   │
│   ├── data/
│   │   ├── habits.json                   # Used by Python app
│   │   └── habits.txt                    # Used by Java app
│   │
│   ├── docs/
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── usage.md
│   │   └── oop_explained.md
│   │
│   ├── setup.sh                          # Prints setup/run commands
│   └── README.md                         # Folder summary and nav help
├── README.md                             # Project-level overview
```

---

## 🔧 Class Design (Shared Concepts)

### 🧩 `Habit` Class

- Represents a single user-defined habit
- Stores:
  - `name` (e.g., "Exercise")
  - `category` (e.g., "Health")
  - `frequency` (e.g., "Daily")
  - List of check-ins (dates)

#### Python
```python
self.check_ins: list[date]
```

#### Java
```java
ArrayList<LocalDate> checkIns;
```

---

### 🧩 `HabitManager` Class

- Manages a collection of `Habit` objects
- Provides logic for:
  - Adding/removing habits
  - Checking in
  - Listing/streaks/analytics (basic)
  - Accessing a habit by name

---

### 🧠 CLI (Python and Java)

- All CLI logic is handled in:
  - `src/python/app.py`
  - `src/java/cli/Main.java`
- Users interact through menu-based input
- CLI calls only `HabitManager` methods (abstraction)

---

## 💾 File I/O Design

### Python
- Loads/saves habit objects to `data/habits.json`
- Format: list of dictionaries (habit name, dates)

### Java
- Uses `data/habits.txt` (plain text or custom serialization)
- Can be extended to use CSV or JSON later

---

## 🔄 Data Flow

```
User CLI Input → HabitManager → Habit → Updates stored → JSON/TXT file
```

---

## 🛠 Tools Used

- Python 3.10+
- Java 11+
- `unittest` for Python tests
- GitHub Codespaces for dev
- GitHub Actions (optional) for CI
