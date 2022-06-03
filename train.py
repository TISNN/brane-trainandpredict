#!/usr/bin/env python3

import yaml
import sys
import os
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

def train_predict(source: str) -> str:
    ### alterative for pytest
    file_path = "/data"
    if source[:3] == "py_":
        file_path = "./data"
        source = source[3:]

    train = pd.read_csv(f"{file_path}/train_traindata.csv")
    test = pd.read_csv(f"{file_path}/test_testdata.csv")
    testid = pd.read_csv(f"{file_path}/test.csv")
    X = train.values[:,1:]
    y = train.values[:,0]

    if source == "knn":
        knn = KNeighborsClassifier(n_neighbors = 3)
        knn.fit(X, y)
        Y_pred = knn.predict(X)
        acc_knn = round(knn.score(X, y) * 100, 2)
        pickle.dump(knn, open(f"{file_path}/{source}.pkl", 'wb'))
        predictions = knn.predict(test)
        PassengerId=testid['PassengerId']
        prdict_test = pd.DataFrame({"PassengerId": PassengerId, "Survived": predictions.astype(np.int32)})
        prdict_test.to_csv(f"{file_path}/{source}_results.csv")

        return "Accuracy of KNN model is "+ str(acc_knn) + " and the KNN results was saved at /data"

    if source == "decision_tree":
        decision_tree = DecisionTreeClassifier()
        decision_tree.fit(X, y)
        Y_pred = decision_tree.predict(X)
        acc_decision_tree = round(decision_tree.score(X, y) * 100, 2)
        pickle.dump(decision_tree, open(f"{file_path}/{source}.pkl", 'wb'))
        predictions = decision_tree.predict(test)
        PassengerId=testid['PassengerId']
        prdict_test = pd.DataFrame({"PassengerId": PassengerId, "Survived": predictions.astype(np.int32)})
        prdict_test.to_csv(f"{file_path}/{source}_results.csv")

        return "Accuracy of decision tree model is "+ str(acc_decision_tree) + " and the decision_tree results was saved at /data"


if __name__ == "__main__":
    # Make sure that at least one argument is given, that is either 'write' or 'read'
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} write|read")
        exit(1)

    # If it checks out, call the appropriate function
    command = sys.argv[1]
    if command == "train_predict":
        print(yaml.dump({ "contents": train_predict(os.environ["SOURCE"]) }))
