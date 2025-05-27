import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import base64
import io

# Set page config
st.set_page_config(
    page_title="ML/DL Problem Solver",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inline CSS for styling
st.markdown("""
<style>
body {
    color: #333;
    font-family: Arial, sans-serif;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 4px;
    border: none;
    padding: 8px 16px;
}

.stTextInput>div>div>input {
    border-radius: 4px;
}

.stSelectbox>div>div>select {
    border-radius: 4px;
}

.stTextArea>div>div>textarea {
    border-radius: 4px;
}

.stSlider>div>div>div>div {
    background-color: #4CAF50;
}

[data-testid="stSidebar"] {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# Main app
def main():
    st.sidebar.title("ML/DL Problem Solver")
    st.sidebar.markdown("""
    **Navigate through your ML/DL problem-solving journey step by step.**
    """)
    
    # Navigation
    app_mode = st.sidebar.selectbox("Choose your problem-solving stage", 
                                   ["🏠 Home",
                                    "1️⃣ Problem Definition",
                                    "2️⃣ Data Understanding",
                                    "3️⃣ Data Preparation",
                                    "4️⃣ Model Selection",
                                    "5️⃣ Training & Evaluation",
                                    "6️⃣ Deployment & Monitoring",
                                    "📋 Summary"])
    
    # Home Page
    if app_mode == "🏠 Home":
        st.title("Machine Learning / Deep Learning Problem Solver")
        st.markdown("""
        Welcome to the ML/DL Problem Solver! This interactive guide will help you navigate through the complete 
        machine learning or deep learning problem-solving process. 
        
        **Get started by selecting a stage from the sidebar.**
        """)
        
        # Columns for overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("1. Problem Definition")
            st.markdown("""
            - Understand the business problem
            - Define success metrics
            - Identify constraints
            """)
            
        with col2:
            st.subheader("2. Data Understanding")
            st.markdown("""
            - Explore data characteristics
            - Check for data quality issues
            - Perform initial feature analysis
            """)
            
        with col3:
            st.subheader("3. Data Preparation")
            st.markdown("""
            - Handle missing values
            - Feature engineering
            - Data splitting
            """)
            
        col4, col5, col6 = st.columns(3)
        
        with col4:
            st.subheader("4. Model Selection")
            st.markdown("""
            - Choose appropriate algorithms
            - Select loss functions
            - Pick optimizers
            """)
            
        with col5:
            st.subheader("5. Training & Evaluation")
            st.markdown("""
            - Train your models
            - Hyperparameter tuning
            - Evaluate performance
            """)
            
        with col6:
            st.subheader("6. Deployment & Monitoring")
            st.markdown("""
            - Deploy your model
            - Monitor performance
            - Set up retraining
            """)
        
        st.markdown("---")
        st.subheader("Quick Start")
        if st.button("Take me through all steps"):
            st.session_state.current_step = "1️⃣ Problem Definition"
            st.rerun()
    
    # Problem Definition
    elif app_mode == "1️⃣ Problem Definition":
        st.title("1. Problem Definition")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Clearly defining your problem is the first and most crucial step in any ML/DL project. 
            A well-defined problem will guide all subsequent decisions.
            """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Problem Type")
            problem_type = st.selectbox(
                "What type of problem are you solving?",
                ["Classification", "Regression", "Clustering", "Dimensionality Reduction", 
                 "Generation (e.g., GANs)", "Reinforcement Learning", "Other"]
            )
            
            if problem_type == "Classification":
                st.info("""
                **Classification** involves predicting discrete class labels. Common algorithms include:
                - Logistic Regression
                - Decision Trees
                - Random Forest
                - SVM
                - Neural Networks
                """)
            elif problem_type == "Regression":
                st.info("""
                **Regression** involves predicting continuous values. Common algorithms include:
                - Linear Regression
                - Decision Trees
                - Random Forest
                - Neural Networks
                """)
            elif problem_type == "Clustering":
                st.info("""
                **Clustering** involves grouping similar data points. Common algorithms include:
                - K-Means
                - DBSCAN
                - Hierarchical Clustering
                - GMM
                """)
                
        with col2:
            st.subheader("Success Metrics")
            if problem_type in ["Classification", "Regression", "Clustering"]:
                metric_options = {
                    "Classification": ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC", "Confusion Matrix"],
                    "Regression": ["MSE", "RMSE", "MAE", "R² Score"],
                    "Clustering": ["Silhouette Score", "Davies-Bouldin Index", "Calinski-Harabasz Index"]
                }
                selected_metrics = st.multiselect(
                    "Select your evaluation metrics",
                    metric_options.get(problem_type, ["Custom Metric"]))
                custom_metric = None
            else:
                selected_metrics = None
                custom_metric = st.text_input("Specify your custom evaluation metric(s)")
                
            business_constraint = st.text_area("Business constraints (latency, interpretability, etc.)")
        
        st.subheader("Output Requirements")
        output_format = st.selectbox("What format should the output be in?", 
                                   ["Probabilities", "Class labels", "Continuous values", "Clusters", "Other"])
        
        interpretability = st.slider("How important is model interpretability?", 1, 10, 5)
        
        if st.button("Save Problem Definition"):
            st.session_state.problem_definition = {
                "problem_type": problem_type,
                "metrics": selected_metrics if selected_metrics else custom_metric,
                "constraints": business_constraint,
                "output_format": output_format,
                "interpretability": interpretability
            }
            st.success("Problem definition saved! Proceed to Data Understanding.")
    
    # Data Understanding
    elif app_mode == "2️⃣ Data Understanding":
        st.title("2. Data Understanding")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Understanding your data is crucial for building effective models. 
            This stage involves exploring your dataset's characteristics, quality, and patterns.
            """)
        
        st.subheader("Data Upload")
        uploaded_file = st.file_uploader("Upload your dataset (CSV, Excel)", type=["csv", "xlsx"])
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                st.session_state.dataset = df
                
                st.success("Data loaded successfully!")
                
                # Basic info
                st.subheader("Basic Information")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**First 5 rows**")
                    st.dataframe(df.head())
                
                with col2:
                    st.write("**Dataset Info**")
                    buffer = io.StringIO()
                    df.info(buf=buffer)
                    st.text(buffer.getvalue())
                
                # Data exploration
                st.subheader("Data Exploration")
                
                tab1, tab2, tab3, tab4 = st.tabs(["Statistics", "Missing Values", "Visualizations", "Correlations"])
                
                with tab1:
                    st.write("**Descriptive Statistics**")
                    st.dataframe(df.describe())
                
                with tab2:
                    st.write("**Missing Values Analysis**")
                    missing_data = df.isnull().sum().to_frame(name="Missing Values")
                    missing_data["Percentage"] = (missing_data["Missing Values"] / len(df)) * 100
                    st.dataframe(missing_data)
                    
                    # Visualize missing values
                    plt.figure(figsize=(10, 6))
                    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
                    st.pyplot(plt)
                
                with tab3:
                    st.write("**Data Distribution**")
                    column_to_plot = st.selectbox("Select column to visualize", df.columns)
                    
                    if pd.api.types.is_numeric_dtype(df[column_to_plot]):
                        plot_type = st.selectbox("Select plot type", ["Histogram", "Box Plot", "Violin Plot"])
                        
                        plt.figure(figsize=(10, 6))
                        if plot_type == "Histogram":
                            sns.histplot(df[column_to_plot], kde=True)
                        elif plot_type == "Box Plot":
                            sns.boxplot(x=df[column_to_plot])
                        else:
                            sns.violinplot(x=df[column_to_plot])
                        st.pyplot(plt)
                    else:
                        plt.figure(figsize=(10, 6))
                        sns.countplot(y=df[column_to_plot])
                        st.pyplot(plt)
                
                with tab4:
                    st.write("**Feature Correlations**")
                    if len(df.select_dtypes(include=['float64', 'int64']).columns) > 1:
                        numeric_df = df.select_dtypes(include=['float64', 'int64'])
                        plt.figure(figsize=(12, 8))
                        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", center=0)
                        st.pyplot(plt)
                    else:
                        st.warning("Not enough numeric columns for correlation analysis.")
                
                # Save data understanding insights
                if st.button("Save Data Understanding Insights"):
                    st.session_state.data_understanding = {
                        "shape": df.shape,
                        "columns": list(df.columns),
                        "missing_values": missing_data.to_dict(),
                        "dtypes": df.dtypes.to_dict()
                    }
                    st.success("Data understanding insights saved! Proceed to Data Preparation.")
            
            except Exception as e:
                st.error(f"Error loading file: {str(e)}")
        else:
            st.warning("Please upload a dataset to proceed.")
    
    # Data Preparation
    elif app_mode == "3️⃣ Data Preparation":
        st.title("3. Data Preparation")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Prepare your data for modeling by handling missing values, encoding categorical variables, 
            scaling features, and splitting into train/test sets.
            """)
        
        if "dataset" not in st.session_state:
            st.warning("Please upload and analyze your data in the Data Understanding section first.")
        else:
            df = st.session_state.dataset.copy()
            
            st.subheader("Data Cleaning")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Handle Missing Values**")
                missing_strategy = st.selectbox(
                    "Select strategy for missing values",
                    ["Drop rows with missing values", 
                     "Fill with mean/median/mode", 
                     "Interpolation",
                     "Advanced imputation (e.g., KNN)"]
                )
                
                if missing_strategy == "Fill with mean/median/mode":
                    fill_method = st.selectbox("Select fill method", ["Mean", "Median", "Mode"])
            
            with col2:
                st.write("**Handle Categorical Data**")
                categorical_strategy = st.selectbox(
                    "Select encoding strategy for categorical variables",
                    ["One-Hot Encoding", "Label Encoding", "Ordinal Encoding", "Target Encoding"]
                )
            
            st.subheader("Feature Engineering")
            feature_engineering = st.text_area("Describe any feature engineering you plan to perform")
            
            st.subheader("Feature Scaling")
            scaling_method = st.selectbox(
                "Select scaling method",
                ["None", "Standard Scaler", "MinMax Scaler", "Robust Scaler", "Normalization"]
            )
            
            st.subheader("Train-Test Split")
            test_size = st.slider("Select test set size (%)", 10, 40, 20)
            random_state = st.number_input("Random state", value=42)
            
            if st.button("Apply Data Preparation"):
                # Simulate data preparation
                st.session_state.data_preparation = {
                    "missing_values_strategy": missing_strategy,
                    "categorical_encoding": categorical_strategy,
                    "feature_engineering": feature_engineering,
                    "scaling_method": scaling_method,
                    "test_size": test_size,
                    "random_state": random_state
                }
                
                st.success("Data preparation steps saved! Proceed to Model Selection.")
                
                # Show sample of "prepared" data
                st.write("**Sample of Prepared Data**")
                st.dataframe(df.head())
    
    # Model Selection
    elif app_mode == "4️⃣ Model Selection":
        st.title("4. Model Selection")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Select appropriate models, loss functions, and optimizers based on your problem type and data characteristics.
            """)
        
        if "problem_definition" not in st.session_state:
            st.warning("Please complete the Problem Definition section first.")
        else:
            problem_type = st.session_state.problem_definition["problem_type"]
            
            st.subheader("Algorithm Selection")
            
            if problem_type == "Classification":
                algorithms = st.multiselect(
                    "Select classification algorithms to try",
                    ["Logistic Regression", "Decision Tree", "Random Forest", 
                     "SVM", "XGBoost", "Neural Network", "Naive Bayes"]
                )
            elif problem_type == "Regression":
                algorithms = st.multiselect(
                    "Select regression algorithms to try",
                    ["Linear Regression", "Ridge Regression", "Lasso Regression",
                     "Decision Tree", "Random Forest", "XGBoost", "Neural Network"]
                )
            elif problem_type == "Clustering":
                algorithms = st.multiselect(
                    "Select clustering algorithms to try",
                    ["K-Means", "DBSCAN", "Hierarchical Clustering", "Gaussian Mixture Models"]
                )
            else:
                algorithms = st.multiselect(
                    "Select algorithms to try",
                    ["Custom Algorithm 1", "Custom Algorithm 2"]
                )
            
            st.subheader("Loss Function")
            if problem_type == "Classification":
                loss_function = st.selectbox(
                    "Select loss function",
                    ["Cross-Entropy", "Binary Cross-Entropy", "Hinge Loss", "Custom"]
                )
            elif problem_type == "Regression":
                loss_function = st.selectbox(
                    "Select loss function",
                    ["MSE", "MAE", "Huber Loss", "Custom"]
                )
            else:
                loss_function = st.text_input("Specify your loss function")
            
            st.subheader("Optimizer Selection")
            optimizer = st.selectbox(
                "Select optimizer",
                ["SGD", "Adam", "RMSprop", "Adagrad", "Adadelta", "Custom"]
            )
            
            st.subheader("Hyperparameter Tuning Strategy")
            tuning_strategy = st.selectbox(
                "Select hyperparameter tuning approach",
                ["Grid Search", "Random Search", "Bayesian Optimization", "Manual Tuning", "No Tuning"]
            )
            
            if st.button("Save Model Selection"):
                st.session_state.model_selection = {
                    "algorithms": algorithms,
                    "loss_function": loss_function,
                    "optimizer": optimizer,
                    "tuning_strategy": tuning_strategy
                }
                st.success("Model selection saved! Proceed to Training & Evaluation.")
    
    # Training & Evaluation
    elif app_mode == "5️⃣ Training & Evaluation":
        st.title("5. Training & Evaluation")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Train your selected models, evaluate their performance, and select the best one for your problem.
            """)
        
        if "model_selection" not in st.session_state:
            st.warning("Please complete the Model Selection section first.")
        else:
            st.subheader("Training Configuration")
            
            col1, col2 = st.columns(2)
            
            with col1:
                epochs = st.number_input("Number of epochs (for iterative models)", min_value=1, value=10)
                batch_size = st.number_input("Batch size", min_value=1, value=32)
            
            with col2:
                learning_rate = st.number_input("Learning rate", min_value=0.0001, max_value=1.0, value=0.001, step=0.0001, format="%.4f")
                early_stopping = st.checkbox("Use early stopping")
            
            st.subheader("Evaluation Metrics")
            if "problem_definition" in st.session_state:
                metrics = st.session_state.problem_definition["metrics"]
                st.write(f"**Selected Metrics:** {', '.join(metrics) if isinstance(metrics, list) else metrics}")
            
            # Simulate training and evaluation
            if st.button("Run Training"):
                with st.spinner("Training models..."):
                    # Simulate training process
                    import time
                    progress_bar = st.progress(0)
                    
                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)
                    
                    # Generate sample results
                    results = {
                        "Logistic Regression": {"Accuracy": 0.85, "Precision": 0.83, "Recall": 0.87},
                        "Random Forest": {"Accuracy": 0.88, "Precision": 0.86, "Recall": 0.90},
                        "Neural Network": {"Accuracy": 0.89, "Precision": 0.88, "Recall": 0.91}
                    }
                    
                    st.session_state.training_results = results
                    st.success("Training completed!")
                
                st.subheader("Results")
                
                # Display results as a table
                results_df = pd.DataFrame(st.session_state.training_results).T
                st.dataframe(results_df.style.highlight_max(axis=0))
                
                # Plot results
                st.subheader("Performance Comparison")
                fig, ax = plt.subplots(figsize=(10, 6))
                results_df.plot(kind='bar', ax=ax)
                plt.xticks(rotation=45)
                plt.ylabel("Score")
                plt.title("Model Performance Comparison")
                st.pyplot(fig)
                
                # Select best model
                st.subheader("Model Selection")
                best_model = st.selectbox("Select the best performing model", list(results.keys()))
                
                if st.button("Save Best Model"):
                    st.session_state.best_model = best_model
                    st.session_state.model_performance = results[best_model]
                    st.success(f"Saved {best_model} as the best model! Proceed to Deployment & Monitoring.")
    
    # Deployment & Monitoring
    elif app_mode == "6️⃣ Deployment & Monitoring":
        st.title("6. Deployment & Monitoring")
        
        with st.expander("ℹ️ About this stage"):
            st.markdown("""
            Deploy your trained model and set up monitoring to ensure it continues to perform well in production.
            """)
        
        if "best_model" not in st.session_state:
            st.warning("Please complete the Training & Evaluation section first.")
        else:
            st.subheader("Deployment Options")
            deployment_option = st.selectbox(
                "Select deployment method",
                ["REST API (e.g., Flask/FastAPI)", 
                 "Cloud Service (e.g., AWS SageMaker, GCP AI Platform)",
                 "Edge Device", 
                 "Batch Processing",
                 "Web Application"]
            )
            
            st.subheader("Monitoring Setup")
            monitoring_frequency = st.selectbox(
                "Monitoring frequency",
                ["Real-time", "Hourly", "Daily", "Weekly", "Monthly"]
            )
            
            monitor_metrics = st.multiselect(
                "Metrics to monitor",
                ["Accuracy", "Precision", "Recall", "Latency", "Throughput", "Data Drift", "Concept Drift"]
            )
            
            alert_threshold = st.slider("Performance degradation alert threshold (%)", 1, 50, 10)
            
            st.subheader("Retraining Strategy")
            retraining_strategy = st.selectbox(
                "Select retraining approach",
                ["On performance degradation", 
                 "Scheduled (e.g., weekly)", 
                 "Continuous learning",
                 "Manual"]
            )
            
            if st.button("Save Deployment Plan"):
                st.session_state.deployment_plan = {
                    "deployment_method": deployment_option,
                    "monitoring_frequency": monitoring_frequency,
                    "monitor_metrics": monitor_metrics,
                    "alert_threshold": alert_threshold,
                    "retraining_strategy": retraining_strategy
                }
                st.success("Deployment plan saved! Check the Summary section for a complete overview.")
    
    # Summary
    elif app_mode == "📋 Summary":
        st.title("Project Summary")
        
        if "problem_definition" not in st.session_state:
            st.warning("Please start by defining your problem in the Problem Definition section.")
        else:
            # Problem Definition Summary
            st.subheader("1. Problem Definition")
            st.json(st.session_state.problem_definition)
            
            # Data Understanding Summary
            if "data_understanding" in st.session_state:
                st.subheader("2. Data Understanding")
                st.json(st.session_state.data_understanding)
            
            # Data Preparation Summary
            if "data_preparation" in st.session_state:
                st.subheader("3. Data Preparation")
                st.json(st.session_state.data_preparation)
            
            # Model Selection Summary
            if "model_selection" in st.session_state:
                st.subheader("4. Model Selection")
                st.json(st.session_state.model_selection)
            
            # Training & Evaluation Summary
            if "best_model" in st.session_state:
                st.subheader("5. Training & Evaluation")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Best Model**")
                    st.success(st.session_state.best_model)
                
                with col2:
                    st.write("**Performance Metrics**")
                    st.json(st.session_state.model_performance)
            
            # Deployment Summary
            if "deployment_plan" in st.session_state:
                st.subheader("6. Deployment & Monitoring")
                st.json(st.session_state.deployment_plan)
            
            st.markdown("---")
            
            # Export summary
            st.subheader("Export Project Plan")
            export_format = st.selectbox("Select export format", ["PDF", "Markdown", "JSON"])
            
            if st.button("Generate Export"):
                st.success(f"Export generated in {export_format} format! (Note: This is a demo - actual export would be implemented in a production app.)")
            
            if st.button("Start New Project"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()

if __name__ == "__main__":
    main()