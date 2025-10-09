# 🧠 Machine Learning Journey: Assignment 6

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning** course.  
This assignment focuses on **regression analysis**, covering **data preparation**, **feature engineering**, **model training**, and **evaluation** for a **house price prediction** task.

---

## 📘 About This Assignment

- **Assignment Name:** Regression Assignment  
- **Course:** Machine Learning with Route Academy  
- **Instructor:** Ahmed Ziada  

This assignment involves building regression models to predict house prices.  
It covers a comprehensive **machine learning pipeline**, including:
- Handling multiple datasets  
- Data cleaning and preprocessing  
- Exploratory data analysis (EDA)  
- Feature engineering  
- Model training and evaluation using various metrics  

---

## 🧩 Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

---

### **Question 1: Load and Merge Datasets**
**Description:**  
Load the `house_data.csv` and `Expanded_data_with_more_features.csv` datasets and merge them into a single DataFrame.  

**Approach:**  
- Used `pd.read_csv()` to load both datasets.  
- Merged them on the `ID` column using `pd.merge()` with an **inner join** to ensure only matching rows were kept.

---

### **Question 2: Data Cleaning and Preprocessing**
**Description:**  
Handle missing values, correct data types, and remove duplicates.  

**Approach:**  
- Used `.isnull().sum()` to identify missing values.  
- Filled missing values:
  - Numerical columns → mean  
  - Categorical columns → mode  
- Converted the `Date` column to datetime objects using `pd.to_datetime()`.  
- Removed duplicate rows with `.drop_duplicates()`.

---

### **Question 3: Exploratory Data Analysis (EDA)**
**Description:**  
Perform EDA to understand data distributions, relationships, and correlations.  

**Approach:**  
- Used **histograms** and **distribution plots** to visualize feature distributions.  
- Created a **correlation matrix** and **heatmap** to find relationships between numerical features and the target (`price`).  
- Used **scatter plots** (e.g., `area` vs `price`) to visualize key feature relationships.

---

### **Question 4: Feature Engineering**
**Description:**  
Create new features to improve model performance, such as `age_of_house` derived from the `Date` column.  

**Approach:**  
- Extracted the **year** from the `Date` column.  
- Computed a new feature `age_of_house` = (current year - year built).  
- This feature was used to capture the potential influence of house age on price.

---

### **Question 5: Model Training**
**Description:**  
Train at least two regression models to predict house prices.  

**Approach:**  
- Split the data into **training** and **testing** sets.  
- Trained two models:
  - **Linear Regression**  
  - **Decision Tree Regressor**  
- Selected key features and fit both models to predict `price`.

---

### **Question 6: Model Evaluation**
**Description:**  
Evaluate the models using **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R-squared (R²)** metrics.  

**Approach:**  
- Used the test set for predictions.  
- Calculated and compared:
  - **MAE:** Measures average absolute errors.  
  - **MSE:** Penalizes larger errors more heavily.  
  - **R²:** Explains variance captured by the model.  
- Compared both models’ results to determine which performed better.

---

## ⚙️ How to Run the Code

To run this analysis, ensure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
