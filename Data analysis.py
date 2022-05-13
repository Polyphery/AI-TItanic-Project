import pandas as pd
import matplotlib.pyplot as plt

db = pd.read_csv("CVSs\\train.csv")
print(db, "\n")

Survived = db["Survived"].tolist()

#|-------------------------------------------------------DATA ANALYSIS FARE-SURVIVORS-------------------------------------------------------|
Fare = db["Fare"].tolist()
Fare_set = set(Fare)
Actual_Fares = [i for i in Fare_set if str(i) != "nan"]
Fare_dict = {}
Fare_sur_dict = {}

for i in Actual_Fares:                                                                  #Creating the dictionary containing the number of each ticket -> {TicketFare : n(TicketFare)}
    Fare_dict[str(i)] = Fare.count(i)

for i in Fare_dict.keys():                                                          #creating the dictionary containing the number of survived for each ticked -> {TicketFare : n(Survived(TicketFare))}
    Fare_sur_dict[i] = len(list(db.query("Fare == {} and Survived == 1".format(i)).index))    
"""
for i in Fare_dict.keys():
    if Fare_sur_dict[i] != 0:
        print("People with the {} thicket survived:".format(i), "{:.2f}%".format(Fare_sur_dict[i]/Fare_dict[i]*100),
            "- {}".format(Fare_sur_dict[i]), "/ {}".format(Fare_dict[i]))
    else:
        print("People with the {} thicket survived: 0%".format(i),
            "- {}".format(Fare_sur_dict[i]), "/ {}".format(Fare_dict[i]))
"""

#|--------------------------------------------------DATA ANALYSIS PASSENGER CLASS-SURVIVORS--------------------------------------------------|
Pclass = db["Pclass"].tolist()
Counter1 = 0
Counter2 = 0
Counter3 = 0
for i in range(len(Survived)):                                                      #Counting how many passengers survived per class
    if Pclass[i] == 3 and Survived[i]:
        Counter1 += 1
    elif Pclass[i] == 2 and Survived[i]:
        Counter2 += 1
    elif Pclass[i] == 1 and Survived[i]:
        Counter3 += 1
"""
print("\nThird class survivors: ", "{:.2f}".format(Counter1/Pclass.count(3)*100),"%\n", 
    "Second class survivors: ", "{:.2f}".format(Counter2/Pclass.count(2)*100),"%\n", 
    "First class survivors: ", "{:.2f}".format(Counter3/Pclass.count(1)*100),"%\n\n",)
"""

#|--------------------------------------------------------DATA ANALYSIS SEX-SURVIVORS--------------------------------------------------------|
Sex = db["Sex"].tolist()
Counter1 = 0
Counter2 = 0
for i in range(len(Survived)):                                                      #Counting how many passengers survived based on the sex
    if Sex[i] == "male" and Survived[i]:
        Counter1 += 1
    elif Sex[i] == "female" and Survived[i]:
        Counter2 += 1
"""
print("Male survivors: ", "{:.2f}".format(Counter1/Sex.count("male")*100),"%\n", 
    "Female survivors: ", "{:.2f}".format(Counter2/Sex.count("female")*100), "%\n\n")
"""


#|------------------------------------------------DATA ANALYSIS SIBLINGS OR SPOUSES-SURVIVORS------------------------------------------------|
SibSp = db["SibSp"].tolist()
Amount_SibSp = set(SibSp)
Fuck_The_Name_of_This_Dictionary = {}
Fuck_This_One_Too = {}
for i in list(Amount_SibSp):                                                        #Creating a dictionary containing the number of people categorized on the amount of siblings and spouses -> {N : n(N)}
    Fuck_The_Name_of_This_Dictionary[i] = SibSp.count(i)

#print(db.query("Survived == 1 and SibSp == 0"))                                    #SQL is this you?

for i in list(Amount_SibSp):                                                        #Creating a dictionary containing the number of survivors based on the amount of siblings and spouses -> {N : n(N)}
    Fuck_This_One_Too[i] = len(list(db.query("Survived == 1 and SibSp == {}".format(i)).index))
"""
for i in Fuck_This_One_Too.keys():                                                  #Outputting the percentage of survivors
    if Fuck_This_One_Too[i] != 0:
        print("Survivors with {} siblings or spouses: ".format(i), "{:.2f}".format(Fuck_This_One_Too[i]/Fuck_The_Name_of_This_Dictionary[i]*100), "%",
            "- {}".format(Fuck_This_One_Too[i]), "/ {}".format(Fuck_The_Name_of_This_Dictionary[i]))
    else: 
        print("Survivors with {} siblings or spouses: 0%".format(i),
            "- {}".format(Fuck_This_One_Too[i]), "/ {}".format(Fuck_The_Name_of_This_Dictionary[i]))
"""
#|--------------------------------------------------------DATA ANALYSIS AGE-SURVIVORS--------------------------------------------------------|
Age = db["Age"].tolist()
Age_set = set(Age)
Actual_Age = [i for i in Age_set if str(i) != "nan"]
Age_sur_dict = {}
Age_dict = {}
for i in Actual_Age:
    Age_dict[i] = Age.count(i)
for i in Actual_Age:
    Age_sur_dict[i] = len(list(db.query("Survived == 1 and Age == {}".format(i)).index))
"""
for i in Age_sur_dict.keys():
    if Age_sur_dict[i] != 0:
        print("Survivors {} years old:".format(i), "{:.2f}".format(Age_sur_dict[i]/Age_dict[i]*100), "%",
        "- {}".format(Age_sur_dict[i]), "/ {}".format(Age_dict[i]))
    else:
        print("Survivors {} years old: 0%".format(i),
        "- {}".format(Age_sur_dict[i]), "/ {}".format(Age_dict[i]))
"""

#|-------------------------------------------------------DATA ANALYSIS CABIN-SURVIVORS-------------------------------------------------------|
db.replace("", float("NaN"), inplace = True)
db.dropna(subset = ["Cabin"], inplace = True) 
Cabins_sur = db.query("Survived == 1")
Cabins_ded = db.query("Survived == 0")

print(Cabins_sur["Cabin"].tolist(), Cabins_ded["Cabin"].tolist())
for i in Cabins_sur["Cabin"].tolist():
    if i in Cabins_ded["Cabin"].tolist():
        print(i, "- {} survived".format(Cabins_sur["Cabin"].tolist().count(i)), 
        "- {} died".format(Cabins_ded["Cabin"].tolist().count(i)))

