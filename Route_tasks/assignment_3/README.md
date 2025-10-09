# 🧮 Machine Learning Journey: Assignment 3 — NumPy

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning course**.  
This third assignment focuses on **data manipulation** and **scientific computing** using the **NumPy** library.

---

## 📘 About This Assignment
**Assignment Name:** NumPy  
**Course:** Machine Learning with Route Academy  
**Instructor:** Ahmed Ziada  


This assignment covers a series of problems designed to build proficiency in using **NumPy** for:
- Array creation and reshaping  
- Vectorized operations  
- Statistical computations  
- Boolean masking and universal functions (ufuncs)  

---

## 🧩 Problem Solutions

### **Question 1: Create a 2D Array with Random Integers**
**Description:**  
Create a 2D NumPy array with shape `(3, 3)` containing random integers between 1 and 20.  

**Approach:**  
Used `np.random.randint()` specifying the range and shape.

---

### **Question 2: Min and Max Values per Row**
**Description:**  
Create a 5×5 array with random values and find the minimum and maximum of each row.  

**Approach:**  
Generated a random array, then applied `.min(axis=1)` and `.max(axis=1)` to compute row-wise minima and maxima.

---

### **Question 3: Sort a Random Vector**
**Description:**  
Create a random vector of size 10 and sort it.  

**Approach:**  
Generated a vector with `np.random.random()` and sorted it using `np.sort()`.

---

### **Question 4: Find the Most Frequent Value**
**Description:**  
Find the most frequent (mode) value in an array.  

**Approach:**  
Used `np.unique(arr, return_counts=True)` to get unique values and their frequencies, then applied `np.argmax()` to identify the most frequent element.

---

### **Question 5: Replace Even Numbers with Zero**
**Description:**  
Replace all even numbers in a 2D array with 0.  

**Approach:**  
Applied **boolean indexing**:  
Created a mask `arr % 2 == 0` and set those positions to `0`.

---

### **Question 6: Apply Square Root Function**
**Description:**  
Apply the square root function to every element of a 1D array.  

**Approach:**  
Used the universal function `np.sqrt()` to apply the operation element-wise.

---

### **Question 7: Subtract Mean of Each Row**
**Description:**  
Create a 3×3 array with random values and subtract the mean of each row from every element in that row.  

**Approach:**  
Computed the row-wise mean using `arr.mean(axis=1)` and subtracted it from each row using broadcasting.

---

### **Question 8: First 20 Odd Numbers**
**Description:**  
Generate a 1D array containing the first 20 odd numbers.  

**Approach:**  
Used `np.arange(1, 41, 2)` to produce the sequence.

---

### **Question 9: Second-Largest Value in Each Column**
**Description:**  
Find the second-largest value in each column of a 5×5 random array.  

**Approach:**  
Computed column-wise maxima using `arr.max(axis=0)`, then removed them with `np.delete()` and found the next largest using `max()`.

---

### **Question 10: Sum of Each Row**
**Description:**  
Compute the sum of each row in a 4×4 array.  

**Approach:**  
Generated a random 4×4 array using `np.random.random()` and applied `.sum(axis=1)` to get row-wise totals.

---

## ⚙️ How to Run the Code
To execute any of the problems:

1. Copy the desired code into a Python environment (Jupyter Notebook or `.py` file).  
2. Run the code to view the output in the console or notebook cell.

---

## 🧰 Requirements
- **Python 3.x**  
- **NumPy**

You can install NumPy using:
```bash
pip install numpy
