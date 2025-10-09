# 🧠 Machine Learning Journey: Assignment 7 — Support Vector Machines (SVM)

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning** course.  
This particular assignment focuses on **Support Vector Machines (SVMs)** — a powerful supervised learning algorithm used for both classification and regression tasks.

---

## 📘 About This Assignment

| **Field** | **Details** |
|------------|-------------|
| **Assignment Name** | SVM Task |
| **Course** | Machine Learning with Route Academy |
| **Instructor** | Ahmed Ziada |


---

## 🎯 Objective

This assignment aims to build proficiency in implementing and tuning **Support Vector Machines** for a classification problem.  
The primary goal is to **predict customer churn** based on a given dataset, demonstrating the complete machine learning workflow — from data preprocessing to model evaluation and optimization.

---

## 🧩 Problem Solutions

Below is a summary of each question and the approach used to solve it.

---

### **Question 1: Load the Dataset**
**Description:**  
Load the `customer_churn_dataset.csv` file into a Pandas DataFrame.  

**Approach:**  
Used `pd.read_csv()` to read the dataset into a structured DataFrame for further processing.

---

### **Question 2: Data Preprocessing**
**Description:**  
Handle missing values, encode categorical variables, and scale numerical features.  

**Approach:**  
- Filled missing numerical values with the **mean** and categorical values with the **mode**.  
- Applied **One-Hot Encoding** for categorical features (e.g., `Gender`, `Contract_Type`).  
- Scaled numerical features using **StandardScaler**, as SVMs are sensitive to feature magnitudes.

---

### **Question 3: Data Splitting**
**Description:**  
Split the dataset into training and testing sets.  

**Approach:**  
Used `train_test_split()` from `sklearn.model_selection` with an **80/20 ratio** to ensure fair model evaluation on unseen data.

---

### **Question 4: Model Training with SVM**
**Description:**  
Train a Support Vector Machine classifier using a linear kernel.  

**Approach:**  
- Initialized `SVC(kernel='linear')` from `sklearn.svm`.  
- Trained the model using `.fit(X_train, y_train)` on the scaled dataset.

---

### **Question 5: Model Evaluation**
**Description:**  
Evaluate model performance using a confusion matrix and classification report.  

**Approach:**  
- Made predictions using the trained model.  
- Generated a **confusion matrix** to visualize correct vs. incorrect predictions.  
- Computed the **classification report** (Precision, Recall, F1-Score, Accuracy) using `classification_report()`.

---

### **Question 6: Hyperparameter Tuning**
**Description:**  
Optimize SVM performance through hyperparameter tuning.  

**Approach:**  
- Used **GridSearchCV** from `sklearn.model_selection` to perform exhaustive search over:  
  - `C` values (regularization strength)  
  - Kernel types (`linear`, `rbf`)  
- Selected the best model configuration based on validation accuracy.

---

## ⚙️ How to Run the Code

### **Requirements**
Make sure you have the following Python libraries installed:

```bash
pip install pandas scikit-learn
