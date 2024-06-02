import tkinter as tk

def reverse_text():
    text = entry.get()
    reversed_text = text[::-1]
    label.config(text=reversed_text)

root = tk.Tk()
root.title("Реверс тексту")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Реверс", command=reverse_text)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
