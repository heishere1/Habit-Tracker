# Bash Cheat Sheet for GitHub Codespaces (Java + Python Projects)

This cheat sheet is designed to help you navigate and operate efficiently inside GitHub Codespaces, specifically when working on hybrid **Java + Python** projects.

---

## 📁 Directory Navigation

| Command | Description |
|--------|-------------|
| `pwd` | Print current working directory |
| `ls` | List files and folders |
| `ls -la` | List all files including hidden ones |
| `cd folder_name` | Move into a folder |
| `cd ..` | Move one directory up |
| `cd ~` | Go to the home directory |
| `tree -L 2` | Show folder structure (install with `sudo apt install tree`) |

---

## 🗂️ File & Folder Management

| Command | Description |
|--------|-------------|
| `mkdir new_folder` | Create a folder |
| `mkdir -p nested/folder/structure` | Create nested folders |
| `touch file.txt` | Create an empty file |
| `rm file.txt` | Delete a file |
| `rm -rf folder/` | Delete folder recursively |
| `cp file1 file2` | Copy file |
| `mv old new` | Move or rename file/folder |

---

## 🔍 File Viewing & Editing

| Command | Description |
|--------|-------------|
| `cat file.txt` | View file contents |
| `less file.txt` | View long files with scroll |
| `nano file.txt` | Edit file in terminal |
| `code file.py` | Open file in Codespaces editor |
| `code .` | Open entire project in editor |

---

## 🧪 Python Development

| Command | Description |
|--------|-------------|
| `python3 file.py` | Run a Python script |
| `python3 -m unittest discover tests` | Run all unittests |
| `pip install -r requirements.txt` | Install dependencies |
| `black src/` | Auto-format Python code |
| `pytest` | Run tests (if using Pytest) |

---

## ☕ Java Development

| Command | Description |
|--------|-------------|
| `javac MyClass.java` | Compile a Java class |
| `java MyClass` | Run compiled class |
| `javac -d out src/java/*.java` | Compile multiple Java files to `out/` |
| `java -cp out Main` | Run Java class from output folder |
| `./gradlew build` | Build project with Gradle (if used) |
| `mvn compile` | Compile Maven project (if used) |

---

## 🔧 Git Workflow (Codespaces Ready)

| Command | Description |
|--------|-------------|
| `git status` | View uncommitted changes |
| `git add .` | Stage all changes |
| `git commit -m "your message"` | Commit changes |
| `git push origin main` | Push to GitHub |
| `git pull origin main` | Pull latest from GitHub |
| `git stash` | Save current changes temporarily |
| `git stash pop` | Reapply stashed changes |
| `git reset --hard origin/main` | Force local copy to match GitHub (⚠️ destructive) |

---

## 🔍 Search & Find

| Command | Description |
|--------|-------------|
| `grep "search_term" file.txt` | Find text in a file |
| `grep -r "term" .` | Search in all files recursively |
| `find . -name "filename.py"` | Locate file by name |

---

## 🧰 Helpful Utilities

| Command | Description |
|--------|-------------|
| `chmod +x script.sh` | Make script executable |
| `./script.sh` | Run shell script |
| `sudo apt update && sudo apt install tree` | Install packages |
| `clear` | Clear terminal screen |
| `exit` | Exit terminal session |

---

## 🔄 GitHub Actions & Codespaces Integration

| Command | Description |
|--------|-------------|
| `ls .github/workflows/` | View GitHub Actions CI/CD scripts |
| `code .github/workflows/test.yml` | Open and edit CI test workflow |
| `git push` | Trigger GitHub Actions if configured |

---

## 🧠 Tips for Java + Python Project Layout

Example:

habit-tracker/                   #← This is your root project folder  
├── src/                         #← "src" stands for "source code"  
│   ├── java/                    #← Java folder (your Android app or Java logic)  
│   │   └── ...                  #← This is where your Java classes live  
│   └── python/                  #← Python folder (for analytics, backend logic)  
│       └── ...                  #← Python modules, services, app.py, etc.  
├── tests/                       #← Folder for all your tests  
│   ├── python/                  #← Python unit/integration tests  
│   └── java/                    #← Java test files (if needed)  
├── .github/workflows/           #← GitHub Actions folder for CI/CD pipelines  
├── README.md                    #← Project overview, usage, and setup instructions  
└── requirements.txt             #← Python dependencies list  

