from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pyttsx3 

engine = pyttsx3.init()
# عشان ياخد النص ويقرأه
def play_text():
    text = text_entry.get()
    if text.strip():
        engine.say(text)
        engine.runAndWait()
        # لو مفيش نص يطلع ايرور مسج
    else:
        messagebox.showwarning("warning", "Please enter text")
# عشان يمسح النص اللي مكتوب
def set_text():
    text_entry.delete(0, tk.END)
# عشان يقفل البرنامج
def exit_app():
    root.destroy()

# بندي عنوان و مقاسات
root = tk.Tk()
root.title("Salah Khaled")
root.geometry("400x300")


label = tk.Label(root, text="Enter your text here:", font=("Arial", 14))
label.pack(pady=10)
# مكان ادخال نص الكتابه 
text_entry = tk.Entry(root, font=("Arial", 14), width=30)
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), bg="lightgreen", command=play_text)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12), bg="lightblue", command=set_text)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="lightcoral", command=exit_app)
exit_button.grid(row=0, column=2, padx=10)


root.mainloop()