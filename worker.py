def id_generator():
    gen_id = 1
    while True:
        gen_id += 1
        yield gen_id


class Worker:
    gen_id = id_generator()

    def set_id(self, new):
        self.__id = new

    def __init__(self, name, surname, depart, salary):
        self.name = name
        self.__id = next(self.gen_id)
        self.surname = surname
        self.depart = depart
        self.salary = float(salary)

    def get_id(self):
        return self.__id

    def __str__(self):
        output = ""
        output += f"ID: {self.get_id()}\n"
        output += f"Name: {self.name}\n"
        output += f"Surname: {self.surname}\n"
        output += f"Depart: {self.depart}\n"
        output += f"Salary: {self.salary}\n"
        return output

    @classmethod
    def input_worker(cls):
        name = input("Enter name: ")
        department = input("Enter department: ")
        surname = input("Enter surname: ")
        salary = float(input("Enter salary: "))
        return cls(name, surname, department, salary)
