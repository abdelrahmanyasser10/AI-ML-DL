# Machine Learning Journey: Assignment 2

This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This second assignment focuses on building proficiency with Python functions and Object-Oriented Programming (OOP) concepts.

---

## About This Assignment

**Assignment Name**: Functions & OOP
**Course**: Machine Learning with Route Academy
**Instructor**: Ahmed Ziad

This assignment contains a series of problems designed to solidify understanding of creating and using functions, as well as designing and implementing Python classes to model real-world concepts.

---

## Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

### Problem 1: Power Function
**Description**: Write a function that calculates the power of a number given a base and an exponent.
**Approach**: A function `pow(base, exponent)` is defined, which uses the `**` operator to compute the power and return the result.

### Problem 2: Area of a Shape
**Description**: Create a function to calculate the area of a square, rectangle, or circle based on user input.
**Approach**: A function `area(shape, *args)` is implemented using a variable number of arguments (`*args`). It uses `if/elif` statements to determine the shape and calculates the area using the appropriate geometric formula.

### Problem 3: Sum of a List
**Description**: Find the sum of all numbers in a list.
**Approach**: A function `sum_list(list)` is created that initializes a `sum` variable to 0 and iterates through the list, adding each element to the sum.

### Problem 4: Concatenate and Find Max/Min in Tuples
**Description**: Concatenate two tuples and then find the maximum and minimum elements of the new tuple.
**Approach**: Two functions, `tuple_concat` and `get_max_min`, are used. The first concatenates the tuples using the `+` operator, and the second uses the built-in `max()` and `min()` functions to find the highest and lowest values.

### Problem 5: Count Numbers in a Tuple
**Description**: Count the number of numeric elements in a tuple if its length is greater than 5.
**Approach**: The function `tuple_count(tuple)` first checks if the length of the tuple is greater than 5. If it is, it iterates through the tuple, using `type()` to check if each element is an integer and increments a counter.

### Problem 6: Print List Element Index
**Description**: Print the index of each list element without using the `index()` function.
**Approach**: A function `print_index(list)` is defined that uses the `range(len(list))` construct to iterate through the indices and print each element along with its position.

### Problem 7: Prime Number Checker
**Description**: Check if a given number is a prime number.
**Approach**: The `is_prime(number)` function first handles the edge case for numbers less than 2. It then uses a `for` loop to check for divisibility from 2 up to the number itself. If any divisor is found, it returns `False`; otherwise, it returns `True`.

### Problem 8: Restaurant Class
**Description**: Create a `Restaurant` class with attributes for menu items, table reservations, and customer orders, and methods to manage them.
**Approach**: The `Restaurant` class is implemented with three attributes (`menu_items`, `book_table`, and `customer_orders`) initialized in the constructor. Methods like `add_item_to_menu`, `book_tables`, and `customer_order` are defined to manipulate these data structures.

### Problems 9, 10, & 11: Bike Rental System
**Description**: A multi-part problem requiring the creation of three classes: `Customer`, `MainBikeRental`, and `Bike`, to manage a bike rental system.
**Approach**:
- **`Customer` Class**: A simple class with `name` and `age` attributes, along with standard getter and setter methods.
- **`MainBikeRental` Class**: Manages the core business logic. It includes methods like `requestBike` to handle rental requests (checking availability and age), `returnBike` to calculate a bill and restock bikes, and `totalCost` to sum up the cost of all active rentals.
- **`Bike` Class**: A class to represent a single bike, with `name` and `price` attributes and corresponding getter and setter methods.

---

### How to Run the Code

To run any of the programs, copy the code into a Python environment (like a Jupyter Notebook or a `.py` file) and execute it. The programs will display output to the console.
