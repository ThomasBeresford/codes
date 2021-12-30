
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_housing_file_path = 'C:\codes\melb_data.csv'

melbourne_home_data = pd.read_csv(melbourne_housing_file_path)

filtered_melbourne_home_data = melbourne_home_data.dropna(axis=0)

y = filtered_melbourne_home_data.Price # this is the prediction target/ what we want to predict

melbourne_home_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] # this is what we want to use to predict the price

X = filtered_melbourne_home_data[melbourne_home_features]

train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=1)

melbourne_model = DecisionTreeRegressor()

melbourne_model.fit(train_X, train_y)

val_predicted_prices = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predicted_prices))