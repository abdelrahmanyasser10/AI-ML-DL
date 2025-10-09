# 🧠 Machine Learning Journey: Assignment 5

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning** course.  
This assignment focuses on **data preparation and visualization** using libraries like **Pandas**, **Matplotlib**, and **Seaborn**.  
It demonstrates key steps in a data science pipeline — from **loading and cleaning data** to **visualizing insights**.

---

## 📘 About This Assignment

- **Assignment Name:** Visualization & Data Preparation  
- **Course:** Machine Learning with Route Academy  
- **Instructor:** Ahmed Ziada  

This assignment covers a range of problems designed to build proficiency in **data preprocessing** and **exploratory data analysis (EDA)**.  
The tasks involve working with the `credit_customers.csv` dataset to handle missing values, correct data types, identify outliers, and visualize the data to gain initial insights.

---

## 🧩 Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

---

### **Question 1: Load and Display Data**
**Description:** Load the `credit_customers.csv` dataset and display the first five rows and a concise summary of the DataFrame.  
**Approach:**  
- Used `pd.read_csv()` to load the dataset.  
- Used `.head()` to show the first few rows.  
- Used `.info()` to display a summary of the data, including column types and non-null values.

---

### **Question 2: Handle Missing Values**
**Description:** Identify and handle any missing values in the dataset.  
**Approach:**  
- Used `.isnull().sum()` to count missing values.  
- Handled missing values as follows:
  - `Duration_in_month`: filled with column mean.  
  - `Credit_amount`: filled with column mean.  
  - `Age`: filled with column mean.  
  - `Gender`: filled with column mode (most frequent value).

---

### **Question 3: Correct Data Types**
**Description:** Correct the data types for columns that are improperly loaded.  
**Approach:**  
- Identified that `Duration_in_month`, `Credit_amount`, and `Age` were loaded as floats due to missing values.  
- Converted these columns to integers using `.astype('int')`.

---

### **Question 4: Outlier Detection**
**Description:** Find and visualize outliers for numerical columns using box plots.  
**Approach:**  
- Used **box plots** to identify potential outliers in `Credit_amount`, `Age`, and `Duration_in_month`.  
- Box plots are effective for visualizing distributions and spotting extreme values.

---

### **Question 5: Handle Outliers**
**Description:** Handle outliers in numerical columns by capping extreme values.  
**Approach:**  
- Applied the **Interquartile Range (IQR)** method:
  - \( Q1 = 25^{th} \text{ percentile} \)  
  - \( Q3 = 75^{th} \text{ percentile} \)  
  - \( IQR = Q3 - Q1 \)  
- Defined bounds:
  - **Upper bound:** \( Q3 + 1.5 \times IQR \)  
  - **Lower bound:** \( Q1 - 1.5 \times IQR \)  
- Capped values exceeding these bounds to maintain data integrity.

---

### **Question 6: Data Visualization**
**Description:** Visualize the distribution of `Credit_amount` and `Age` using histograms and distribution plots.  
**Approach:**  
- Created a **histogram** for `Credit_amount` to show frequency distribution.  
- Used a **distribution plot** for `Age` to visualize the probability distribution across ages.

---

### **Question 7: Categorical Data Visualization**
**Description:** Visualize the distribution of categorical features using a count plot.  
**Approach:**  
- Used a **count plot** to show category frequencies in the `Gender` column.  
- Helped visualize the **male-to-female ratio** in the dataset.

---

### **Question 8: Bivariate Analysis**
**Description:** Visualize the relationship between `Credit_amount` and `Age` using a scatter plot.  
**Approach:**  
- Created a **scatter plot** to explore correlations or trends between the two numerical variables.

---

## ⚙️ How to Run the Code

To run this analysis, ensure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib seaborn
