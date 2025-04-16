#!/bin/bash

# ---------------------------------------------
# setup.sh – Instructional script for beginners
# ---------------------------------------------
# This script does NOT run the Habit Tracker.
# It simply prints clear terminal commands that
# you can copy and paste to:
# - Run the app in Python
# - Run the app in Java
# - Run automated Python tests
#
# This helps beginners get started quickly without guessing commands.
#
# 🧑‍💻 HOW TO USE THIS FILE:
#
# 1. Open your GitHub Codespaces terminal (bottom pane)
# 2. Navigate to the habit_tracker_main folder:
#       cd habit_tracker_main
# 3. Run this script by typing:
#       bash setup.sh
# 4. Follow the printed steps. Copy-paste them one at a time.
# 5. If you get stuck, read the README.md or usage.md in the docs folder.
#
# 💡 You can use this in:
# - GitHub Codespaces (recommended)
# - Local VS Code terminal
# - Git Bash / WSL / Linux / macOS Terminal
#
# Note: This script prints instructions. It does not run the app by itself.

echo ""
echo "🔧 Setting up Habit Tracker CLI project..."
echo ""

# Python CLI Instructions
echo "▶ To run Python CLI:"
echo "  cd src/python && python3 app.py"
echo ""

# Python Test Instructions
echo "▶ To run Python tests:"
echo "  cd habit_tracker_main"
echo "  touch tests/python/__init__.py"
echo "  python3 -m unittest discover tests/python"
echo ""

# Java Compile Instructions
echo "▶ To compile Java:"
echo "  cd src/java/cli"
echo "  javac -d ../../compiled ../model/Habit.java ../service/HabitManager.java Main.java"
echo ""

# Java Run Instructions
echo "▶ To run Java:"
echo "  cd ../../compiled && java cli.Main"
echo ""

echo "✅ Setup instructions printed. You can now copy/paste them to get started."
