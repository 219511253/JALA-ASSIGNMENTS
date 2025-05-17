#Write a function to add integer values of an array
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]
result = sum_of_array(numbers)
print("Sum of array:", result)

#Write a function to calculate the average value of an array of integers
def average_of_array(arr):
    if len(arr) == 0:
        return 0  
    total = sum(arr)  
    average = total / len(arr)  
    return average  
numbers = [10, 20, 30, 40, 50]
result = average_of_array(numbers)
print("Average of array:", result)

#Write a program to find the index of an array element
def find_index(arr, element):
    if element in arr:
        return arr.index(element)  
    else:
        return -1 
arr = [10, 20, 30, 40, 50]
element = 30
index = find_index(arr, element)
print("Index of", element, "is:", index)

#Write a function to test if array contains a specific value
def contains_value(arr, value):
    return value in arr 

arr = [10, 20, 30, 40, 50]
value = 30
result = contains_value(arr, value)
print("Does the array contain", value, "?", result)

#Write a function to remove a specific element from an array
def remove_element(arr, value):
    if value in arr:
        arr.remove(value)  #Removes the first occurrence of the value
        return arr
    else:
        return "Element not found in the array"
arr = [10, 20, 30, 40, 50]
value = 30
result = remove_element(arr, value)
print("Updated array:", result)

#Write a function to copy an array to another array
def copy_array(arr):
# Create a copy of the array using the copy() method
    new_array = arr.copy()  
    return new_array
arr = [10, 20, 30, 40, 50]
new_arr = copy_array(arr)
print("Original array:", arr)
print("Copied array:", new_arr)


#Write a function to insert an element at a specific position in the array
def insert_element(arr, value, position):
    if position < 0 or position > len(arr):
        return "Invalid position"  
    # Insert the value at the given position
    arr.insert(position, value)  
    return arr
arr = [10, 20, 30, 40, 50]
value = 25
position = 2
updated_arr = insert_element(arr, value, position)
print("Updated array:", updated_arr)

#Write a function to find the minimum and maximum value of an array
def find_min_max(arr):
    if len(arr) == 0:
        return "Array is empty"  
    min_value = min(arr)  
    max_value = max(arr)     
    return min_value, max_value
arr = [10, 20, 30, 40, 50]
min_value, max_value = find_min_max(arr)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

#Write a function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]  

arr = [10, 20, 30, 40, 50]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)

#Write a function to find the duplicate values of an array
def find_duplicates(arr):
    duplicates = [] 
    seen = set()     
    for num in arr:
        if num in seen:
            if num not in duplicates: 
                duplicates.append(num)
        else:
            seen.add(num)     
    return duplicates
arr = [10, 20, 30, 20, 40, 50, 10]
duplicates = find_duplicates(arr)
print("Duplicate values:", duplicates)

#Write a program to find the common values between two arrays
def find_common_values(arr1, arr2):
    # Use set intersection to find common values
    common_values = list(set(arr1) & set(arr2))
    return common_values
arr1 = [10, 20, 30, 40, 50]
arr2 = [30, 40, 50, 60, 70]
common_values = find_common_values(arr1, arr2)
print("Common values between the two arrays:", common_values)

# Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))
arr = [10, 20, 30, 20, 40, 50, 10]
unique_arr = remove_duplicates(arr)
print("Array with duplicates removed:", unique_arr)


#Write a method to find the second largest number in an array
def second_largest(arr):
    arr = list(set(arr))
    if len(arr) < 2:
        return None
    arr.sort(reverse=True)
    return arr[1]
arr = [10, 20, 30, 40, 50]
result = second_largest(arr)
print("Second largest number:", result)

#Write a method to find the second largest number in an array
def second_largest(arr):
    if len(arr) < 2:
        return None     
    first, second = float('-inf'), float('-inf')  
    for num in arr:
        if num > first:
            second = first  
            first = num  
        elif num > second and num != first:
            second = num    
    return second if second != float('-inf') else None  
arr = [10, 20, 30, 40, 50]
result = second_largest(arr)
print("Second largest number:", result)

#Write a method to find number of even number and odd numbers in an array
def count_even_odd(arr):
    even_count = 0  
    odd_count = 0   
    
    for num in arr:
        if num % 2 == 0: 
            even_count += 1
        else:  
            odd_count += 1    
    return even_count, odd_count  
arr = [10, 20, 33, 45, 50, 63, 70]
even_count, odd_count = count_even_odd(arr)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


#Write a function to get the difference of largest and smallest value
def difference_largest_smallest(arr):
    if len(arr) == 0:
        return "Array is empty"    
    largest = max(arr)  
    smallest = min(arr)     
    return largest - smallest  
arr = [10, 20, 30, 40, 50]
result = difference_largest_smallest(arr)
print("Difference between largest and smallest value:", result)


#Write a method to verify if the array contains two specified elements(12,23)
def contains_elements(arr, elem1, elem2):
    # Check if both elements are in the array
    return elem1 in arr and elem2 in arr
arr = [10, 12, 23, 30, 40, 50]
elem1 = 12
elem2 = 23
result = contains_elements(arr, elem1, elem2)
print("Array contains", elem1, "and", elem2, ":", result)

#Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    # Convert the array to a set to remove duplicates and convert it back to a list
    new_array = list(set(arr))
    return new_array
arr = [10, 20, 30, 20, 40, 50, 10]
new_arr = remove_duplicates(arr)
print("Array with duplicates removed:", new_arr)






