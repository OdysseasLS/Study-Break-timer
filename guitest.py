import tkinter as tk
import tkinter.ttk as ttk

WINDOW = tk.Tk()
label = tk.Label(
    text="Study-Break Timer",
    fg="white",
    bg="black",
    width=20,
    height=7
)  # consider ttk.Label() for themed label
label.pack()

wrk_time_label = tk.Label(text="Study time(in minutes)")
wrk_time_label.pack()
wrk_time_entry = tk.Entry()
wrk_time_entry.pack()

brk_time_label = tk.Label(text="Break time(in minutes)")
brk_time_label.pack()
brk_time_entry = tk.Entry()
brk_time_entry.pack()

button = tk.Button(
    text="Start",
    width=10,
    height=5,
    bg="green",
    fg="white"
)
button.pack()

WINDOW.mainloop()

wrk_time = wrk_time_entry.get()
brk_time = brk_time_entry.get()
print(wrk_time, brk_time)
