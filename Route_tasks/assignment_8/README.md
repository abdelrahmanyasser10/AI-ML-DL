# 🧠 Machine Learning Journey: Assignment 8

This repository documents my progress and solutions for the assignments in the **Route Academy Machine Learning** course.  
This assignment focuses on the **K-Nearest Neighbors (KNN)** algorithm — a supervised learning technique used for both **classification** and **regression**.

---

## 📘 About This Assignment

- **Assignment Name:** Classification (KNN)  
- **Course:** Machine Learning with Route Academy  
- **Instructor:** Ahmed Ziada  
- **Student:** Abdelrahman Yasser  

This assignment is designed to build proficiency in **implementing and evaluating** a K-Nearest Neighbors (KNN) classifier for a real-world classification task.  
The goal is to **classify car evaluations** based on the given dataset, showcasing the complete pipeline — from **data loading and preprocessing** to **model training**, **evaluation**, and **hyperparameter tuning**.

---

## 🧩 Problem Solutions

Below is a brief summary of each problem and the approach taken to solve it.

---

### **Question 1: Load and Display the Dataset**
**Description:**  
Load the `CAR_EVALUATION.csv` dataset and display its basic information.  

**Approach:**  
- Used `pd.read_csv()` to load the dataset into a Pandas DataFrame.  
- Displayed the first few rows with `.head()`.  
- Used `.info()` to summarize data types and non-null counts.

---

### **Question 2: Preprocessing and Encoding**
**Description:**  
Convert all categorical columns into numerical format for modeling.  

**Approach:**  
- Applied **Label Encoding** from `sklearn.preprocessing` to convert string-based categorical columns into numerical form.  
- Each unique category was assigned an integer value.  
- This transformation made the dataset suitable for KNN, which requires numerical inputs.

---

### **Question 3: Data Splitting**
**Description:**  
Split the preprocessed data into **training** and **testing** sets.  

**Approach:**  
- Used `train_test_split` from `sklearn.model_selection`.  
- Adopted an **80/20 split**, where 80% of the data was used for training and 20% for testing.  
- This ensured sufficient training data while keeping a fair portion for unbiased evaluation.

---

### **Question 4: Model Training and Evaluation**
**Description:**  
Train a K-Nearest Neighbors model and evaluate its performance.  

**Approach:**  
- Instantiated a `KNeighborsClassifier` model.  
- Trained the model using `.fit()` on the training data.  
- Predicted test data with `.predict()`.  
- Evaluated performance using:
  - **Accuracy Score** (`metrics.accuracy_score`)  
  - **Confusion Matrix**  
  - **Classification Report** (precision, recall, F1-score)  

This provided both a quantitative and qualitative view of the model’s effectiveness.

---

### **Question 5: Hyperparameter Tuning**
**Description:**  
Find the optimal value for **k** (number of neighbors) to maximize model performance.  

**Approach:**  
- Iterated over values of `k` from 1 to 25.  
- For each `k`, trained a KNN model and calculated its accuracy.  
- Stored all accuracy scores in a list.  
- Plotted accuracy vs. `k` to visualize model performance trends.  
- Identified the `k` value corresponding to the **highest accuracy** — which achieved the best generalization.

---

## ⚙️ How to Run the Code

To execute this project, ensure the following libraries are installed:

```bash
pip install pandas numpy scikit-learn matplotlib
