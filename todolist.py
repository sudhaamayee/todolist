import tkinter as tk
from tkinter import messagebox, font
import random


# === Colors and Fonts ===
BG_COLOR = "#E37383"       # watermelon pink
BTN_COLOR = "#FF8DA1"      # light pink
LIST_BG = "#FFF5EE"
FONT_NAME = "Comic Sans MS" 
DOODLES = ["🍉", "🌼", "✨", "🍋", "🌀", "🎈", "🌟","🍓","🧃"]

# === Functions ===
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, f"🔸 {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "You forgot to type a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Hmm...", "No task selected.")

def mark_done(event=None):
    try:
        selected = listbox.curselection()[0]
        current = listbox.get(selected)
        if current.startswith("✅"):
            listbox.delete(selected)
            listbox.insert(selected, current[2:].strip())
        else:
            listbox.delete(selected)
            listbox.insert(selected, f"✅ {current}")
    except IndexError:
        pass

# === Main Window ===
root = tk.Tk()
root.title("📝To-Do List")
root.geometry("400x500")
root.configure(bg=BG_COLOR)
# === Canvas for Full Background ===
canvas = tk.Canvas(root, width=420, height=550, bg=BG_COLOR, highlightthickness=0)
canvas.place(x=0, y=0)

# 🎨 Scatter doodles across full canvas
for _ in range(60):
    doodle = random.choice(DOODLES)
    x = random.randint(0, 400)
    y = random.randint(0, 540)
    canvas.create_text(x, y, text=doodle, font=("Comic Sans MS", 12), fill="black")

frame_x, frame_y = 80, 40
frame_w, frame_h = 260, 470

for _ in range(30):
    doodle = random.choice(DOODLES)
    # Choose border side randomly
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        x = random.randint(frame_x, frame_x + frame_w)
        y = frame_y - 10
    elif side == 'bottom':
        x = random.randint(frame_x, frame_x + frame_w)
        y = frame_y + frame_h + 5
    elif side == 'left':
        x = frame_x - 10
        y = random.randint(frame_y, frame_y + frame_h)
    else:
        x = frame_x + frame_w + 5
        y = random.randint(frame_y, frame_y + frame_h)
    canvas.create_text(x, y, text=doodle, font=("Comic Sans MS", 12), fill="black")

# === Main Frame Over Canvas ===
frame = tk.Frame(canvas, bg=BG_COLOR, width=frame_w, height=frame_h)
frame.place(x=frame_x, y=frame_y)

# === Fonts ===
try:
    doodle_font = font.Font(family=FONT_NAME, size=12)
except:
    doodle_font = font.Font(size=12)

# === Heading ===
heading = tk.Label(root, text="🌿 My TO-DO List", bg=BG_COLOR, fg="#333", font=("Comic Sans MS", 18, "bold"))
heading.pack(pady=15)

# === Entry ===
entry = tk.Entry(root, font=doodle_font, bg=LIST_BG, width=26, justify="center")
entry.pack(pady=10)

# === Buttons ===
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack()

add_btn = tk.Button(button_frame, text="➕ Add", font=doodle_font, bg=BTN_COLOR, command=add_task)
add_btn.grid(row=0, column=0, padx=10)

del_btn = tk.Button(button_frame, text="❌ Delete", font=doodle_font, bg=BTN_COLOR, command=delete_task)
del_btn.grid(row=0, column=1, padx=10)

# === Task List ===
listbox = tk.Listbox(root, width=30, height=15, bg=LIST_BG, font=doodle_font, selectbackground="#caffbf")
listbox.pack(pady=20)
listbox.bind('<Double-Button-1>', mark_done)

# === Footer ===
footer = tk.Label(root, text="✨ Double-click task to mark complete!", bg=BG_COLOR, font=("Comic Sans MS", 10, "italic"))
footer.pack()

# === Run the App ===
root.mainloop()

