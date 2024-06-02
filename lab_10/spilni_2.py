import tkinter as tk

def change_color(event):
    if root["bg"] == "green":
        root["bg"] = "blue"
    else:
        root["bg"] = "green"

root = tk.Tk()
root.geometry("300x200")
root.title("Зміна кольору фону")

root["bg"] = "green"

root.bind("<Button-1>", change_color)

def on_enter(event):
    change_color(None)

root.bind("<Return>", on_enter)

root.mainloop()
