import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
from scikitplot.metrics import plot_cumulative_gain
import pickle

test = pd.read_csv('data/x_test.csv')
y_test = pd.read_csv('data/y_test.csv')

# Saving XGBoost Classifier Tuned Model
xgb_tuned = pickle.load(open('models/xgb_tuned.pkl', 'rb'))

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

prob = xgb_tuned.predict_proba(test[columns_selected])

call_1 = 20000 / len(test)
call_2 = 40000 / len(test)

fig, ax = plt.subplots(figsize=(15, 10))
skplt.metrics.plot_cumulative_gain(y_test, prob, ax=ax)
plt.axhline(0.8, 0, 1)
plt.show()
