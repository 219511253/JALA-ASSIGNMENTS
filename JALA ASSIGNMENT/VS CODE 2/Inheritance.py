# Class A (Super Class)
class A:
    def __init__(self):
        self.data_a = "Class A data"

    def method_a1(self):
        print("Method A1 in Class A")

    def method_a2(self):
        print("Method A2 in Class A")

    def overridden_method(self):
        print("Overridden Method in Class A")


# Class B (Subclass of A)
class B(A):
    def __init__(self):
        super().__init__()
        self.data_b = "Class B data"

    def method_b1(self):
        print("Method B1 in Class B")

    def method_b2(self):
        print("Method B2 in Class B")

    def overridden_method(self):
        print("Overridden Method in Class B")


# Class C (Subclass of B)
class C(B):
    def __init__(self):
        super().__init__()
        self.data_c = "Class C data"

    def method_c1(self):
        print("Method C1 in Class C")

    def method_c2(self):
        print("Method C2 in Class C")

    def overridden_method(self):
        print("Overridden Method in Class C")


# Main function
def main():
    # Create objects of each class
    obj_a = A()
    obj_b = B()
    obj_c = C()

    # Call methods for each object
    print("\nCalling methods for object of Class A:")
    obj_a.method_a1()
    obj_a.method_a2()
    obj_a.overridden_method()

    print("\nCalling methods for object of Class B:")
    obj_b.method_b1()
    obj_b.method_b2()
    obj_b.overridden_method()

    print("\nCalling methods for object of Class C:")
    obj_c.method_c1()
    obj_c.method_c2()
    obj_c.overridden_method()

    # Call overridden method using superclass reference
    print("\nCalling overridden method with superclass reference (B):")
    super_b = A()
    super_b.overridden_method()

    print("\nCalling overridden method with superclass reference (C):")
    super_c = B()
    super_c.overridden_method()

    # Accessing data members
    print("\nAccessing data members (instance variables):")
    print("Class A data:", obj_a.data_a)
    print("Class B data:", obj_b.data_b)
    print("Class C data:", obj_c.data_c)


# Run the main function
if __name__ == "__main__":
    main()
