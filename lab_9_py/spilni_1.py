import os

path =  os.path.dirname(os.path.realpath(__file__)) + "/"


with open(f"{path}t.txt", "r") as file_in:
    lines = file_in.readlines()

not_empty_lines = [line for line in lines if line.strip()]

with open(f"{path}g.txt", "w") as file_out:
    file_out.writelines(not_empty_lines)