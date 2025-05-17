#Define a static variable and access that through a class 
class MyClass:
    # Static (class) variable
    static_variable = 100

# Accessing the static variable directly through the class
print("Accessing through class:", MyClass.static_variable)

# Creating an instance of the class
obj = MyClass()

# Accessing the static variable through the instance
print("Accessing through object:", obj.static_variable)


#Define a static variable and access that through a instance
class MyClass:
    # Static (class-level) variable
    static_variable = "I am static!"

# Create an instance of the class
obj = MyClass()

# Access static variable through the instance
print("Accessed via instance:", obj.static_variable)


#Define a static variable and change within the instance
class MyClass:
    # Static (class-level) variable
    static_variable = 100

# Create two instances
obj1 = MyClass()
obj2 = MyClass()

# Modify the static variable using obj1
obj1.static_variable = 200  # This creates an instance variable in obj1

# Print values
print("obj1.static_variable:", obj1.static_variable) 
print("obj2.static_variable:", obj2.static_variable)  
print("MyClass.static_variable:", MyClass.static_variable)


#Define a static variable and change within the class
class MyClass:
    # Static variable (class-level)
    static_variable = 100

    @classmethod
    def change_static_variable(cls, new_value):
        cls.static_variable = new_value  # Changing static variable through class method

# Before change
print("Before change:", MyClass.static_variable)

# Call method to change the static variable
MyClass.change_static_variable(200)

# After change
print("After change:", MyClass.static_variable)

# Create an instance and access it
obj = MyClass()
print("Accessed through instance:", obj.static_variable)
