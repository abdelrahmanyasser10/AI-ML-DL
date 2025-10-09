# 🧾 Machine Learning Journey: Assignment 4 — Pandas

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning course**.  
This fourth assignment focuses on **data analysis** and **manipulation** using the **Pandas** library.

---

## 📘 About This Assignment
**Assignment Name:** Pandas  
**Course:** Machine Learning with Route Academy  
**Instructor:** Ahmed Ziada  


This assignment covers a series of tasks designed to develop proficiency in:
- Loading, inspecting, and cleaning data  
- Performing descriptive statistical analysis  
- Aggregating, grouping, and summarizing data  
- Working with time-based data and categorical variables  

The tasks utilize a real-world dataset — **"Online Shopping Dataset.csv"** — to extract actionable insights.

---

## 🧩 Problem Solutions

### **Question 1: Load the Dataset**
**Description:**  
Load the *Online Shopping Dataset.csv* file into a Pandas DataFrame.  

**Approach:**  
Used `pd.read_csv()` to import the dataset, ensuring proper structure for subsequent analysis.

---

### **Question 2: Display Basic Information**
**Description:**  
Display the first 5 rows, last 5 rows, and a concise summary of the DataFrame.  

**Approach:**  
Used `.head()`, `.tail()`, and `.info()` to explore the dataset, check for missing values, and understand column data types.

---

### **Question 3: Data Cleaning**
**Description:**  
Handle missing values and correct column data types.  

**Approach:**  
- Checked for missing values using `.isnull().sum()`.  
- Filled missing categorical data using `.fillna()` with `"Unknown"`.  
- Filled missing payment methods with the mode: `.mode()[0]`.  
- Converted *Purchase Date* to datetime using `pd.to_datetime()`.

---

### **Question 4: Descriptive Statistics**
**Description:**  
Generate descriptive statistics for numerical columns and analyze categorical columns.  

**Approach:**  
- Used `.describe()` to obtain numerical statistics (mean, std, quartiles).  
- Used `.value_counts()` to summarize categorical variable frequencies.

---

### **Question 5: Total Revenue**
**Description:**  
Calculate the total revenue generated from online sales.  

**Approach:**  
Summed the `Total Amount` column using `.sum()`.

---

### **Question 6: Sales Trends**
**Description:**  
Analyze monthly sales trends to understand seasonal patterns.  

**Approach:**  
- Extracted month from *Purchase Date* using `.dt.month`.  
- Grouped by month and summed `Total Amount` using `.groupby()` and `.sum()`.

---

### **Question 7: Top 5 Bestselling Products**
**Description:**  
Identify the top 5 bestselling product categories.  

**Approach:**  
Grouped data by `Product Category`, summed the `Total Items`, then used `.sort_values(ascending=False).head(5)`.

---

### **Question 8: Top 5 Customers by Revenue**
**Description:**  
Identify the top 5 customers generating the most revenue.  

**Approach:**  
Grouped by `Customer ID`, summed `Total Amount`, and sorted descending to get top 5.

---

### **Question 9: Average Order Value by Payment Method**
**Description:**  
Calculate the average order value for each payment method.  

**Approach:**  
Grouped data by `Payment Method` and used `.mean()` on `Total Amount`.

---

### **Question 10: Customer Demographics**
**Description:**  
Analyze customer orders and spending behavior by location.  

**Approach:**  
Grouped by `Customer Location` and applied:
- `.size()` for number of orders  
- `.agg({'Total Amount': 'mean'})` for average order value  

---

## ⚙️ How to Run the Code
To execute this analysis:

1. Ensure **Pandas** is installed:
   ```bash
   pip install pandas
2. Open the notebook file:
   ```bash
   Assignment_04_Pandas.ipynb
3. Run each cell in Jupyter Notebook or VS Code (Jupyter extension) to reproduce the analysis.
