# 🐍 Python Programming — A to Z Code Notes

> My personal collection of Python concepts, code examples, practice problems, and mini projects — organized for learning and revision.

## 📚 Table of Contents

1. Python Basics
2. Operators
3. Conditional Statements
4. Loops
5. Pattern Printing
6. Strings
7. Lists
8. Tuples
9. Sets
10. Dictionaries
11. Functions
12. Recursion
13. Searching Algorithms
14. Sorting Algorithms
15. Basic Problem Solving
16. Mini Projects
17. Important Python Notes

---

## 01. Python Basics

### Print Output

```python
print("Hello, World!")
print(10)
print(5 + 3)
```

### Variables and Data Types

```python
name = "Sadia"
age = 21
height = 1.65
is_student = True

print(name)
print(age)
print(type(height))
```

### User Input

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
```

### Type Conversion

```python
a = int("10")
b = float("5.5")
c = str(100)

print(a, b, c)
```

## 02. Operators

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Power
```

## 03. Conditional Statements

### Even or Odd

```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Largest of Three Numbers

```python
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
```

### Leap Year

```python
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
```

## 04. Loops

### Print 1 to N

```python
n = int(input())

for i in range(1, n + 1):
    print(i)
```

### Sum of First N Natural Numbers

```python
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)
```

### Factorial

```python
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
```

### Multiplication Table

```python
n = int(input())

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

## 05. Pattern Printing

### Right Triangle

```python
n = int(input())

for i in range(1, n + 1):
    print("*" * i)
```

### Number Triangle

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

## 06. Strings

### Reverse a String

```python
s = input()
print(s[::-1])
```

### Palindrome Check

```python
s = input()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

### Count Vowels

```python
s = input().lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)
```

### Count Characters

```python
s = input()
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)
```

## 07. Lists

### Input a List

```python
arr = list(map(int, input().split()))
print(arr)
```

### Find the Largest Element

```python
arr = list(map(int, input().split()))
largest = arr[0]

for x in arr:
    if x > largest:
        largest = x

print(largest)
```

### Reverse a List

```python
arr = list(map(int, input().split()))
print(arr[::-1])
```

### Remove Duplicates from a Sorted List

```python
arr = list(map(int, input().split()))
result = []

for x in arr:
    if not result or result[-1] != x:
        result.append(x)

print(result)
```

*Note: The duplicate-removal code above assumes the list is sorted.*

## 08. Tuples

```python
numbers = (10, 20, 30, 20)

print(numbers[0])
print(numbers.count(20))
print(numbers.index(30))
```

Tuples are ordered and immutable, meaning their elements cannot be reassigned after creation.

## 09. Sets

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
```

## 10. Dictionaries

```python
student = {
    "name": "Sadia",
    "department": "CSE",
    "semester": 2
}

print(student["name"])

student["semester"] = 3
student["cgpa"] = 3.71

print(student)
```

## 11. Functions

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Functions help organize code into reusable blocks.

## 12. Recursion

### Factorial Using Recursion

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

### Print 1 to N Using Recursion

```python
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

## 13. Searching Algorithms

### Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [10, 20, 30, 40]
print(linear_search(arr, 30))
```

### Binary Search

*The array must be sorted.*

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40))
```

## 14. Sorting Algorithms

### Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort([5, 2, 4, 1, 3]))
```

### Selection Sort

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([5, 2, 4, 1, 3]))
```

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(merge_sort([5, 2, 4, 1, 3]))
```

## 15. Basic Problem-Solving Notes

| Problem | Main Concept |
|---|---|
| Even or odd | Modulo operator |
| Prime number | Divisibility and loops |
| Palindrome | Reverse and compare |
| Factorial | Loop or recursion |
| Fibonacci sequence | Repeated addition |
| Largest element | Comparison |
| Array reversal | Two pointers or slicing |
| Duplicate removal | Set or two pointers |
| Frequency counting | Dictionary |
| Pair sum | Hashing or two pointers |

## 16. Mini Projects

### 🧮 Project 1 — Calculator

**File:** `mini_project1.py`

A simple calculator for basic arithmetic operations.

```python
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
```

**Key concepts:** Input, type conversion, operators, conditionals, and error prevention.

### 🎯 Project 2 — Number Guessing Game

**File:** `mini_project2.py`

The computer generates a random number, and the player keeps guessing until they find it.

```python
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it.")
        print("Attempts:", attempts)
        break
```

**Key concepts:** Random numbers, loops, conditions, counters, and user input.

## 17. Important Python Notes

- `=` assigns a value; `==` compares values.
- `append()` adds one item to a list.
- `extend()` adds items from an iterable.
- `len()` returns the number of items.
- `range(n)` generates numbers from `0` to `n-1`.
- `break` exits a loop.
- `continue` skips the current iteration.
- `return` sends a result back from a function.
- Lists are mutable; strings and tuples are immutable.
- Binary search requires sorted data.
- Recursive functions need a base case.
- Merge sort typically runs in \(O(n \log n)\) time.

---

## 🎯 Learning Goals

- Strengthen Python fundamentals.
- Practice problem-solving and logical thinking.
- Understand recursion and algorithms.
- Improve Data Structures and Algorithms (DSA) skills.
- Build practical mini projects.
- Maintain consistent coding practice.

**My motto:** Learn the concept. Understand the code. Practice independently. Improve every day. 🚀

