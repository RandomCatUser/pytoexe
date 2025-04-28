import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import threading
import os
import webbrowser
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

GITHUB_URL = "https://github.com/RandomCatUser"

def open_github():
    webbrowser.open(GITHUB_URL)

def select_py_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        entry_py_file.delete(0, ctk.END)
        entry_py_file.insert(0, file_path)

def select_icon_file():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    if icon_path:
        entry_icon_file.delete(0, ctk.END)
        entry_icon_file.insert(0, icon_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output_folder.delete(0, ctk.END)
        entry_output_folder.insert(0, folder_path)

def clear_fields():
    entry_py_file.delete(0, ctk.END)
    entry_icon_file.delete(0, ctk.END)
    entry_output_folder.delete(0, ctk.END)
    entry_custom_args.delete(0, ctk.END)
    checkbox_console.deselect()
    checkbox_debug.deselect()

def run_conversion():
    py_file = entry_py_file.get()
    icon_file = entry_icon_file.get()
    output_folder = entry_output_folder.get()
    custom_args = entry_custom_args.get()
    include_console = checkbox_console.get()
    debug_mode = checkbox_debug.get()

    if not py_file.endswith('.py'):
        messagebox.showerror("Error", "Please select a valid Python (.py) file.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    try:
        progress_bar.set(0)
        label_progress.configure(text="Building EXE... Please wait ⚙️")

        command = [
            "pyinstaller",
            "--onefile",
            "--distpath", output_folder
        ]

        if not include_console:
            command.append("--noconsole")

        if debug_mode:
            command.append("--debug=all")

        if icon_file.endswith('.ico'):
            command += ["--icon", icon_file]

        command.append(py_file)

        # Simulate progress bar while PyInstaller runs
        def simulate_progress():
            while progress_bar.get() < 0.95:
                time.sleep(0.5)
                progress_bar.set(progress_bar.get() + 0.05)
                label_progress.configure(text=f"Building EXE... {int(progress_bar.get() * 100)}%")

        progress_thread = threading.Thread(target=simulate_progress)
        progress_thread.start()

        subprocess.run(command, check=True)

        progress_bar.set(1)
        label_progress.configure(text="✅ EXE Built Successfully!")
        messagebox.showinfo("Success", f"✅ Executable created successfully!\n\nSaved to: {output_folder}")

    except subprocess.CalledProcessError as e:
        progress_bar.set(0)
        label_progress.configure(text="❌ Build Failed.")
        messagebox.showerror("Error", f"Conversion failed!\n\n{e}")

def convert_to_exe():
    threading.Thread(target=run_conversion).start()

# GUI Setup
app = ctk.CTk()
app.title("Python to EXE Converter")
app.geometry("600x700")
app.resizable(False, False)

# ----------------- Top Bar -----------------
top_frame = ctk.CTkFrame(app, corner_radius=0, height=60)
top_frame.pack(fill="x")

label_title = ctk.CTkLabel(top_frame, text="🐍 Py2EXE Converter", font=("Arial Black", 26))
label_title.pack(side="left", padx=20, pady=10)

github_button = ctk.CTkButton(
    top_frame,
    text="🌐 GitHub",
    width=120,
    height=35,
    fg_color="transparent",
    hover_color="#1f6aa5",
    border_color="#1f6aa5",
    border_width=2,
    command=open_github
)
github_button.pack(side="right", padx=20)

# ----------------- Main Content -----------------
main_frame = ctk.CTkFrame(app, corner_radius=20)
main_frame.pack(pady=30, padx=30, fill="both", expand=True)

title_label = ctk.CTkLabel(main_frame, text="🔹 Select Files and Settings", font=("Arial", 20))
title_label.pack(pady=15)

# Python File Selection
frame_py_file = ctk.CTkFrame(main_frame, corner_radius=10)
frame_py_file.pack(pady=10, padx=20, fill="x")

entry_py_file = ctk.CTkEntry(frame_py_file, placeholder_text="Select Python (.py) file", height=40, corner_radius=10)
entry_py_file.pack(side="left", fill="x", expand=True, padx=(0, 10))

button_browse_py = ctk.CTkButton(frame_py_file, text="Browse", command=select_py_file, height=40, corner_radius=10)
button_browse_py.pack(side="right")

# Icon File Selection
frame_icon_file = ctk.CTkFrame(main_frame, corner_radius=10)
frame_icon_file.pack(pady=10, padx=20, fill="x")

entry_icon_file = ctk.CTkEntry(frame_icon_file, placeholder_text="Select Icon (.ico) file (optional)", height=40, corner_radius=10)
entry_icon_file.pack(side="left", fill="x", expand=True, padx=(0, 10))

button_browse_icon = ctk.CTkButton(frame_icon_file, text="Browse", command=select_icon_file, height=40, corner_radius=10)
button_browse_icon.pack(side="right")

# Output Folder Selection
frame_output_folder = ctk.CTkFrame(main_frame, corner_radius=10)
frame_output_folder.pack(pady=10, padx=20, fill="x")

entry_output_folder = ctk.CTkEntry(frame_output_folder, placeholder_text="Select Output Folder", height=40, corner_radius=10)
entry_output_folder.pack(side="left", fill="x", expand=True, padx=(0, 10))

button_browse_output = ctk.CTkButton(frame_output_folder, text="Browse", command=select_output_folder, height=40, corner_radius=10)
button_browse_output.pack(side="right")

# Custom Arguments
frame_custom_args = ctk.CTkFrame(main_frame, corner_radius=10)
frame_custom_args.pack(pady=10, padx=20, fill="x")

entry_custom_args = ctk.CTkEntry(frame_custom_args, placeholder_text="Custom PyInstaller Arguments", height=40, corner_radius=10)
entry_custom_args.pack(side="left", fill="x", expand=True, padx=(0, 10))

# Console and Debug Checkboxes
frame_options = ctk.CTkFrame(main_frame, corner_radius=10)
frame_options.pack(pady=10, padx=20, fill="x")

checkbox_console = ctk.CTkCheckBox(frame_options, text="Enable Console")
checkbox_console.pack(side="left", padx=(0, 10))

checkbox_debug = ctk.CTkCheckBox(frame_options, text="Debug Mode")
checkbox_debug.pack(side="left")

# Convert Button
button_convert = ctk.CTkButton(main_frame, text="✨ Convert to EXE ✨", command=convert_to_exe, font=("Arial Bold", 20), height=50, corner_radius=15)
button_convert.pack(pady=25)

# ----------------- Progress Bar -----------------
progress_bar = ctk.CTkProgressBar(main_frame, width=400, height=20, corner_radius=10)
progress_bar.pack(pady=10)
progress_bar.set(0)

label_progress = ctk.CTkLabel(main_frame, text="", font=("Arial", 14))
label_progress.pack()

# ----------------- Footer -----------------
footer_frame = ctk.CTkFrame(app, corner_radius=0, height=40)
footer_frame.pack(fill="x", side="bottom")

footer_label = ctk.CTkLabel(footer_frame, text="Made with ❤️ by RandomCatUser", font=("Arial", 12))
footer_label.pack(pady=10)

app.mainloop() 