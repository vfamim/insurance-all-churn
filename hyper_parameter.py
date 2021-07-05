# Import the relevant libraries
# Data manipulation
import pandas as pd
import numpy as np

# Save files
import pickle

# Machine Learning models
from xgboost import XGBClassifier
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV


# import
x_train = pd.read_csv('data/x_train.csv')
y_train = pd.read_csv('data/y_train.csv')

columns_selected = ['Gender',
                    'Age',
                    'Region_Code',
                    'Previously_Insured',
                    'Vehicle_Damage',
                    'Annual_Premium',
                    'Policy_Sales_Channel',
                    'age_class',
                    'Vehicle_Age_0',
                    'Vehicle_Age_1',
                    'Vehicle_Age_2']

x_train_fs = x_train[columns_selected]

# Model
xgb_tuning = XGBClassifier(random_state=42)

# Parameters
parameters = {
    'n_estimators': [300, 400, 500],
    'eta': [0.5],
    'max_depth': [10],
    'subsample': [0.9],
    'colsample_bytree': [0.6]
}

# Fit
xgb_tuning = HalvingGridSearchCV(xgb_tuning,
                                 parameters,
                                 verbose=1, n_jobs=1, cv=3,
                                 scoring='roc_auc')

xgb_tuning.fit(x_train_fs, y_train.values)

print(xgb_tuning.best_params_)
