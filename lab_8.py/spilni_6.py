class Worker:
    def __init__(self, name="", age=0, salary=0) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name}, {self.age} {self.salary}"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def checkAge(self, age):
        return 1 <= age <= 100

    def setAge(self, age):
        if self.checkAge(age=age):
            self.age = age

    def getAge(self):
        return self.age

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


w1 = Worker()
w2 = Worker()

w1.setName("Іван")
w1.setAge(101)
w1.setSalary(1000)

w2.setName("Вася")
w2.setAge(34)
w2.setSalary(2000)

print(w1.getAge() + w2.getAge())
print(w1.getSalary() + w2.getSalary())
