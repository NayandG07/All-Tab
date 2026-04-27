## String Manipulation:

### Qs.1 Write a Python program to find the most frequent character in a given string.


```python
text = "programming is fun"

char_count = {}
for i in text:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

most_frequent = max(char_count, key=char_count.get)
print(f"The most frequent character is '{most_frequent}' with {char_count[most_frequent]} occurrences\n")
print(char_count)
```

    The most frequent character is 'r' with 2 occurrences
    
    {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, ' ': 2, 's': 1, 'f': 1, 'u': 1}
    

### Qs.2 Write a Python program to check if two strings are anagrams of each other, considering case sensitivity.


```python
str1 = "Listen"
str2 = "Silent"

sorted_str1 = sorted(str1.lower())
sorted_str2 = sorted(str2.lower())

if sorted_str1 == sorted_str2:
    print(f"'{str1}' and '{str2}' are anagrams\n")
else:
    print(f"'{str1}' and '{str2}' are not anagrams\n")
```

    'Listen' and 'Silent' are anagrams
    
    

### Qs.3 Write a Python program to capitalize the first letter of each word in a given string.


```python
text = "hello world python programming"
capitalized = text.title()

print("Original text:", text)
print("Capitalized text:", capitalized)
```

    Original text: hello world python programming
    Capitalized text: Hello World Python Programming
    

### Qs.4 Write a Python program to find the longest word in a given string.


```python
text = "Python is an amazing programming language"
words = text.split()
longest_word = max(words, key=len)

print(f"The longest word is '{longest_word}' with {len(longest_word)} characters\n")
```

    The longest word is 'programming' with 11 characters
    
    

### Qs.5 Write a Python program to remove all puncutation marks from a given string.


```python
text = "Hello, World! How are you? This is a test... string."
punctuation = ""
for i in text:
    if i.isalnum() or i.isspace():
        punctuation += i

print("Original text:", text)
print("Without punctuation:", punctuation)
```

    Original text: Hello, World! How are you? This is a test... string.
    Without punctuation: Hello World How are you This is a test string
    

## Lists:

### Qs.1 Write a Python program to remove duplicates from a list without changing its order.


```python
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("Original list:", numbers)
print("List without duplicates:", new_list)
```

    Original list: [1, 2, 3, 2, 4, 1, 5, 3]
    List without duplicates: [1, 2, 3, 4, 5]
    

### Qs.2 Write a Python program to find the intersection of two lists.


```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = []
for i in list1:
    if i in list2:
        intersection.append(i)

print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", intersection)
```

    List 1: [1, 2, 3, 4, 5]
    List 2: [4, 5, 6, 7, 8]
    Intersection: [4, 5]
    

##### Alternatively:


```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = list(set(list1).intersection(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", list(intersection))
```

    List 1: [1, 2, 3, 4, 5]
    List 2: [4, 5, 6, 7, 8]
    Intersection: [4, 5]
    

### Qs.3 Write a Python program to check if a list is a sublist of another list.


```python
main_list = [1, 2, 3, 4, 5, 6, 7]
sublist = [3, 4, 5]

print("Main list:", main_list)
print("Sublist:", sublist)

if str(sublist)[1:-1] in str(main_list):
    print("Sublist is present")
else:
    print("Sublist is NOT present")

```

    Main list: [1, 2, 3, 4, 5, 6, 7]
    Sublist: [3, 4, 5]
    Sublist is present
    

### Qs.4 Write a Python program to find the difference betweeen two lists.


```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for i in list1:
    if i not in list2:
        difference.append(i)

print("List 1:", list1)
print("List 2:", list2)
print("Difference:", difference)
```

    List 1: [1, 2, 3, 4, 5]
    List 2: [4, 5, 6, 7, 8]
    Difference: [1, 2, 3]
    

###### Alternatively:


```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

difference = list(set(list1) - set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Difference:", difference)
```

    List 1: [1, 2, 3, 4, 5]
    List 2: [4, 5, 6, 7, 8]
    Difference: [1, 2, 3]
    

### Qs.5 Write a Python program to remove the elements from a list that are present in another list.


```python
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 5, 7]
result = []
for i in list1:
    if i not in list2:
        result.append(i)

print("Main list:", list1)
print("Elements to remove: ", list2)
print("Result:", result)
```

    Main list: [1, 2, 3, 4, 5, 6, 7]
    Elements to remove:  [3, 5, 7]
    Result: [1, 2, 4, 6]
    

## Tuples:

### Qs.1 Write a Python program to count the number of occurrences of each element in a tuple.


```python
numbers = (1, 2, 3, 2, 4, 1, 5, 3)
count_dict = {}
for i in numbers:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print("Tuple: ", numbers)
print("Counted Dictionary: ", count_dict)
print("Occurrences:")
for i in count_dict:
    print(f"number {i}: {count_dict[i]} times")
print()
```

    Tuple:  (1, 2, 3, 2, 4, 1, 5, 3)
    Counted Dictionary:  {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}
    Occurrences:
    number 1: 2 times
    number 2: 2 times
    number 3: 2 times
    number 4: 1 times
    number 5: 1 times
    
    

