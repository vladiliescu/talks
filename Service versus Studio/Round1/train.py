import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

import os
from azureml.core.run import Run


# Load training data
train = pd.read_csv('./data/train.csv')

X_columns = ['Type', #'Name',
             'Age', 'Breed1', 'Breed2', 'Gender',
             'Color1', 'Color2', 'Color3', 'MaturitySize', 
             'FurLength', 'Vaccinated', 'Dewormed', 'Sterilized', 
             'Health', 'Quantity', 'Fee', 'State', #'RescuerID',
             'VideoAmt', #'Description', 'PetID',
             'PhotoAmt']
y_columns = ['AdoptionSpeed']

X = train[X_columns]
y = train[y_columns]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)


# Train the classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Evaluate the classifier
y_predicted = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_predicted)

# Log evaluation results
print('Accuracy is', accuracy)
run = Run.get_context()
run.log('accuracy', accuracy)

# Log model
os.makedirs('./outputs', exist_ok=True)
joblib.dump(value=classifier, filename='outputs/model.pkl')

