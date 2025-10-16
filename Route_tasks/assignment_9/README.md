# 🧠 Machine Learning Assignment: Pen-Digits Classification

This repository contains my work for the **Pen-Digits Classification** assignment as part of the **Machine Learning** course.  
The task involves building and improving classification models through data exploration, preprocessing, model training, evaluation, and performance enhancement.

---

## 📘 About This Assignment

- **Assignment Name:** ML Assignment — Pen-Digits Classification  
- **Course:** Machine Learning  

**Problem:**  
The primary goal is to classify digits from the Pen-Digits dataset.  
This involves a complete workflow — from data exploration and preprocessing to model training, evaluation, and optimization.

---

## 🧩 Problem Solutions

Below is a summary of the key tasks from the assignment and the approach taken to solve each.

---

### **1️⃣ Decision Tree**

**Description:**  
The first step was to explore the dataset and build a Decision Tree model.  
This included visualizing relationships between variables, formatting data, fitting the model, and evaluating it using a confusion matrix and accuracy score.

**Approach:**  
- Used scatterplot matrices and heatmaps to visualize feature correlations.  
- Trained a Decision Tree classifier on the training data.  
- Explored pruning techniques and evaluated their impact on model accuracy.

---

### **2️⃣ Bagging**

**Description:**  
This section focused on implementing **bagging** techniques.  
The task required applying both **SVM** and **Decision Tree** as base estimators, and tuning a **Random Forest**, which is a well-known bagging ensemble model.

**Approach:**  
- Implemented Bagging with SVM and Decision Tree classifiers.  
- Evaluated model performance on the test set.  
- Conducted hyperparameter tuning for Random Forest (number of estimators).  
- Plotted accuracy against the number of estimators to find the optimal configuration.

---

### **3️⃣ Boosting**

**Description:**  
This part involved building and tuning two boosting models: **GradientBoosting** and **XGBoost**.  
The objective was to optimize hyperparameters and compare both models' performance.

**Approach:**  
- Tuned the `n_estimators` and `learning_rate` parameters for GradientBoosting.  
- Used the best-performing parameters to train an XGBoost classifier.  
- Compared GradientBoosting and XGBoost results against bagging models, analyzing trade-offs in accuracy and robustness.

---

### **4️⃣ Improving with PCA and Feature Selection**

**Description:**  
The final step aimed to improve the best-performing model by simplifying the feature space.  
This was achieved through **Principal Component Analysis (PCA)** and **feature selection** techniques.

**Approach:**  
- Identified the best model based on accuracy, precision, recall, and F1-score.  
- Applied PCA to reduce dimensionality and selected the most important features.  
- Retrained and evaluated the optimized model to assess improvement over the baseline.

---

## ⚙️ How to Run the Code

### 🧩 Requirements
Ensure the following Python libraries are installed:

```bash
pip install pandas scikit-learn xgboost

## ▶️ Run the Notebook

You can execute the provided notebook in any Jupyter environment:

```bash
    jupyter notebook Ensemble.ipynb


The notebook includes all steps — from data preprocessing and model training to tuning and performance comparison.