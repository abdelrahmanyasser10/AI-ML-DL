# Machine Learning Journey: Assignment 3

This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This assignment focuses on **foundational data manipulation and scientific computing using the NumPy library**.

---

## About This Assignment

**Assignment Name**: NumPy

**Course**: Machine Learning with Route Academy

**Instructor**: Ahmed Ziada


This assignment covers a range of problems designed to **build proficiency in using NumPy for array creation, manipulation, and mathematical operations**.

---

## Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

### Question 1: Create a 2D Array with Random Integers
**Description**: Create a 2D NumPy array with a shape of (3, 3) containing random integers between 1 and 20.
**Approach**: I used `np.random.randint()` and specified the range and the desired shape.

### Question 2: Min and Max Values per Row
**Description**: Create a 5x5 array with random values and find the minimum and maximum values for each row.
**Approach**: I first created a random 5x5 array and then used the `.min()` and `.max()` methods with the `axis=1` parameter to find the minimum and maximum values for each row.

### Question 3: Sort a Random Vector
**Description**: Create a random vector of size 10 and sort it.
**Approach**: I generated a 1D array using `np.random.random()` and sorted it using the `np.sort()` function.

### Question 4: Find the Most Frequent Value
**Description**: Find the most frequent value in an array.
**Approach**: I used `np.unique()` with `return_counts=True` to get a list of unique values and their frequencies. Then, I used `np.argmax()` on the counts to find the index of the highest frequency, which corresponds to the most frequent value.

### Question 5: Replace Even Numbers with Zero
**Description**: Replace all even numbers in a 2D array with 0.
**Approach**: This was solved using **boolean indexing**. I created a boolean mask using `arr % 2 == 0` to identify even numbers and then assigned a value of 0 to all elements where the condition was `True`.

### Question 6: Apply Square Root Function
**Description**: Apply the square root function to each element of a 1D array.
**Approach**: I used the `np.sqrt()` function, which is a universal function (ufunc) that applies the operation element-wise to the array.

### Question 7: Subtract Mean of Each Row
**Description**: Create a 3x3 array with random values and subtract the mean of each row from each element.
**Approach**: I first calculated the mean of each row using `arr.mean(axis=1)`. Then, I performed the subtraction by manually subtracting the mean of each row from its corresponding elements.

### Question 8: First 20 Odd Numbers
**Description**: Create a 1D array containing the first 20 odd numbers.
**Approach**: I used the `np.arange()` function, starting at 1, ending at 41 (exclusive), and with a step of 2 to generate the sequence of odd numbers.

### Question 9: Second-Largest Value in Each Column
**Description**: Create a 5x5 array with random values and find the second-largest value in each column.
**Approach**: I first calculated the largest value in each column using `arr.max(axis=0)`. Then, I found the index of the max value with `argmax()`, used `np.delete()` to remove it, and found the maximum of the remaining values, which is the second-largest value.

### Question 10: Sum of Each Row
**Description**: Create a 4x4 array with random values and find the sum of each row.
**Approach**: I created a random 4x4 array using `np.random.random()` and then used the `.sum()` method with `axis=1` to find the sum of each row.

---

### How to Run the Code

To run any of the programs, copy the code into a Python environment (like a Jupyter Notebook or a `.py` file) and execute it. The programs will display the output to the console.