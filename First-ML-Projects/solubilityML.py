import pandas as pd


# Loading Dataset of Molecules Solubility using Physics-informed Learning
df = pd.read_csv('https://raw.githubusercontent.com/oplogix/Projects/main/First-ML-Projects/delaney_solubility_with_descriptors.csv')


#Data Preparation

#Data separation as X and Y

y = df['logS']

x = df.drop('logS', axis=1)   #Axis: 1 = Column, 0 = Row

#Data Splitting

from sklearn.model_selection import train_test_split  # From scikit-learn module

#Training set = 80% of the data, while the test set = 20% of the data.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100) # Defining new variables


# Linear Regression Model - First Model

# Training the Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# Train LR Model on this dataset
lr.fit(x_train, y_train)

LinearRegression()

# Applying the model to make a prediction
y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)

# Evaluate Model Performance
from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

# Organizing Data of LR Model
lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']


# Random Forest Training Model - Second model 

# Training the Model
from sklearn.ensemble import RandomForestRegressor   # Using Regressor because Y value (LogS in Quantatative), Categorical would be Classification model

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train, y_train)

# Applying the Model to make a Prediction
y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

# Evaluating Models Performance

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

# Organizing RF Data

rf_results = pd.DataFrame(['Random Forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']



# Model Comparison
df_models = pd.concat([lr_results, rf_results], axis=0).reset_index(drop=True)
print(df_models)


# Creating ScatterPlot

import matplotlib.pyplot as plt
import numpy as np

x = [y_train]
y = [y_lr_train_pred]

plt.figure(figsize=(10,10))
plt.scatter(x, y, alpha=0.3)
plt.title("Linear Regression Graph")
plt.ylabel('Predict LogS')
plt.xlabel('Expirimental LogS')
plt.show()

# #Get Trendline Coefficients and Polynomial
# z = np.polyfit(x, y, 1) -  ("expected 1D vector for x") - https://stackoverflow.com/questions/33177548/typeerror-expected-1d-vector-for-x
# p = np.poly1d(z)

# #Add Trendline
# plt.plot(x, p(x), '#F8766D')