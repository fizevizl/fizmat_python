import tkinter as tk
from tkinter import messagebox
import cmath

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Помилка", "a не може бути нулем у квадратному рівнянні.")
            return

        D = b**2 - 4*a*c

        if D > 0:
            root1 = (-b + cmath.sqrt(D)) / (2*a)
            root2 = (-b - cmath.sqrt(D)) / (2*a)
            result = f"Корені рівняння:\n x1 = {root1.real:.2f}\n x2 = {root2.real:.2f}"
        elif D == 0:
            root = -b / (2*a)
            result = f"Рівняння має один корінь:\n x = {root:.2f}"
        else:
            root1 = (-b + cmath.sqrt(D)) / (2*a)
            root2 = (-b - cmath.sqrt(D)) / (2*a)
            result = f"Рівняння має комплексні корені:\n x1 = {root1}\n x2 = {root2}"

        messagebox.showinfo("Розв'язок", result)
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа.")

root = tk.Tk()
root.title("Розв'язання квадратного рівняння")

label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = tk.Label(root, text="b:")
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_c = tk.Label(root, text="c:")
label_c.grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=5, pady=5)

solve_button = tk.Button(root, text="Розв'язати", command=solve_quadratic)
solve_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
