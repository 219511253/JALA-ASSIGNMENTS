from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def sound(self):
        pass
    
    # Non-abstract method (can be inherited as is)
    def sleep(self):
        print("This animal is sleeping.")
    
# Subclass that implements the abstract method
class Dog(Animal):
    
    # Implementing the abstract method
    def sound(self):
        print("The dog barks.")
    
    # Method to create an instance of Animal inside the subclass (this will fail)
    def call_abstract_method(self):
        # Creating an instance of the abstract class Animal
        try:
            animal_instance = Animal()  # This will raise an error because Animal is abstract
            animal_instance.sound()     # Abstract method, but Animal cannot be instantiated
        except TypeError as e:
            print(f"Error: {e}")
    
    # Method to create an instance of the subclass and call the non-abstract method
    def call_non_abstract_method(self):
        # Creating an instance of the subclass (Dog)
        dog_instance = Dog()  # Instance of Dog class (subclass of Animal)
        dog_instance.sleep()  # Calling the non-abstract method inherited from Animal

# Main function to test the program
def main():
    # Creating an object of the subclass (Dog)
    dog = Dog()
    
    # Calling the non-abstract method from the parent class
    print("Calling non-abstract method sleep():")
    dog.sleep()  # Output: This animal is sleeping.
    
    # Calling the implemented abstract method from the subclass
    print("\nCalling implemented abstract method sound():")
    dog.sound()  # Output: The dog barks.
    
    # Calling the method that tries to create an Animal instance (which will fail)
    print("\nCalling method that tries to create an Animal instance:")
    dog.call_abstract_method()  # Will show an error message
    
    # Calling the method that creates a Dog instance and calls the non-abstract method
    print("\nCalling method that creates a Dog instance and calls non-abstract method:")
    dog.call_non_abstract_method()  # Output: This animal is sleeping.

# Run the main function
if __name__ == "__main__":
    main()
