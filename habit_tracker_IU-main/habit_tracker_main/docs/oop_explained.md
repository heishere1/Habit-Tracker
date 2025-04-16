# 🧠 OOP Principles in Habit Tracker (Python + Java)

This project is designed as a hands-on way to **practice and understand object-oriented programming (OOP)** through the development of a CLI-based habit tracking system.

We use two languages — **Python and Java** — to demonstrate that OOP concepts are **universal** across languages.

---

## ✅ 1. Encapsulation

Encapsulation means that data (attributes) and logic (methods) are bundled inside objects. It also hides internal details from external code.

### Python
```python
class Habit:
    def __init__(self, name):
        self.name = name  # publicly accessible
        self.__check_ins = []  # private by convention
```

### Java
```java
public class Habit {
    private String name;
    public String getName() { return name; }  // controlled access
}
```

🔎 Where used:
- All class properties are stored inside objects.
- We expose only what is needed through methods like `getName()`, `checkIn()`.

---

## ✅ 2. Abstraction

Abstraction means simplifying interaction — users of the class don’t need to know how things work internally.

### Example
- CLI interacts with `HabitManager`, but doesn’t know how check-ins are stored.
- `HabitManager.getHabit(name)` gives a habit object, hiding internal list logic.

---

## ✅ 3. Composition

Composition is when one class is composed of other classes as attributes — it allows building complex systems out of simpler ones.

### Example

```python
class HabitManager:
    def __init__(self):
        self.habits = []  # List of Habit objects
```

```java
public class HabitManager {
    private ArrayList<Habit> habits;
}
```

🔎 Where used:
- `HabitManager` is composed of multiple `Habit` objects.
- This structure allows scaling easily to 1, 10, or 100 habits.

---

## ✅ 4. Modularity

Each class is implemented in its **own file** and has a single responsibility.

- `Habit`: stores and manages a single habit
- `HabitManager`: manages a collection of habits
- `Main.java` or `app.py`: user interface layer (CLI)

📁 Folders:
```
src/python/modules/habit.py
src/python/modules/habit_manager.py
src/java/model/Habit.java
src/java/service/HabitManager.java
```

---

## ✅ 5. Reusability

Each class is reusable in other apps. Example: you can reuse `HabitManager` in a web, mobile, or GUI version of the app — it doesn't rely on CLI-specific logic.

---

## ✅ 6. Extensibility

You can extend the app by:
- Adding more fields (e.g., reminders, deadlines)
- Creating subclasses (e.g., `HealthHabit`, `WorkHabit`)
- Overriding methods for analytics or UI rendering

---

## ✅ Summary Table

| Concept       | Where It Appears                    | Description                         |
|---------------|-------------------------------------|-------------------------------------|
| Encapsulation | `Habit`, `HabitManager`             | Methods control access to data      |
| Abstraction   | CLI only calls manager methods      | Logic hidden from users             |
| Composition   | `HabitManager` → list of `Habit`s   | Objects built from other objects    |
| Modularity    | Separate files per class            | Clean, maintainable code            |
| Reusability   | Core logic not tied to UI           | Usable in different projects        |
| Extensibility | Easy to add features or subclasses  | Built for future growth             |

---

## 💡 Final Tip for Students

When coding:
- Think of each class as a mini "machine" with inputs/outputs.
- Build clean APIs (methods) to communicate with each class.
- Avoid global state or giant functions — divide logic into logical parts.

