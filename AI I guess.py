from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

db = pd.read_csv("CVSs\\train.csv")
db.replace("", float("NaN"), inplace = True)
db.dropna(inplace = True) 
Rt = pd.read_csv("CVSs\\test.csv")
Rt.replace("", float("NaN"), inplace = True)
Rt.dropna(inplace = True) 
Rt.replace("female", 1, inplace = True)
Rt.replace("male", 0, inplace = True)

y = db["Survived"]
features = ["Sex", "Pclass", "Age", "Fare"]
xt = pd.get_dummies(db[features])
ohe = OneHotEncoder(handle_unknown = "ignore")
ohe.fit(db[features])
Rt[features].to_csv("idk.csv", index = False)
x = ohe.transform(Rt[features])

Aoi = RandomForestClassifier(n_estimators = 500)
Aoi.fit(xt, y)
guess = Aoi.predict(x)
out = pd.DataFrame({"PassengerId" : db.PassengerId, "Survived" : guess})
print(out)

#Results = {out["PassengerId"].tolist()[i] : out["Survived"].tolist()[i] for i in range(len(out["PassengerId"].tolist()))}
#Compar = {db["PassengerId"].tolist()[i] : db["Survived"].tolist()[i] for i in range(len(db["PassengerId"].tolist()))}
#correct = 0
#for i in Results.keys():
#    if Results[i] == Compar[i]: correct += 1

#print("{}%".format(correct/len(out["PassengerId"].tolist())*100))