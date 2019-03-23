import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from azureml.core.run import Run

# Load training data
train = pd.read_csv('./data/train.csv')

X_columns = ['Type', #'Name',
             'Age', 'Breed1', 'Breed2', 'Gender',
             'Color1', 'Color2', 'Color3', 'MaturitySize', 
             'FurLength', 'Vaccinated', 'Dewormed', 'Sterilized', 
             'Health', 'Quantity', 'Fee', 'State', #'RescuerID',
             'VideoAmt', #'Description', 'PetID',
             'PhotoAmt', 
             'IsFree', 'IsMulticolor', 'IsPurebreed']
y_columns = ['AdoptionSpeed']

train['IsFree'] = train['Fee'] == 0
train['IsMulticolor'] = (train['Color2'] != 0) | (train['Color3'] != 0)
train['IsPurebreed'] = train['Breed2'] == 0

X = train[X_columns]
y = train[y_columns]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)


classifiers = [DecisionTreeClassifier(),
               RidgeClassifier(), 
               RandomForestClassifier(n_estimators=10), 
               LogisticRegression(multi_class='auto', solver='liblinear')]

run = Run.get_context()
os.makedirs('./outputs', exist_ok=True)

best_accuracy = 0
best_model = None

for classifier in classifiers:
    classifier.fit(X_train, y_train.values.flatten())
    y_predicted = classifier.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_predicted)
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        best_model = classifier

    model_name = type(classifier).__name__
    print('Accuracy of', model_name, 'is', accuracy)
    run.log('accuracy', accuracy)
    run.log('model', model_name)

    run.log_row("Model and accuracy", model=model_name, accuracy=accuracy)

    joblib.dump(value=classifier, filename='outputs/model_' + model_name + '.pkl')

run.log('best_accuracy', best_accuracy)
run.log('best_model', type(best_model).__name__)
joblib.dump(value=best_model, filename='outputs/best_model.pkl')