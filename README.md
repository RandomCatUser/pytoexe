# Python to EXE Converter

A simple tool to convert your Python `.py` scripts into standalone Windows `.exe` applications easily!

Repository: [RandomCatUser/pytoexe](https://github.com/RandomCatUser/pytoexe)

---

## ✨ Features
- Simple and clean interface
- One-click `.py` to `.exe` conversion
- Automatic handling of dependencies
- Lightweight and fast process
- No coding experience required for basic use

---

## 🚀 How It Works
This tool uses `PyInstaller` under the hood to bundle your Python scripts into executables. It manages:
- Compiling your `.py` files
- Packaging dependencies
- Creating a single `.exe` output

---

## 📥 How to Download

1. **Download ZIP File**  
   - Go to the [Repository Link](https://github.com/RandomCatUser/pytoexe).
   - Click the green `Code` button.
   - Select `Download ZIP`.
   - Extract the ZIP file anywhere on your PC.

   **OR**

2. **Clone using Git (if you have Git installed)**  
   Open Command Prompt and run:
   ```bash
   git clone https://github.com/RandomCatUser/pytoexe.git
   ```

---

## 🛠️ How to Install

1. **Install Python**  
   - Download and install Python 3.7+ from [python.org](https://www.python.org/downloads/).
   - Make sure to check "Add Python to PATH" during installation.

2. **Install Required Packages**  
   Open a terminal (Command Prompt) inside the project folder and run:
   ```bash
   pip install pyinstaller
   ```

   > **Note:** If you get errors about pip, update it first:
   > ```bash
   > python -m pip install --upgrade pip
   > ```

---

## 🧩 How to Use

### If the project has a Graphical User Interface (GUI):
1. Open the project folder.
2. Run the main script (example: `python converter.py` or double-click the `.py` if associated with Python).
3. A window will open.  
   - Select your Python `.py` script.
   - Click the **Convert** button.
4. After a few seconds, your `.exe` will be ready inside the `dist/` folder!

---

### If using Manual Command Line:

1. Open a terminal (Command Prompt) in the project directory.
2. Run:
   ```bash
   pyinstaller --onefile your_script.py
   ```
   Replace `your_script.py` with the filename you want to convert.

3. After completion:
   - Go to the `dist/` folder.
   - Your `.exe` file will be there!

---

## 📂 Folder Structure

```
pytoexe/
│
├── dist/        # Output folder for your .exe files
├── build/       # Temporary files (can be deleted after build)
├── your_script.spec # Spec file for advanced PyInstaller settings
├── converter.py # Main program (GUI launcher, if available)
└── README.md    # This file
```

---

## ⚙️ Requirements
- Windows 10 or 11 21H2 OR Grater
- Python 3.7 or higher
- PyInstaller package
- 4GB Ram
- Intel or AMD Cpu
- Git Cloner
---



## 🙌 Credits
Developed with ❤️ by [RandomCatUser].

---
