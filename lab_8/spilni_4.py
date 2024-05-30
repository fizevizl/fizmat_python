class Worker:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name}, {self.age} {self.salary}"
    

w1 = Worker("Іван", 25, 1000)
w2 = Worker("Вася", 26, 2000)
print(w1)
print(w2)

print(f"сума віку {w1.name} і {w2.name}: {w1.age + w2.age}")
print(f"суму зарплат {w1.name} і {w2.name}: {w1.salary + w2.salary}")
