

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
bool_list = [item[0] == "A" for item in fruit]
print(bool_list)


numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']


words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 6, 6]


numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]


words = ["cat", "dog", "fish"]
prefixed_words = [f"my-{word}" for word in words]
print(prefixed_words)  # Output: ['my-cat', 'my-dog', 'my-fish']


numbers = [1, 2, 3, 4, 5]
tripled_odds = [num * 3 for num in numbers if num % 2 != 0]
print(tripled_odds)  # Output: [3, 9, 15]


numbers = [1, 2, 3, 4]
tuples = [(num, num ** 2) for num in numbers]
print(tuples)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16)]


nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]


words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c']


words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}


words = ["hello", "world", "python"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)  # Output: ['olleh', 'dlrow', 'nohtyp']


table = [i * j for i in range(1, 4) for j in range(1, 4)]
print(table)  # Output: [1, 2, 3, 2, 4, 6, 3, 6, 9]


list1 = ["A", "B", "C"]
list2 = [1, 2, 3]
pairs = [(x, y) for x in list1 for y in list2]
# Output: [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3), ('C', 1), ('C', 2), ('C', 3)]
print(pairs)


numbers = [1, 2, 3, 4, 5]
replaced = [num if num % 2 == 0 else -1 for num in numbers]
print(replaced)  # Output: [-1, 2, -1, 4, -1]
