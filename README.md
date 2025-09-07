# Telecom Customer Churn Analysis and Article Manager

This repository contains two distinct projects: a data analysis project on telecom customer churn and a Python script for managing articles.

---

## 1. Telecom Customer Churn Analysis

This project explores the dynamics of customer behavior and demographics in the Indian telecom sector to predict customer churn. It utilizes two datasets from four major telecom partners: Airtel, Reliance Jio, Vodafone, and BSNL.

![Cartoon of telecom customers](IMG_8811.png)

### Project Overview

The telecommunications sector in India is rapidly evolving, leading to increased competition and customer churn. Understanding the factors that influence customer retention is crucial for telecom companies to improve their services and satisfaction. This project aims to analyze customer data to identify key drivers of churn and build a predictive model.

### Datasets

The analysis is based on two CSV files:

*   `telecom_demographics.csv`: Contains information about Indian customer demographics.
    | Variable | Description |
    | :--- | :--- |
    | `customer_id` | Unique identifier for each customer. |
    | `telecom_partner` | The telecom partner associated with the customer. |
    | `gender` | The gender of the customer. |
    | `age` | The age of the customer. |
    | `state` | The Indian state in which the customer is located. |
    | `city` | The city in which the customer is located. |
    | `pincode` | The pincode of the customer's location. |
    | `registration_event` | When the customer registered with the telecom partner. |
    | `num_dependents` | The number of dependents (e.g., children) the customer has. |
    | `estimated_salary` | The customer's estimated salary. |
*   `telecom_usage.csv`: Contains information about the usage patterns of Indian customers.
    | Variable | Description |
    | :--- | :--- |
    | `customer_id` | Unique identifier for each customer. |
    | `calls_made` | The number of calls made by the customer. |
    | `sms_sent` | The number of SMS messages sent by the customer. |
    | `data_used` | The amount of data used by the customer. |
    | `churn` | Binary variable indicating whether the customer has churned or not (1 = churned, 0 = not churned). |

### How to Run the Analysis

The entire analysis is contained within the `notebook.ipynb` Jupyter Notebook. To run it, you will need to have Python and Jupyter Notebook installed.

**Required Libraries:**

You can install the necessary libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imblearn
```

The following libraries are used in the notebook:
*   pandas
*   numpy
*   matplotlib
*   seaborn
*   scikit-learn (StandardScaler, OneHotEncoder, RandomForestClassifier, LogisticRegression, etc.)
*   imblearn (SMOTE)

Once the libraries are installed, you can launch Jupyter Notebook and open `notebook.ipynb` to view and run the analysis.

---

## 2. Article Manager

This is a simple Python script (`article_manager.py`) that processes a given text, splits it into pages, and calculates a payment based on the number of pages.

### Functionality

The `ArticleManager` class in the script provides the following functionalities:
*   Splits a long string of text into pages based on a specified number of words per line and lines per page.
*   Calculates a payment amount based on the total number of pages, using a customizable payment structure.
*   Displays the paginated text along with the total page count and payment due.

### How to Run

You can run the script directly from the command line:

```bash
python article_manager.py
```

The script includes an example usage block, which will be executed when you run the file. You can modify the `article_text` and `options` variables within the script to process different articles and use different formatting/payment settings.

---

## Files in this Repository

*   `notebook.ipynb`: Jupyter Notebook containing the full analysis of telecom customer churn.
*   `customer_churn_analysis.ipynb`: (Corrupted or empty)
*   `main.ipynb`: (Corrupted or empty)
*   `article_manager.py`: Python script for processing and paginating articles.
*   `telecom_demographics.csv`: Dataset with customer demographic information.
*   `telecom_usage.csv`: Dataset with customer usage data.
*   `IMG_8811.png`: A decorative image used in the churn analysis notebook.
*   `README.md`: This file.
