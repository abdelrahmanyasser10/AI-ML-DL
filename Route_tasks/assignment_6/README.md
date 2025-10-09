# Machine Learning Journey: Assignment 6

This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This assignment focuses on **regression analysis**, covering data preparation, feature engineering, model training, and evaluation for a house price prediction task.

---

## About This Assignment

**Assignment Name**: Regression Assignment

**Course**: Machine Learning with Route Academy

**Instructor**: Ahmed Ziada


This assignment involves building regression models to predict house prices. It covers a comprehensive machine learning pipeline, including handling multiple datasets, data cleaning, exploratory data analysis, feature engineering, and evaluating model performance using various metrics.

---

## Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

### Question 1: Load and Merge Datasets
**Description**: Load the `house_data.csv` and `Expanded_data_with_more_features.csv` datasets and merge them into a single DataFrame.
**Approach**: I used `pd.read_csv()` to load both datasets. The datasets were merged on the `ID` column using `pd.merge()` with an `inner` join to ensure only matching rows were kept.

### Question 2: Data Cleaning and Preprocessing
**Description**: Handle missing values, correct data types, and remove any duplicates.
**Approach**: I used `.isnull().sum()` to identify missing values. For numerical columns, I filled missing values with the mean. For categorical columns, I filled them with the mode. The `Date` column was converted to datetime objects using `pd.to_datetime()`. Duplicate rows were identified and removed with `.drop_duplicates()`.

### Question 3: Exploratory Data Analysis (EDA)
**Description**: Perform EDA to understand the data distribution, relationships between features, and correlations.
**Approach**: I used histograms and distribution plots to visualize the distribution of key features. A correlation matrix and heat map were created to identify relationships between numerical features and the target variable (`price`). Scatter plots were used to visualize the relationships between specific features like `area` and `price`.

### Question 4: Feature Engineering
**Description**: Create new features to improve model performance, such as `age_of_house` from the `Date` column.
**Approach**: I created new, more meaningful features. For example, I extracted the year from the `Date` column and used it to calculate the `age_of_house`. This new feature is likely to have a strong relationship with the house price.

### Question 5: Model Training
**Description**: Train at least two different regression models (e.g., Linear Regression, Decision Tree Regressor) to predict house prices.
**Approach**: I split the data into training and testing sets. I trained a **Linear Regression** model and a **Decision Tree Regressor** model using the training data. The models were fit with a set of selected features to predict the `price`.

### Question 6: Model Evaluation
**Description**: Evaluate the performance of the trained models using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
**Approach**: I used the test set to make predictions with each trained model. The performance of each model was then evaluated by calculating the MAE, MSE, and R-squared. The results were compared to determine which model performed better.

---

## How to Run the Code

To run this analysis, you will need to have the following libraries installed:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can execute the code in a Jupyter Notebook or a Python environment. The provided notebook `Regression_Assignment.ipynb` contains all the code cells and can be run directly.

---
