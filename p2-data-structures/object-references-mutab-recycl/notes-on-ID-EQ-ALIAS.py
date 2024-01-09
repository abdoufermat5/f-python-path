from datetime import date

abdou = {
    "name": "Abdou Yaya Sadiakhou",
    "born": date(1998, 9, 21),
    "sex": "Male"
}

abdoufermat = abdou

hacker = {
    "name": "Abdou Yaya Sadiakhou",
    "born": date(1998, 9, 21),
    "sex": "Male"
}


def execute_id_eq():
    print("abdou == abdoufermat :", abdoufermat == abdou)
    # Output : True -> content are same
    print("-" * 30)
    print("abdoufermat is abdoufermat :", abdoufermat is abdou)
    # Output : True -> both are referencing the same object
    print("-" * 30)
    print("abdou == hacker :", abdou == hacker)
    # Output : True -> content are same
    print("-" * 30)
    print("abdou is hacker :", abdou is hacker)
    # Output : False -> they are not referencing the same object!


class Classroom:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students[:]

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, student):
        self.students.remove(student)


def execute_cr():
    import copy

    sts = Classroom(["Eve", "Mia", "Riley", "Lauren", "Johnny"])
    sts1 = copy.copy(sts)
    sts2 = copy.deepcopy(sts)
    print("==============Content of objects================")
    print(f"sts: {sts.students}"
          f"\nsts1: {sts1.students}"
          f"\nsts: {sts2.students}\n")
    print("Before modifications")
    print("========IDs of objects================")
    print(f"ID_sts: {id(sts)}"
          f"\nID_sts1: {id(sts1)}"
          f"\nID_sts2: {id(sts2)}\n")
    print(f"ID_sts.students: {id(sts.students)}"
          f"\nID_sts1.students: {id(sts1.students)}"
          f"\nID_sts2.students: {id(sts2.students)}")
    print("\nmodifying sts1 by dropping one item")
    sts.removeStudent("Mia")
    print()
    print("==============Content of objects================")
    print(f"sts: {sts.students}"
          f"\nsts1: {sts1.students}"
          f"\nsts: {sts2.students}\n")
    print("After modifications")
    print("========IDs of objects================")
    print(f"ID_sts: {id(sts)}\nID_sts1: {id(sts1)}\nID_sts2: {id(sts2)}\n")
    print(
        f"ID_sts.students: {id(sts.students)}"
        f"\nID_sts1.students: {id(sts1.students)}"
        f"\nID_sts2.students: {id(sts2.students)}")


# We should avoid initializing with mutable objects
class HauntedBus:
    def __init__(self, passengers=[]):  # this is a bad idea
        print("========IDs of passengers================")
        print(id(passengers))
        self.passengers = passengers

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


def execute_hb():
    bus = HauntedBus(["Emma", "Lana", "Abigail"])
    print("bus1 passengers", bus.passengers)
    bus.drop("Lana")
    bus.pick("Lauren")
    print("bus1 passengers", bus.passengers)
    # PROBLEMS
    bus2 = HauntedBus()  # self.passengers is empty list
    bus2.pick("Mia")
    print("bus2 passengers", bus2.passengers)
    bus3 = HauntedBus()  # self.passengers is still the same as in bus2 because the address of the empty
    # list (which is not empty now) still the same and it contains "Mia"
    print("bus3 passengers", bus3.passengers)
    bus3.pick("Lexi")
    print("bus 2 passengers", bus2.passengers)
    print("bus 3 passengers", bus3.passengers)
    print("bus2.passengers is bus3.passengers", bus2.passengers is bus3.passengers)


if __name__ == "__main__":
    execute_hb()
