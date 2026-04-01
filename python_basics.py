# ============================================================
#  Live 14 - Python Programming
#  Topics: Variables, Data Types, Data Structures,
#          Control Flow, Functions
# ============================================================


# ============================================================
# 1. VARIABLES
# ============================================================

# A variable stores a value. No need to declare a type first.
name = "Alice"
age = 25
height = 1.68
is_student = True

print("=== Variables ===")
print("Name   :", name)
print("Age    :", age)
print("Height :", height)
print("Student:", is_student)

# Multiple assignment
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Swap values
x, y = y, x
print("After swap: x =", x, ", y =", y)


# ============================================================
# 2. DATA TYPES
# ============================================================

print("\n=== Data Types ===")

# int — whole numbers
population = 1_000_000
print("int   :", population, type(population))

# float — decimal numbers
pi = 3.14159
print("float :", pi, type(pi))

# str — text (single or double quotes)
greeting = "Hello, World!"
print("str   :", greeting, type(greeting))

# bool — True or False
is_open = False
print("bool  :", is_open, type(is_open))

# NoneType — represents "nothing"
result = None
print("None  :", result, type(result))

# Type conversion (casting)
print("\n--- Type Conversion ---")
num_str = "42"
num_int = int(num_str)       # str → int
num_float = float(num_str)   # str → float
back_to_str = str(num_int)   # int → str
print("str → int  :", num_int,   type(num_int))
print("str → float:", num_float, type(num_float))
print("int → str  :", back_to_str, type(back_to_str))

# String operations
print("\n--- String Operations ---")
first = "Python"
second = "Programming"
combined = first + " " + second   # concatenation
print("Concatenation:", combined)
print("Uppercase    :", combined.upper())
print("Length       :", len(combined))
print("Replace      :", combined.replace("Python", "Java"))
print(f"f-string     : Hello, I am learning {first}!")  # f-string


# ============================================================
# 3. DATA STRUCTURES
# ============================================================

print("\n=== Data Structures ===")

# --- List: ordered, changeable, allows duplicates ---
print("\n--- List ---")
fruits = ["apple", "banana", "cherry", "banana"]
print("List         :", fruits)
print("First item   :", fruits[0])       # index starts at 0
print("Last item    :", fruits[-1])      # negative index
print("Slice [1:3]  :", fruits[1:3])    # slicing

fruits.append("mango")          # add to end
fruits.remove("banana")         # remove first occurrence
print("After changes:", fruits)
print("Length       :", len(fruits))

# Loop through a list
print("Items:")
for fruit in fruits:
    print(" -", fruit)

# --- Tuple: ordered, UNCHANGEABLE ---
print("\n--- Tuple ---")
coordinates = (10.5, 20.3)
print("Tuple        :", coordinates)
print("Latitude     :", coordinates[0])
print("Longitude    :", coordinates[1])
# coordinates[0] = 99  # This would cause an error!

# --- Dictionary: key-value pairs ---
print("\n--- Dictionary ---")
student = {
    "name": "Bob",
    "age": 20,
    "gpa": 3.8,
    "enrolled": True,
}
print("Dict         :", student)
print("Name         :", student["name"])
print("GPA          :", student.get("gpa", "N/A"))  # safe access

student["major"] = "Computer Science"   # add new key
student["age"] = 21                     # update value
print("After update :", student)

print("Keys  :", list(student.keys()))
print("Values:", list(student.values()))

# --- Set: unique values, unordered ---
print("\n--- Set ---")
colors = {"red", "blue", "green", "red", "blue"}
print("Set (no duplicates):", colors)
colors.add("yellow")
colors.discard("red")
print("After add/discard  :", colors)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union        :", a | b)
print("Intersection :", a & b)
print("Difference   :", a - b)


# ============================================================
# 4. CONTROL FLOW
# ============================================================

print("\n=== Control Flow ===")

# --- if / elif / else ---
print("\n--- if / elif / else ---")
score = 75

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} → Grade: {grade}")

# Ternary (one-liner if)
status = "Pass" if score >= 50 else "Fail"
print("Status:", status)

# --- for loop ---
print("\n--- for loop ---")
total = 0
for i in range(1, 6):      # 1, 2, 3, 4, 5
    total += i
    print(f"  i = {i}, running total = {total}")
print("Sum 1–5:", total)

# range(start, stop, step)
print("Even numbers:", list(range(0, 11, 2)))

# enumerate — get index + value
animals = ["cat", "dog", "bird"]
for index, animal in enumerate(animals, start=1):
    print(f"  {index}. {animal}")

# --- while loop ---
print("\n--- while loop ---")
countdown = 5
while countdown > 0:
    print("  Countdown:", countdown)
    countdown -= 1
print("  Go!")

# --- break & continue ---
print("\n--- break & continue ---")
for num in range(1, 11):
    if num == 4:
        continue    # skip 4
    if num == 8:
        break       # stop at 8
    print(" ", num, end="")
print()  # newline

# --- Nested loops ---
print("\n--- Nested loops (multiplication table 1–3) ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end="")
    print()


# ============================================================
# 5. FUNCTIONS
# ============================================================

print("\n=== Functions ===")

# --- Basic function ---
def greet(person_name):
    """Print a greeting message."""
    print(f"Hello, {person_name}!")

greet("Alice")
greet("Bob")

# --- Function with return value ---
def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(3, 7)
print("3 + 7 =", result)

# --- Default parameter ---
def power(base, exponent=2):
    """Return base raised to exponent (default: squared)."""
    return base ** exponent

print("3^2 =", power(3))        # uses default exponent
print("2^10 =", power(2, 10))   # custom exponent

# --- Multiple return values ---
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

data = [4, 7, 1, 9, 3]
lo, hi = min_max(data)
print(f"Data: {data}  →  min={lo}, max={hi}")

# --- *args — variable number of arguments ---
def total(*args):
    """Return the sum of any number of arguments."""
    return sum(args)

print("Total(1,2,3)      =", total(1, 2, 3))
print("Total(5,10,15,20) =", total(5, 10, 15, 20))

# --- **kwargs — keyword arguments ---
def display_info(**kwargs):
    """Print key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Student info:")
display_info(name="Carol", age=22, major="Data Science")

# --- Lambda (anonymous function) ---
print("\n--- Lambda ---")
square = lambda n: n ** 2
is_even = lambda n: n % 2 == 0

print("square(5)  =", square(5))
print("is_even(4) =", is_even(4))
print("is_even(7) =", is_even(7))

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Sorted         :", sorted(numbers))
print("Sorted (desc)  :", sorted(numbers, reverse=True))
print("Evens only     :", list(filter(is_even, numbers)))
print("Squares        :", list(map(square, numbers)))

# --- Scope: local vs global ---
print("\n--- Scope ---")
message = "I am global"

def show_scope():
    local_var = "I am local"
    print(" Inside function:", local_var)
    print(" Inside function (global):", message)

show_scope()
print("Outside function:", message)
# print(local_var)  # This would raise a NameError!

# --- Putting it all together: a mini grade calculator ---
print("\n--- Mini Grade Calculator ---")

def letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def class_summary(scores):
    """Print a summary for a list of student scores."""
    print(f"  Scores : {scores}")
    print(f"  Average: {sum(scores) / len(scores):.1f}")
    print(f"  Highest: {max(scores)}")
    print(f"  Lowest : {min(scores)}")
    grades = [letter_grade(s) for s in scores]
    print(f"  Grades : {grades}")

class_scores = [88, 72, 55, 91, 67, 78, 45, 83]
class_summary(class_scores)

print("\n=== End of Python Basics ===")
