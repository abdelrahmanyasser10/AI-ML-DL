# 🧠 Machine Learning Journey: Assignment 2 — Functions & OOP

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning course**.  
This second assignment focuses on building proficiency with **Python functions** and **Object-Oriented Programming (OOP)** concepts.

---

## 📘 About This Assignment
**Assignment Name:** Functions & OOP  
**Course:** Machine Learning with Route Academy  
**Instructor:** Ahmed Ziada


This assignment contains a series of problems designed to strengthen understanding of:
- Creating and using Python functions  
- Implementing and working with classes and objects  
- Modeling real-world systems using OOP principles  

---

## 🧩 Problem Solutions

### **Problem 1: Power Function**
**Description:**  
Write a function that calculates the power of a number given a base and an exponent.  

**Approach:**  
A function `pow(base, exponent)` is defined using the `**` operator to compute and return the result.

---

### **Problem 2: Area of a Shape**
**Description:**  
Create a function to calculate the area of a square, rectangle, or circle based on user input.  

**Approach:**  
Implemented a function `area(shape, *args)` that uses conditional statements to determine the shape and calculate the area using geometric formulas.

---

### **Problem 3: Sum of a List**
**Description:**  
Find the sum of all numbers in a list.  

**Approach:**  
A function `sum_list(list)` initializes a variable to 0 and iterates through the list to accumulate the total.

---

### **Problem 4: Concatenate and Find Max/Min in Tuples**
**Description:**  
Concatenate two tuples and find the maximum and minimum elements in the resulting tuple.  

**Approach:**  
Two functions — `tuple_concat()` and `get_max_min()` — are defined.  
`tuple_concat` merges the tuples, and `get_max_min` uses built-in `max()` and `min()` to find the respective values.

---

### **Problem 5: Count Numbers in a Tuple**
**Description:**  
Count the number of numeric elements in a tuple if its length exceeds 5.  

**Approach:**  
The function `tuple_count(tuple)` checks the tuple’s length, then iterates through its elements, counting integers using `isinstance()`.

---

### **Problem 6: Print List Element Index**
**Description:**  
Print the index of each element in a list without using the built-in `index()` function.  

**Approach:**  
The function `print_index(list)` uses `range(len(list))` to print each element along with its index.

---

### **Problem 7: Prime Number Checker**
**Description:**  
Check whether a given number is prime.  

**Approach:**  
The function `is_prime(number)` handles edge cases for numbers < 2 and checks divisibility from 2 up to the number’s square root.

---

### **Problem 8: Restaurant Class**
**Description:**  
Create a `Restaurant` class with attributes and methods to manage menu items, table bookings, and customer orders.  

**Approach:**  
The `Restaurant` class contains attributes (`menu_items`, `book_table`, and `customer_orders`) initialized in the constructor, with methods to modify and retrieve them.

---

### **Problems 9–11: Bike Rental System**
**Description:**  
Design a simple bike rental management system using multiple classes.  

**Approach:**  
- **Customer Class:** Holds customer details (name, age) with getters and setters.  
- **Bike Class:** Represents a bike with attributes for name and price.  
- **MainBikeRental Class:** Contains business logic for renting, returning, and billing bikes using methods like `requestBike()`, `returnBike()`, and `totalCost()`.

---

## ⚙️ How to Run the Code
To execute any problem:

1. Copy the desired code into a Python environment (Jupyter Notebook or `.py` file).  
2. Run the code to view results in the console or notebook output.

### **Requirements**
Make sure you have **Python 3.x** installed.  
No external libraries are required for this assignment.
