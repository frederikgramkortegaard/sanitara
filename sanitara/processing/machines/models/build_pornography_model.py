""" """
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import pickle
import csv
import os

from joblib import dump

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.ensemble import VotingClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics

# Load data
df = pd.read_csv("../../../data/pornography_url_data.csv",  sep='\s*,\s*', nrows=200000)

# Clean data
df['label'] = df['label'].astype('str')
df['label'].replace("nan", "0.0", inplace=True)
df['name'] = df['name'].astype('str')
df = df.iloc[0: df.groupby("label").count().iloc[1]['name'] * 2]

results = {}

# Train Model
for test_size in [0.3]:
    print(f"test size, {test_size}")
    X_train, X_test, y_train, y_test = train_test_split(df["name"], df["label"], test_size=test_size, random_state=1, shuffle=True, stratify=df['label'])
    print(f"Len of Train: {len(X_train)}, Len of Test: {len(X_test)}")

    text_clf = Pipeline([
        ('vect', CountVectorizer(max_df=1.0, max_features=None, ngram_range=(1,1))),
        ('tfidf', TfidfTransformer(norm='l1', use_idf=True)),
        ('clf', SGDClassifier(max_iter=50, penalty='l2', alpha=1e-05))
    ])

    text_clf.fit(X_train, y_train)
    predicted = text_clf.predict(X_test)

    # Evaluate & Save Model
    metric = metrics.classification_report(y_test, predicted, target_names=["0", "1"])
    new_model_name = f"model_pornography_{len(list(filter(lambda x: 'model_pornography_' and '.joblib' in x, os.listdir())))}"

    cross_validation = cross_validate(text_clf, df['name'], df['label'], return_train_score=True)
    
    with open(f"{new_model_name}.log", 'w') as f:
        f.write(f"-> {new_model_name} : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        f.write(f"\nDataset: Len of Train: {len(X_train)}, Len of Test: {len(X_test)}")
        f.write(f"\nTest size: {str(test_size * 100)}% of dataset")
        f.write(f"\nMean Accuracy: {np.mean(predicted == y_test)}")
        f.write("\nMetrics:\n" + metric.strip())
        f.write("\nCross Validation:\n" + '\n'.join([f'{key}: {value}' for key,value in cross_validation.items()]))

    print(f"wrote evaluation log to {new_model_name}.log")
    dump(text_clf, new_model_name+".joblib")
    print(f"saved model as {new_model_name}.joblib")
