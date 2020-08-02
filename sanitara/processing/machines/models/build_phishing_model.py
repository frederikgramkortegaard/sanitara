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

# Clean data

results = {}

# Train Model


# Evaluate & Save Model
new_model_name = f"model_phishing_{len(list(filter(lambda x: 'model_phishing_' and '.joblib' in x, os.listdir())))}"
