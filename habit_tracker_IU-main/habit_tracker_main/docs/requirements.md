# 📋 Project Requirements – Habit Tracker CLI App

This file outlines the full feature set, development constraints, and technical expectations for the cross-platform Habit Tracker app built in Python and Java.

---

## ✅ Functional Requirements

### 1. Habit Management
- Add a new habit with:
  - Name
  - Category (e.g., Health, Productivity)
  - Frequency (Daily / Weekly / Custom)
- Remove a habit by name
- List all existing habits

### 2. Predefined Habits
- The app should include:
  - "Drink Water" (daily)
  - "Morning Stretching" (Mon–Fri)
  - "Read 10 Pages" (custom: 5 days/week)
- Users can activate or deactivate any predefined habit

### 3. Habit Check-In
- Mark a habit as completed for the current or specific date
- Store check-in dates persistently

### 4. Streak Tracking and Summaries
- Calculate:
  - Current streak (consecutive check-ins)
  - Longest streak
  - Missed days or completion ratio
- View summary from CLI interface

### 5. CLI Interface
- Menu-based interface (no GUI)
- Supports basic keyboard input
- Runs in Codespaces or any local terminal

### 6. Data Storage
- Python: store habit data as JSON (`data/habits.json`)
- Java: store habit data as plain text (`data/habits.txt`)
- No database or server required

---

## 🧪 Testing Requirements

- Python unit tests using `unittest`
- At minimum, test:
  - Habit creation
  - Adding/removing
  - Streak logic

---

## ⚙️ Technical Requirements

### Languages
- Python 3.10+
- Java 11+

### Dev Environment
- GitHub Codespaces compatible
- Single-click setup with `setup.sh`
- Works cross-platform (Linux/macOS/Windows)

### Version Control
- Git-based with hosted repository on GitHub
- Organized folder structure with markdown documentation

---

## 🚫 Non-Requirements

- No mobile or web interface
- No real-time notifications
- No persistence between devices (local only)
