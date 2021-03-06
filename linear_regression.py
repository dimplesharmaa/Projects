# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aYlAnCZAf-Ksna6c-7kwHsRg611KxiMk
"""

import pandas as pd
df = pd.read_csv('Advertising.csv')
df.head()

X=df[['TV']].values
Y=df[['sales']].values

from sklearn.linear_model import LinearRegression
lmodel = LinearRegression()
lmodel.fit(X,Y)

print(lmodel.coef_)
print(lmodel.intercept_)

Ypred = lmodel.predict(X)

print(((Y-Ypred)**2).mean())

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X,Ypred,c='g')
plt.show()

"""For multi variables"""

#TV,Radio
X = df[['TV','radio']].values
Y = df[['sales']].values

lmodel2 = LinearRegression()
lmodel2.fit(X,Y)

Ypred = lmodel2.predict(X)
error_value = ((Y-Ypred)**2).mean()
print(error_value)
print(lmodel2.coef_)
print(lmodel2.intercept_)

"""For 3 variables"""

X = df[['TV','radio','newspaper']]
Y = df[['sales']]

lmodel3 = LinearRegression()
lmodel3.fit(X,Y)

Ypred = lmodel3.predict(X)
error_value = ((Y-Ypred)**2).mean()
print(error_value)
print(lmodel3.coef_)
print(lmodel3.intercept_)

#[[120.5]]
#[[120.5,76]]
#[[120.5,76,150]]
print(lmodel.predict([[120.5]]))
print(lmodel2.predict([[120.5,76]]))
print(lmodel3.predict([[120.5,76,150]]))

df = df[['TV','radio','newspaper','sales']]
df.corr()       # we can reject the attributes with less corr value. sales is affecting least by newspaper advertisement here

np.hstack((Ypred,Y))

"""**LINEAR REGRESSION USING MEDIUM BLOG BY NAGESH SINGH CHAUHAN**"""

import pandas as pd
data = pd.read_csv('weather.csv')
data.head()

data.shape

data.describe()

# We'll predict max temperature based on minimum temperature
x = data['MinTemp'].values.reshape(-1,1)
y = data['MaxTemp'].values.reshape(-1,1)

plt.scatter(x,y)
plt.show

# Splitting the dataset into test and train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Training the alogrithm
from sklearn.linear_model import LinearRegression
r = LinearRegression()  
r.fit(x_train, y_train)

#To retrieve the intercept:
print(r.intercept_)
#For retrieving the slope:
print(r.coef_)

# make predictions on testing dataset
y_pred = r.predict(x_test)

# Compare the actual values with the predicted values
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

# Comparing actual and predicted values using bar graph
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# Plotting the best fit line on the graph
plt.scatter(x_test, y_test,  color='gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.show()

# Evaluating the performance of algorithm. 3 evaluation metrics are commonly used
from sklearn import metrics
# 1. Mean Absolute Error (MAE)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 
# 2. Mean Squared Error (MSE)
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# 3. Root Mean Squared Error (RMSE)
import numpy as np
np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

"""**Doubt**: How to judge or evaluate the performance of our linear regression model via errors?

**MULTI-VARIABLE LINEAR REGRESSION**
"""

wine = pd.read_csv('wine.csv')
wine.head()

# Commented out IPython magic to ensure Python compatibility.
# Importing all the required libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# %matplotlib inline

wine.shape

wine.describe()

wine.isnull().sum()

# Separating features/attributes and labels
X = wine[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']].values
Y = wine['quality'].values

# Splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Training the model
wmodel = LinearRegression()  
wmodel.fit(X_train, Y_train)

# Getting the coefficients/ slopes
import pandas as pd
coeff_df = pd.DataFrame(wmodel.coef_, columns=['Coefficient'])  
coeff_df

# Doubt: How to print the table with the variable names too
# This means that for a unit increase in ???density???, there is a decrease of 31.51 units in the quality of the wine.

# Predicting the test set
Y_pred = wmodel.predict(X_test)

df = pd.DataFrame({'Actual': Y_test, 'Predicted': Y_pred})
df1 = df.head(25)
df1

print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))

#You can see that the value of root mean squared error is 0.62, which is
# slightly greater than 10% of the mean value which is 5.63. This means 
# that our algorithm was not very accurate but can still make reasonably 
# good predictions.

"""**REASONS FOR INACCURACIES IN THE MODEL**
1.   More data is required
2.   Bad assumptions i.e. this data has a linear relationship which might not be true
3.   Poor features ie features used may not have had a high enough correlation to the values we are trying to predict




"""