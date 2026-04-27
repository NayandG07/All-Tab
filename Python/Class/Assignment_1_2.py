# Assignment 1.2

#########################
# String Manipulation
#########################

print("STRING MANIPULATION EXERCISES\n")

### 1. Find the most frequent character in a given string
print("1. Most frequent character in a string:")
text = "programming is fun"

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_frequent = max(char_count, key=char_count.get)
print(f"The most frequent character is '{most_frequent}' with {char_count[most_frequent]} occurrences\n")

### 2. Check if two strings are anagrams
print("2. Check if strings are anagrams:")
str1 = "Listen"
str2 = "Silent"

sorted_str1 = sorted(str1.lower())
sorted_str2 = sorted(str2.lower())

if sorted_str1 == sorted_str2:
    print(f"'{str1}' and '{str2}' are anagrams\n")
else:
    print(f"'{str1}' and '{str2}' are not anagrams\n")

### 3. Capitalize first letter of each word
print("3. Capitalize first letter of each word:")
text = "hello world python programming"
capitalized = text.title()

print(f"Original: {text}")
print(f"Capitalized: {capitalized}\n")

### 4. Find the longest word in a string
print("4. Find the longest word:")
text = "Python is an amazing programming language"
words = text.split()
longest_word = max(words, key=len)

print(f"The longest word is '{longest_word}' with {len(longest_word)} characters\n")

### 5. Remove all punctuation marks
print("5. Remove punctuation marks:")
text = "Hello, World! How are you? This is a test... string."
clean_text = ""
for char in text:
    if char.isalnum() or char.isspace():
        clean_text += char

print(f"Original: {text}")
print(f"Without punctuation: {clean_text}\n")

#########################
# Lists
#########################

print("\nLIST EXERCISES\n")

### 1. Remove duplicates without changing order
print("1. Remove duplicates from list:")
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(f"Original list: {numbers}")
print(f"List without duplicates: {unique_list}\n")

### 2. Find intersection of two lists
print("2. Find intersection of lists:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = []
for item in list1:
    if item in list2:
        intersection.append(item)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}\n")

### 3. Check if a list is a sublist
print("3. Check if list is a sublist:")
main_list = [1, 2, 3, 4, 5, 6, 7]
sublist = [3, 4, 5]
is_sublist = False

for i in range(len(main_list) - len(sublist) + 1):
    if main_list[i:i+len(sublist)] == sublist:
        is_sublist = True
        break

print(f"Main list: {main_list}")
print(f"Sublist: {sublist}")
print(f"Is sublist present? {is_sublist}\n")

### 4. Find difference between two lists
print("4. Find difference between lists:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Elements in List 1 but not in List 2: {difference}\n")

### 5. Remove elements present in another list
print("5. Remove elements present in another list:")
main_list = [1, 2, 3, 4, 5, 6, 7]
remove_list = [3, 5, 7]
result = []
for item in main_list:
    if item not in remove_list:
        result.append(item)

print(f"Original list: {main_list}")
print(f"Elements to remove: {remove_list}")
print(f"Result after removal: {result}\n")

#########################
# Tuples
#########################

print("\nTUPLE EXERCISES\n")

### 1. Count occurrences in a tuple
print("1. Count occurrences in tuple:")
numbers = (1, 2, 3, 2, 4, 1, 5, 3)
count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(f"Tuple: {numbers}")
print("Occurrences:")
for num, count in count_dict.items():
    print(f"Number {num}: {count} times")
print()

### 2. Convert list of tuples to dictionary
print("2. Convert list of tuples to dictionary:")
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
result_dict = {}
for key, value in tuple_list:
    result_dict[key] = value

print(f"List of tuples: {tuple_list}")
print(f"Dictionary: {result_dict}\n")

### 3. Find smallest and largest elements
print("3. Find smallest and largest elements in tuple:")
numbers = (5, 2, 8, 1, 9, 3, 7)
smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Tuple: {numbers}")
print(f"Smallest element: {smallest}")
print(f"Largest element: {largest}\n")

### 4. Remove element from tuple
print("4. Remove element from tuple:")
numbers = (1, 2, 3, 4, 5)
element_to_remove = 3
temp_list = list(numbers)
temp_list.remove(element_to_remove)
result = tuple(temp_list)

print(f"Original tuple: {numbers}")
print(f"After removing {element_to_remove}: {result}\n")

### 5. Concatenate tuples
print("5. Concatenate tuples:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
result = tuple1 + tuple2 + tuple3

print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Tuple 3: {tuple3}")
print(f"Concatenated tuple: {result}\n")

#########################
# Dictionary
#########################

print("\nDICTIONARY EXERCISES\n")

### 1. Find keys with max and min values
print("1. Find keys with maximum and minimum values:")
scores = {"John": 85, "Alice": 92, "Bob": 78, "Emma": 95}
max_key = ""
min_key = ""
max_value = float('-inf')
min_value = float('inf')

for key, value in scores.items():
    if value > max_value:
        max_value = value
        max_key = key
    if value < min_value:
        min_value = value
        min_key = key

print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key} ({max_value})")
print(f"Key with minimum value: {min_key} ({min_value})\n")

### 2. Check if dictionaries are equal
print("2. Check if dictionaries are equal:")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "a": 1, "c": 3}
are_equal = True

if len(dict1) != len(dict2):
    are_equal = False
else:
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            are_equal = False
            break

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Are the dictionaries equal? {are_equal}\n")

### 3. Find union of dictionaries
print("3. Find union of dictionaries:")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
union_dict = {}

for key, value in dict1.items():
    union_dict[key] = value
for key, value in dict2.items():
    union_dict[key] = value

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Union: {union_dict}\n")

### 4. Remove specific key from dictionary
print("4. Remove specific key from dictionary:")
my_dict = {"name": "John", "age": 30, "city": "New York"}
key_to_remove = "age"

if key_to_remove in my_dict:
    del my_dict[key_to_remove]

print(f"Original dictionary: {{'name': 'John', 'age': 30, 'city': 'New York'}}")
print(f"After removing '{key_to_remove}': {my_dict}\n")

### 5. Create dictionary from two lists
print("5. Create dictionary from two lists:")
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
result_dict = {}

for i in range(len(keys)):
    result_dict[keys[i]] = values[i]

print(f"Keys list: {keys}")
print(f"Values list: {values}")
print(f"Resulting dictionary: {result_dict}\n")

### 6. Find keys with top three values
print("6. Find keys with top three values:")
scores = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Emma": 95,
    "Mike": 88
}

sorted_items = []
for key, value in scores.items():
    sorted_items.append((key, value))

for i in range(len(sorted_items)):
    for j in range(i + 1, len(sorted_items)):
        if sorted_items[i][1] < sorted_items[j][1]:
            sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

top_three = sorted_items[:3]

print(f"Dictionary: {scores}")
print("Top three scores:")
for key, value in top_three:
    print(f"{key}: {value}") 