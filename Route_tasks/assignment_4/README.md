# Machine Learning Journey: Assignment 4

This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This assignment focuses on **foundational data analysis and manipulation using the Pandas library**.

---

## About This Assignment

**Assignment Name**: Pandas

**Course**: Machine Learning with Route Academy

**Instructor**: Ahmed Ziada


This assignment covers a range of problems designed to **build proficiency in data loading, cleaning, manipulation, and analysis using the Pandas library**. The tasks involve working with a real-world dataset to answer specific questions.

---

## Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

### Question 1: Load the Dataset
**Description**: Load the "Online Shopping Dataset.csv" file into a Pandas DataFrame.
**Approach**: I used the `pd.read_csv()` function to load the dataset into a DataFrame, ensuring the data is correctly structured for subsequent analysis.

### Question 2: Display Basic Information
**Description**: Display the first 5 rows, the last 5 rows, and a concise summary of the DataFrame.
**Approach**: I used the `.head()`, `.tail()`, and `.info()` methods to quickly inspect the data, check for missing values, and understand the data types of each column.

### Question 3: Data Cleaning
**Description**: Handle missing values, if any, and convert columns with incorrect data types.
**Approach**: First, I used `.isnull().sum()` to check for missing values. To handle them, I filled missing values in `Payment Method` with the most frequent method using `.mode()[0]` and in `Product Category` and `Customer Location` with "Unknown" using `.fillna()`. I also converted the `Purchase Date` to datetime format using `pd.to_datetime()`.

### Question 4: Descriptive Statistics
**Description**: Generate descriptive statistics for numerical columns and get the value counts for categorical columns.
**Approach**: I used `.describe()` for numerical columns like `Total Amount` to get statistics such as mean, standard deviation, and quartiles. For categorical columns, I used `.value_counts()` to find the frequency of each unique value.

### Question 5: Total Revenue
**Description**: Calculate the total revenue generated from online sales.
**Approach**: I summed the `Total Amount` column using `.sum()` to find the total revenue.

### Question 6: Sales Trends
**Description**: Analyze monthly sales trends.
**Approach**: I extracted the month from the `Purchase Date` and created a new column. Then, I grouped the data by month and summed the `Total Amount` to see how sales varied from month to month.

### Question 7: Top 5 Bestselling Products
**Description**: Identify the top 5 bestselling products based on the number of items sold.
**Approach**: I grouped the data by `Product Category` and summed the `Total Items` column. Then, I used `.sort_values()` in descending order and `.head(5)` to get the top 5 categories.

### Question 8: Top 5 Customers by Revenue
**Description**: Identify the top 5 customers who have generated the most revenue.
**Approach**: I grouped the data by `Customer ID` and summed the `Total Amount`. The result was sorted in descending order and the top 5 were selected.

### Question 9: Average Order Value by Payment Method
**Description**: Calculate the average order value for each payment method.
**Approach**: I grouped the data by `Payment Method` and used the `.mean()` method on the `Total Amount` column to find the average value for each payment method.

### Question 10: Customer Demographics
**Description**: Analyze the number of orders and average order value for each customer location.
**Approach**: I grouped the data by `Customer Location` and used `.size()` to count the number of orders and `.agg()` with `('Total Amount', 'mean')` to calculate the average order value for each location.

---

### How to Run the Code

To run this analysis, ensure you have the `pandas` library installed. You can then execute the code in a Jupyter Notebook or a Python environment. The provided notebook `Assignment_04_Pandas.ipynb` contains all the code cells and can be run directly.

***
