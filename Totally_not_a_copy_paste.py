from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 


test_data = pd.read_csv("CVSs/test.csv")
train_data = pd.read_csv("CVSs/train.csv")

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch", "Fare"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

X_t, X_v, y_t, y_v = train_test_split(X, y, test_size=.25, random_state=2)

Aoi = RandomForestClassifier(n_estimators=1000, max_depth=3, random_state=2)
Aoi.fit(X_t, y_t)
random_forest = round(Aoi.score(X_t, y_t) * 100, 2)
print(random_forest)