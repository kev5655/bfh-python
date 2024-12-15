

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
bool_list = [item for item in fruit if item[0] == "A"]
print(bool_list)

bool_list = [item.upper() for item in fruit if item[0] == "A"]
print(bool_list)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Include only even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


words = ["hello", "world", "python", "rocks"]
# Convert words starting with 'p' to uppercase
uppercase_p = [word.upper() for word in words if word[0] == "p"]
print(uppercase_p)  # Output: ['PYTHON']


names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Include names with more than 3 characters
long_names = [name for name in names if len(name) > 3]
print(long_names)  # Output: ['Alice', 'Charlie', 'David']


# Generate squares of numbers from 1 to 10 that are greater than 25
squares = [x**2 for x in range(1, 11) if x**2 > 25]
print(squares)  # Output: [36, 49, 64, 81, 100]


text = "This is a sample sentence."
# Extract vowels
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)  # Output: ['i', 'i', 'a', 'a', 'e', 'e', 'e']


grades = {"Alice": 85, "Bob": 76, "Charlie": 90, "David": 65}
# Include students with grades above 80
high_scorers = [name for name, grade in grades.items() if grade > 80]
print(high_scorers)  # Output: ['Alice', 'Charlie']


nested_list = [[1, 2], [3, 4], [5, 6]]
# Flatten the nested list
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]


words = ["apple", "banana", "cherry", "date", "grape"]
# Include words ending with 'e'
words_ending_with_e = [word for word in words if word.endswith("e")]
print(words_ending_with_e)  # Output: ['apple', 'date', 'grape']


# Generate multiples of 3 from 1 to 30
multiples_of_3 = [x for x in range(1, 31) if x % 3 == 0]
print(multiples_of_3)  # Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


animals = ["dog", "cat", "elephant", "tiger", "lion"]
# Include animals with more than 3 letters and capitalize them
capitalized_animals = [animal.upper() for animal in animals if len(animal) > 3]
print(capitalized_animals)  # Output: ['ELEPHANT', 'TIGER', 'LION']
