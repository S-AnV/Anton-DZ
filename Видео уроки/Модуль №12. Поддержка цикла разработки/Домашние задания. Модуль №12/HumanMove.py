class Student:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

# s1 = Student('Andrey')
#
# for i in range(10):
#     s1.walk()
# print(s1.distance)