### Qs.2 Write a Python program to convert a list of tuples into a dictionary.


```python
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
result_dict = dict(tuple_list)

print("List of tuples:", tuple_list)
print("Dictionary:", result_dict)
```

    List of tuples: [('a', 1), ('b', 2), ('c', 3)]
    Dictionary: {'a': 1, 'b': 2, 'c': 3}
    

### Qs.3 Write a Python program to find the smallest and largest elements in a tuple.


```python
numbers = (5, 2, 8, 1, 9, 3, 7)
smallest = numbers[0]
largest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print("Tuple:", numbers)
print("Smallest iber:", smallest)
print("Largest iber:", largest)
```

    Tuple: (5, 2, 8, 1, 9, 3, 7)
    Smallest iber: 1
    Largest iber: 9
    

##### Alternatively:


```python
numbers = (5, 2, 8, 1, 9, 3, 7)
smallest = min(numbers)
largest = max(numbers)

print("Tuple:", numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
```

    Tuple: (5, 2, 8, 1, 9, 3, 7)
    Smallest number: 1
    Largest number: 9
    

### Qs.4 Write a Python program to remove an element from a tuple.


```python
tup = (1, 2, 3, 4, 5)
element = 3
tup_list = list(tup)
tup_list.remove(element)
tup = tuple(tup_list)

print("Original Tuple:", numbers)
print("After removing:", element)
print("Resulting Tuple:", tup)
```

    Original Tuple: (1, 2, 3, 4, 5)
    After removing: 3
    Resulting Tuple: (1, 2, 4, 5)
    

### Qs.5 Write a Python program to concatenate multiple tuples.


```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
result = tuple1 + tuple2 + tuple3

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)
print("Concatenated Tuple:", result)
```

    Tuple 1: (1, 2, 3)
    Tuple 2: (4, 5, 6)
    Tuple 3: (7, 8, 9)
    Concatenated Tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9)
    

## Dictionary:

### Qs.1 Write a Python program to find the keys with the maximum and minimum values in a dictionary.


```python
scores = {"John": 85, "Alice": 92, "Bob": 78, "Emma": 95}
max_key = ""
min_key = ""
max_value = float('-inf')
min_value = float('inf')

for i, j in scores.items():
    if j > max_value:
        max_value = j
        max_key = i
    if j < min_value:
        min_value = j
        min_key = i

print('Dictionary:', scores)
print('Max key:', max_key)
print('Max value:', max_value)
print('Min key:', min_key)
print('Min value:', min_value)
```

    Dictionary: {'John': 85, 'Alice': 92, 'Bob': 78, 'Emma': 95}
    Max key: Emma
    Max value: 95
    Min key: Bob
    Min value: 78
    

##### Alternatively:


```python
scores = {"John": 85, "Alice": 92, "Bob": 78, "Emma": 95}

max_key = max(scores, key=scores.get)
min_key = min(scores, key=scores.get)

print('Dictionary:', scores)
print('Max key:', max_key, 'Max value:', scores[max_key])
print('Min key:', min_key, 'Min value:', scores[min_key])
```

    Dictionary: {'John': 85, 'Alice': 92, 'Bob': 78, 'Emma': 95}
    Max key: Emma Max value: 95
    Min key: Bob Min value: 78
    

### Qs.2 Write a Python program to check if two dictionaries are equal.


```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "a": 1, "c": 3}
are_equal = True

if len(dict1) != len(dict2):
    are_equal = False
else:
    for i in dict1:
        if i not in dict2 or dict1[i] != dict2[i]:
            are_equal = False
            break

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Are the dictionaries equal?:", are_equal)
```

    Dictionary 1: {'a': 1, 'b': 2, 'c': 3}
    Dictionary 2: {'b': 2, 'a': 1, 'c': 3}
    Are the dictionaries equal?: True
    

### Qs.3 Write a Python program to find the union of two dictionaries.


```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

union_dict = dict1.copy()
union_dict.update(dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Union dictionary:", union_dict)
```

    Dictionary 1: {'a': 1, 'b': 2}
    Dictionary 2: {'b': 3, 'c': 4}
    Union dictionary: {'a': 1, 'b': 3, 'c': 4}
    

### Qs.4 Write a Python program to remove a specific key from a dictionary.


```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
key = "age"

my_dict.pop(key)

print("Dictionary:", my_dict)
print('After removing key:', key,'\n', my_dict)
```

    Dictionary: {'name': 'John', 'city': 'New York'}
    After removing key: age 
     {'name': 'John', 'city': 'New York'}
    

### Qs.5 Write a Python program to create a dictionary from two lists.


```python
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]

result_dict = dict(zip(keys, values))

print("Keys:", keys)
print("Values:", values)
print("Result:", result_dict)
```

    Keys: ['name', 'age', 'city']
    Values: ['John', 30, 'New York']
    Result: {'name': 'John', 'age': 30, 'city': 'New York'}
    

### Qs.6 Write a Python program to find the keys associated with the top three values in multiple dictionaries.


```python

```
