# ---------------- Customer Churn Analysis ------------------
# Goal: Predict whether a customer will churn based on their usage & demographics.
# Churn – The target variable i.e Yes for customer churned and No for customer stayed.
# This Project explains that the Customer churn occurs when a customer stops using a company’s service lead to revenue loss. 
# Analyzing churn helps businesses understand why customers leave and how to improve retention.
# High churn rates can affect revenue and business growth.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay,
    classification_report, roc_auc_score, roc_curve
)

# ---------------- Load Dataset ----------------
dataset = pd.read_csv("Telco-Customer-Churn.csv")
print(dataset.head())
print(dataset.info())
print(dataset.describe())

# ---------------- Handling Missing values and EDA ----------------
# Churn Distribution
sns.countplot(x='Churn', data=dataset, palette='coolwarm')
plt.title('Churn Distribution')
plt.show()

# Convert TotalCharges to numeric
dataset['TotalCharges'] = pd.to_numeric(dataset['TotalCharges'], errors='coerce')
dataset['TotalCharges'].fillna(dataset['TotalCharges'].median(), inplace=True)

# Correlation Heatmap
plt.figure(figsize=(12,6))
sns.heatmap(dataset.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Tenure vs Churn
sns.histplot(data=dataset, x="tenure", hue="Churn", multiple="stack")
plt.title("Tenure Distribution by Churn")
plt.show()

# MonthlyCharges vs Churn
sns.boxplot(x="Churn", y="MonthlyCharges", data=dataset)
plt.title("Monthly Charges by Churn")
plt.show()

# ---------------- Preprocessing ----------------
# Encode categorical variables
categorical_cols = dataset.select_dtypes(include=["object"]).columns.tolist()
categorical_cols.remove("customerID")
for col in categorical_cols:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])

# Features & Target
X = dataset.drop(['customerID', 'Churn'], axis=1)
y = dataset['Churn']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Standardize Features (mainly useful for Logistic Regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------- Model Training ----------------
# Random Forest
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# Logistic Regression (for comparison)
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# ---------------- Evaluation ----------------
def evaluate_model(y_true, y_pred, model_name, probs=None):
    print(f"\n--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))
    if probs is not None:
        print("ROC-AUC Score:", roc_auc_score(y_true, probs))
        fpr, tpr, _ = roc_curve(y_true, probs)
        plt.plot(fpr, tpr, label=f"{model_name} (AUC={roc_auc_score(y_true, probs):.2f})")

# Evaluate RandomForest
evaluate_model(y_test, rf_pred, "Random Forest", probs=rf.predict_proba(X_test)[:,1])

# Evaluate Logistic Regression
evaluate_model(y_test, lr_pred, "Logistic Regression", probs=lr.predict_proba(X_test)[:,1])

# Plot ROC Curves
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()

# Confusion Matrix (RandomForest)
cm = confusion_matrix(y_test, rf_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Churn", "Churn"])
disp.plot(cmap="coolwarm")
plt.title('Random Forest Confusion Matrix')
plt.show()
