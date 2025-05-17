# Simulating two classes with constructors and methods, packages and usage.
class ClassA:
    def __init__(self):
        print("ClassA Constructor Called")

    def method_a(self):
        print("Method of ClassA called")


class ClassB:
    def __init__(self):
        print("ClassB Constructor Called")

    def method_b(self):
        print("Method of ClassB called")



def main():
    # Simulating import from package
    # from package import ClassA, ClassB

    # Creating object of ClassA and calling its method
    obj_a = ClassA()
    obj_a.method_a()

    print("---")

    # Creating object of ClassB and calling its method
    obj_b = ClassB()
    obj_b.method_b()

if __name__ == "__main__":
    main()
