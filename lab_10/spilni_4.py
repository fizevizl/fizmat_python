import tkinter as tk

def capitalize_first_letter():
    text = entry.get()
    capitalized_text = ' '.join([word.capitalize() for word in text.split()])
    label.config(text=capitalized_text)

root = tk.Tk()
root.title("Заміна перших літер на заголовні")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Замінити", command=capitalize_first_letter)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
