from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np

test_data = pd.read_csv("CVSs/test.csv")
train_data = pd.read_csv("CVSs/train.csv")

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch", "Fare"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])
#X_test[["Pclass", "Parch", "Fare"]].replace("", np.nan, inplace = True)
#X_test.dropna(subset = [features], inplace = True)
#X_test.to_csv("idk.csv", index = False)
X_t, X_v, y_t, y_v = train_test_split(X, y, test_size = .25, random_state = 2)

Aoi = RandomForestClassifier(n_estimators = 1000, max_depth = 3, random_state = 2)
Aoi.fit(X_t, y_t)
random_forest = round(Aoi.score(X_t, y_t)*100, 2)
print(random_forest)

Aoi.fit(X_v, y_v)
random_forest = round(Aoi.score(X_v, y_v)*100, 2)
print(random_forest)
#guess = Aoi.predict(X_test)
#out = pd.DataFrame({"PassengerId" : test_data.PassengerId, "Survived" : guess})
#print(out)