class MyClass:
    # Method with one parameter
    def display(self, a):
        print(f"Method with one parameter: {a}")
    
    # Method with two parameters (using default argument)
    def display(self, a, b=None):
        if b is None:
            print(f"Method with one parameter: {a}")
        else:
            print(f"Method with two parameters: {a}, {b}")

# Main class to instantiate and call methods
if __name__ == "__main__":
    obj = MyClass()

    print("Calling method with one parameter:")
    obj.display(10)  # Calls method with one parameter

    print("\nCalling method with two parameters:")
    obj.display(10, 20)  # Calls method with two parameters
#Write two methods with the same name but different number of parameters of different data type and call the methods 
class MyClass:
    def show(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                print(f"One integer parameter: {args[0]}")
            elif isinstance(args[0], str):
                print(f"One string parameter: '{args[0]}'")
            else:
                print("Unsupported single parameter type.")
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], str):
                print(f"Integer and String: {args[0]}, '{args[1]}'")
            elif isinstance(args[0], str) and isinstance(args[1], int):
                print(f"String and Integer: '{args[0]}', {args[1]}")
            else:
                print("Unsupported combination of two parameters.")
        else:
            print("Unsupported number of parameters.")

# Main part
if __name__ == "__main__":
    obj = MyClass()

    print("Calling with one int:")
    obj.show(10)

    print("\nCalling with one string:")
    obj.show("Python")

    print("\nCalling with int and string:")
    obj.show(5, "Hello")

    print("\nCalling with string and int:")
    obj.show("Test", 99)


#Write two methods with the same name and same number of parameters of same type 
class MyClass:
    def process(self, value):
        if value < 0:
            print(f"Processing a negative number: {value}")
        elif value == 0:
            print("Processing zero")
        else:
            print(f"Processing a positive number: {value}")

# Main code
if __name__ == "__main__":
    obj = MyClass()

    print("Calling process with -5:")
    obj.process(-5)

    print("\nCalling process with 0:")
    obj.process(0)

    print("\nCalling process with 10:")
    obj.process(10)
