# Machine Learning Journey: Assignment 5

This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This assignment focuses on **data preparation and visualization using libraries like Pandas, Matplotlib, and Seaborn**. It demonstrates key steps in a data science pipeline, from loading and cleaning data to visualizing insights.

---

## About This Assignment

**Assignment Name**: Visualization & Data Preparation

**Course**: Machine Learning with Route Academy

**Instructor**: Ahmed Ziada


This assignment covers a range of problems designed to **build proficiency in data preprocessing and exploratory data analysis (EDA)**. The tasks involve working with the "credit_customers.csv" dataset to handle missing values, correct data types, identify outliers, and visualize the data to gain initial insights.

---

## Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

### Question 1: Load and Display Data
**Description**: Load the `credit_customers.csv` dataset and display the first five rows and a concise summary of the DataFrame.
**Approach**: I used `pd.read_csv()` to load the dataset. The `.head()` method was used to show the first few rows, and `.info()` provided a summary of the data, including column types and non-null values.

### Question 2: Handle Missing Values
**Description**: Identify and handle any missing values in the dataset.
**Approach**: I used `.isnull().sum()` to count the missing values in each column. The strategy for handling missing values depended on the column:
- **`Duration_in_month`**: Missing values were filled with the mean of the column.
- **`Credit_amount`**: Missing values were filled with the mean of the column.
- **`Age`**: Missing values were filled with the mean of the column.
- **`Gender`**: Missing values were filled with the mode of the column, which is the most frequent value.

### Question 3: Correct Data Types
**Description**: Correct the data types for columns that are improperly loaded.
**Approach**: I identified that `Duration_in_month`, `Credit_amount`, and `Age` were loaded as floating-point numbers due to the missing values, but are conceptually integers. I converted these columns to an integer type using `.astype('int')`.

### Question 4: Outlier Detection
**Description**: Find and visualize outliers for numerical columns using box plots.
**Approach**: I used **box plots** to visually identify potential outliers in the `Credit_amount`, `Age`, and `Duration_in_month` columns. A box plot is a great way to show the distribution of data and pinpoint extreme values.

### Question 5: Handle Outliers
**Description**: Handle outliers in the numerical columns by capping the extreme values.
**Approach**: I used the **Interquartile Range (IQR)** method to define the upper and lower bounds for outlier detection. I calculated the first quartile ($Q_1$) and third quartile ($Q_3$) and then defined the upper bound as $Q_3 + 1.5 \times IQR$ and the lower bound as $Q_1 - 1.5 \times IQR$. Any value above the upper bound or below the lower bound was capped at the respective bound. 

### Question 6: Data Visualization
**Description**: Visualize the distribution of `Credit_amount` and `Age` using a histogram and a distribution plot.
**Approach**: I created a **histogram** for `Credit_amount` to show the frequency distribution of different credit amounts. For `Age`, I used a distribution plot to visualize the probability distribution of ages in the dataset.

### Question 7: Categorical Data Visualization
**Description**: Visualize the distribution of categorical features using a count plot.
**Approach**: I used a **count plot** to visualize the frequency of each category in the `Gender` column. This provided a clear view of the male-to-female ratio in the dataset.

### Question 8: Bivariate Analysis
**Description**: Visualize the relationship between `Credit_amount` and `Age` using a scatter plot.
**Approach**: I created a **scatter plot** to explore the relationship between `Credit_amount` and `Age`. This plot helps to identify any correlations or patterns between the two numerical variables.

---

## How to Run the Code

To run this analysis, you will need to have the following libraries installed:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

You can execute the code in a Jupyter Notebook or a Python environment. The provided notebook `Assignment_05_Data_Preprocessing.ipynb` contains all the code and can be run directly.

---
