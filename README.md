<h1> Table of Contents </h1>

- [Introduction](#introduction)
    - [Context](#context)
    - [The Challenge](#the-challenge)
- [Data](#data)
  - [Data Source](#data-source)
  - [Data Dimension](#data-dimension)
  - [Columns Description](#columns-description)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Univariate Analysis](#univariate-analysis)
    - [Target Variable](#target-variable)
    - [Numerical Variables Distribution](#numerical-variables-distribution)
    - [Categorical Variable](#categorical-variable)
  - [Bivariate Analysis](#bivariate-analysis)
  - [Multivariate Analysis](#multivariate-analysis)
    - [Numerical Attributes](#numerical-attributes)
    - [Categorical Variables](#categorical-variables)
- [Feature Selection](#feature-selection)
- [Machine Learning Model](#machine-learning-model)
  - [Single Performance](#single-performance)
  - [Real Performance using Cross Validation](#real-performance-using-cross-validation)
- [Business Performance](#business-performance)
  - [1. Main insights on the most relevant attributes of customers interested in purchasing auto insurance.](#1-main-insights-on-the-most-relevant-attributes-of-customers-interested-in-purchasing-auto-insurance)
  - [2. What percentage of customers interested in purchasing auto insurance will the sales team be able to reach by making 20,000 calls?](#2-what-percentage-of-customers-interested-in-purchasing-auto-insurance-will-the-sales-team-be-able-to-reach-by-making-20000-calls)
  - [3. If the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?](#3-if-the-sales-teams-capacity-increases-to-40000-calls-what-percentage-of-customers-interested-in-purchasing-auto-insurance-will-the-sales-team-be-able-to-contact)
  - [4. How many calls the sales team need to make to contact 80% of customers interested in purchasing auto insurance?](#4-how-many-calls-the-sales-team-need-to-make-to-contact-80-of-customers-interested-in-purchasing-auto-insurance)

# Introduction

![cover](https://github.com/vfamim/Insurance-all-company/blob/master/img/cover.jpg)

### Context

Insurance All is a company that provides health insurance for customers. The development team is analyzing the possibility of offering a new product to your policyholders: auto insurance.

Just like health insurance, the customers of this new auto insurance plan need to pay an annual amount to Insurance All company to obtain assured value by the company, to the cost of an eventual accident of damage to the vehicle.

Insurance All company conducted a survey for approximately 380,000 customers about their interest in joining a new auto insurance product last year. All customers expressed interest or not in purchasing auto insurance and these response were saved in a database along with other customers attributes.

The development team selected 127 thousand new customers who did not respond to the survey to participate in a campaign, which they will receive the offer of a new auto insurance product. The offer will be made by the sales team trough telephone calls.

However, the sales team has the capacity to make 20 thousand calls within campaign period.

### The Challenge

In that context, I was hired as a Data Science consultant to build a model that predicts whether or not the customer would be interested in auto insurance.
With my solution, the sales team hopes to be able to prioritize the people with the greatest interest in the new product and thus, optimize the campaign making only contacts with customers most likely to purchase the insurance.

As a result of my consultancy, I will need to deliver a report containing some analysis and answers to the following questions:

1. Main insights on the most relevant attributes of customers interested in purchasing auto insurance. 
2. What percentage of customers interested in purchasing auto insurance will the sales team be able to reach by making 20,000 calls? 
3. If the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?
4. How many calls the sales team need to make to contact 80% of customers interested in purchasing auto insurance?

# Data

## Data Source

Dataset is available on Kaggle community: [Health Insurance Cross Sell Prediction 🏠 🏥 | Kaggle](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction)

All the context was extracted from: [Como usar Data Science para fazer a empresa vender mais? – Seja Um Data Scientist](https://sejaumdatascientist.com/como-usar-data-science-para-fazer-a-empresa-vender-mais/)

## Data Dimension

The Dataset has:

* 508146 rows
* 12 columns

## Columns Description

| Variable             | Definition                                                   | DTYPE   |
| :------------------- | :----------------------------------------------------------- | ------- |
| id                   | Unique ID for the customer                                   | int64   |
| Gender               | Gender of the customer                                       | Object  |
| Age                  | Age of the customer                                          | int64   |
| Driving_License      | 0 : Customer does not have DL, 1 : Customer already has DL   | int64   |
| Region_Code          | Unique code for the region of the customer                   | float64 |
| Previously_Insured   | 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance | int64   |
| Vehicle_Age          | Age of the Vehicle                                           | object  |
| Vehicle_Damage       | 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past. | object  |
| Annual_Premium       | The amount customer needs to pay as premium in the year      | float64 |
| Policy*Sales*Channel | Anonymised Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc. | float64 |
| Vintage              | Number of Days, Customer has been associated with the company | int64   |
| Response             | 1 : Customer is interested, 0 : Customer is not interested   | int64   |

# Exploratory Data Analysis

## Univariate Analysis

### Target Variable

The customers with health insurance interest is approximately 9%. 

The number of people interested in the service is **46710** and those not interested are **461436**. This shows an imbalance data.

![img01](img/img01.svg)

### Numerical Variables Distribution

![img02](img/img02.svg)

### Categorical Variable

![img03](img/img03.svg)

## Bivariate Analysis

| Nº   | Hypothesis                                                   | validation |
| ---- | ------------------------------------------------------------ | ---------- |
| H1   | Males represent 70% of customers with Health Insurance.      | FALSE      |
| H2   | Most health insurance customers are in their 40s.            | TRUE       |
| H3   | All customers with Health Insurance has driving license.     | TRUE       |
| H4   | Vehicles under age 1 represents mojority of customers with Health Insurance. | FALSE      |
| H5   | All Vehicle with damage status represents the majority of customers with Health Insurance. | TRUE       |
| H6   | People with 100 days or more of association with the company are customers. | TRUE       |
| H7   | Most People with Previous Insured acquire Health Insurance.  | TRUE       |
| H8   | Low fee(annual premium) brings more customers.               | TRUE       |
|      |                                                              |            |

## Multivariate Analysis

### Numerical Attributes

![img04](img/img04.svg)

### Categorical Variables

![img05](img/img05.svg)

# Feature Selection

The metric to feature selection was Boruta, an all relevant feature selection wrapper algorithm, capable of working with any classification method that output variable importance measure (VIM); by default, Boruta uses Random Forest. The method performs a top-down search for relevant features by comparing original attributes' importance with importance achievable at random, estimated using their permuted copies, and progressively eliminating irrelevant features to stabilize that test.

| feature              | Rank |  Keep |
| :------------------- | ---: | ----: |
| Gender               |    1 |  True |
| Age                  |    1 |  True |
| Region_Code          |    1 |  True |
| Previously_Insured   |    1 |  True |
| Vehicle_Damage       |    1 |  True |
| Annual_Premium       |    1 |  True |
| Policy_Sales_Channel |    1 |  True |
| age_class            |    1 |  True |
| Vehicle_Age_0        |    1 |  True |
| Vehicle_Age_1        |    1 |  True |
| Vehicle_Age_2        |    1 |  True |

# Machine Learning Model

 We applied the following machine learning model to predict:

* Logistic Regression
* Decision Tree
* XGBoost Classifier

## Single Performance

|               Accuracy | Precision |   Recall |       F1 |      ROC |          |
| ---------------------: | --------: | -------: | -------: | -------: | -------- |
|               Baseline |  0.501564 | 0.092435 | 0.501499 | 0.156099 | 0.501535 |
|    Logistic Regression |  0.686717 | 0.201687 | 0.814066 | 0.323280 | 0.743945 |
|          Random Forest |  0.808875 | 0.224475 | 0.439627 | 0.297200 | 0.642940 |
|     XGBoost Classifier |  0.734035 | 0.218129 | 0.732605 | 0.336166 | 0.733393 |
| XGBooster Classifier + |  0.814799 | 0.242811 | 0.479019 | 0.322267 | 0.663904 |

## Real Performance using Cross Validation

|                          |   test_Accuracy   |  test_Precision   |       test_Recall |           test_F1 |     test_ROC      |
| -----------------------: | :---------------: | :---------------: | ----------------: | ----------------: | :---------------: |
|      Logistic Regression | 0.7948 +/- 0.0411 | 0.7392 +/- 0.0148 |  0.9104 +/- 0.095 | 0.8156 +/- 0.0486 | 0.7948 +/- 0.0411 |
| Random Forest Classifier | 0.8465 +/- 0.1287 | 0.8426 +/- 0.0464 | 0.8478 +/- 0.2734 | 0.8407 +/- 0.1855 | 0.8465 +/- 0.1287 |
|       XGBoost Classifier | 0.8252 +/- 0.0805 | 0.7757 +/- 0.0291 | 0.9127 +/- 0.1779 | 0.8372 +/- 0.0999 | 0.8252 +/- 0.0805 |
|     XGBoost Classifier + | 0.8749 +/- 0.1623 | 0.8534 +/- 0.0609 | 0.8984 +/- 0.3407 | 0.8687 +/- 0.2328 | 0.8749 +/- 0.1623 |

For the context of the project, the metric chosen was the ROC curve. 

> The ROC curve is created by plotting the true positive rate (TPR) against the false positive rate (FPR) at various threshold settings. 

<img src="img/img06.svg" style="zoom:80%;" />

> The value of AUC ranges from 0.0 to 1.0 and the threshold between the class is 0.5. That is, above this limit, the algorithm classifies in one class and below in the other class.

> The higher the AUC, better.

Among the models, the XGBoost Classifier perform better. The Hyperparameter Fine Tuning technique GridSearchCV was used. 

GridSearchCV tries all the combinations of the values passed in the dictionary and evaluates the model for each combination using the Cross-Validation method. Hence after using this function we get accuracy/loss for every combination of hyperparameters and we can choose the one with the best performance.

# Business Performance

## 1. Main insights on the most relevant attributes of customers interested in purchasing auto insurance.

* Customers with age between 40 and 50 have more interesting in insurance health.

* Customers who own vehicles between one and two years have more interesting in insurance health.

* Customers who pay less annual premium are more interesting in insurance health.

## 2. What percentage of customers interested in purchasing auto insurance will the sales team be able to reach by making 20,000 calls?

20,000 calls represents 20% of total data. The sales team will call to 51% of all interested customers, about 2.6 more time that random method.

![img07](img/bp1.png)

## 3. If the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?

40,000 calls represents 39% of total data. The sales team will call to 87% of all interested customers, about 3.9 more time that random method.

![img08](img/bp2.png)

## 4. How many calls the sales team need to make to contact 80% of customers interested in purchasing auto insurance?

To reach 80% of interested customer the sales team need 35093 calls.

![img09](img/bp3.png)