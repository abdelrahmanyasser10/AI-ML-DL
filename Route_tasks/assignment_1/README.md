# 🐍 Machine Learning Journey: Assignment 1 — Introduction to Programming

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning** course.  
This first assignment focuses on **foundational programming concepts in Python**, building a strong base for future machine learning tasks.

---

## 📘 About This Assignment

| **Field** | **Details** |
|------------|-------------|
| **Assignment Name** | Introduction to Programming |
| **Course** | Machine Learning with Route Academy |
| **Instructor** | Ahmed Ziada |
| **Student** | Abdelrahman Yasser |

---

## 🎯 Objective

This assignment includes a series of Python programming problems designed to strengthen understanding of **control flow**, **data structures**, and **basic algorithms** — key foundations for machine learning.

---

## 🧩 Problem Summaries & Approaches

Below is a summary of each problem and the solution approach used.

---

### **Problem 1: Maximum and Minimum of Three Numbers**
**Description:**  
Find the maximum and minimum among three numbers, or check if they’re equal and determine whether each is positive or negative.  

**Approach:**  
Used a series of `if/elif` statements to compare numbers and detect equality. Handled positive/negative checks with additional conditional branches.

---

### **Problem 2: Check for Vowel Characters**
**Description:**  
Check if a word contains a vowel and print its position if found.  

**Approach:**  
Iterated through each character, comparing against a list of vowels. Used `.lower()` to make the search case-insensitive and printed the vowel and index when matched.

---

### **Problem 3: Display Last Digit**
**Description:**  
Display the last digit of a given number.  

**Approach:**  
Used the modulo operator (`% 10`) to extract the last digit.

---

### **Problem 4: Divisibility Check**
**Description:**  
Determine if a number is divisible by both 2 and 3.  

**Approach:**  
Applied the modulo operator (`%`) to test divisibility by both 2 and 3, combining results with the logical `and` operator.

---

### **Problem 5: Class Attendance Percentage**
**Description:**  
Compute a student’s attendance percentage and determine exam eligibility if attendance < 75%.  

**Approach:**  
Calculated attendance percentage, checked for logical validity, and printed eligibility using `if/else` blocks.

---

### **Problem 6: String Case Conversion**
**Description:**  
Convert a string to either all upper-case or all lower-case depending on which case appears more frequently.  

**Approach:**  
Counted upper- vs. lower-case letters, then applied `.upper()` or `.lower()` accordingly.

---

### **Problem 7: Palindrome and Armstrong Number Check**
**Description:**  
Check whether a number is a palindrome or an Armstrong number.  

**Approach:**  
- **Palindrome:** reversed the number as a string and compared.  
- **Armstrong:** summed digits raised to the power of the number’s length and compared to the original.

---

### **Problem 8: Number to Words Conversion (Bonus)**
**Description:**  
Convert a number into its English word form (e.g., 124 → “One hundred and twenty-four”).  

**Approach:**  
Implemented a recursive function handling ranges (0–19, 20–99, 100–999) by mapping each segment to its corresponding text representation.

---

### **Problem 9: Series Sum Calculation**
**Description:**  
Calculate the sum of the series 1 + 4 − 9 + 16 − 25 + 36 … up to n terms.  

**Approach:**  
Initialized sum = 1, looped from 2 to n, and alternated between adding even squares and subtracting odd squares.

---

### **Problem 10: Count Word Occurrences**
**Description:**  
Count occurrences of the word “car” in a string and output their positions.  

**Approach:**  
Split the input text into words, looped with enumeration, counted matches, and displayed their indices + 1.

---

### **Problem 11: Input Type Processing**
**Description:**  
Process user input differently depending on its type: numeric, alphabetic, or mixed.  

**Approach:**  
Used `.isdigit()` and `.isalpha()` for type checks.  
- For numbers → summed digits.  
- For text → removed spaces.  
- For mixed → split into separate components.

---

### **Problem 12: Average of Tuple of Tuples**
**Description:**  
Compute the average of numbers inside each inner tuple within a larger tuple.  

**Approach:**  
Iterated over the outer tuple and applied `sum()` / `len()` on each inner tuple, storing results in a new list.

---

### **Problem 13: Check and Sort List**
**Description:**  
Check if a list is empty; if not, sort it in ascending order.  

**Approach:**  
Used `len()` to check emptiness and `list.sort()` for sorting in-place.

---

### **Problem 14: Remove Even Numbers**
**Description:**  
Remove all even numbers from a list.  

**Approach:**  
Iterated backward through the list using `.pop(i)` to safely remove even elements without index errors.

---

### **Problem 15: Extract Elements with High Frequency**
**Description:**  
Extract elements from a list that appear more than K times.  

**Approach:**  
Counted element frequencies using a dictionary and appended elements with counts > K to a result list, avoiding duplicates.

---

### **Problem 16: Sort Dictionary Keys and Values**
**Description:**  
Sort both dictionary keys and their list values.  

**Approach:**  
Sorted each list using `.sort()` and then reconstructed a new dictionary from sorted keys.

---

### **Problem 17: Student Dictionary Management**
**Description:**  
Create and manage a dictionary of student info (age + grades) with options to view or edit.  

**Approach:**  
Implemented an interactive menu in a `while` loop. Included input validation and error handling for missing students or invalid entries.

---

## ⚙️ How to Run the Code

### **Requirements**
You only need **Python 3.x** — no external libraries required.

### **Run Instructions**
1. Clone this repository:
   ```bash
   git clone https://github.com/abdelrahmanyasser10/AI-ML-DL.git
   cd AI-ML-DL/Route_tasks/assignment_1
2. Run the Python file(s):
   ```bash
    python Assignment1.py
