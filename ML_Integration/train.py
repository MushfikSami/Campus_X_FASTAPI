import pickle
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('/content/House Price Prediction Dataset.csv').drop(['Location','Condition','Garage'],axis=1)
df.head()


x=df.drop('Price',axis=1)
y=df['Price']



model=LinearRegression()
model.fit(x,y)

joblib.dump(model,'model_joblib')