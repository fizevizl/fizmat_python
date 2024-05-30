import os

path =  os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"

with open(f"{path}text2.txt", "r", encoding="utf-8") as file_in:
    lines = file_in.readlines()

lines = [line.strip() for line in lines if line.strip()]
short_lines = min(lines, key=len)

print(f"Перший найкоротший рядок: {short_lines}")