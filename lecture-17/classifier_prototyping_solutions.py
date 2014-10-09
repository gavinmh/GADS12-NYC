# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# TODO import pandas
import pandas as pd

# <codecell>

# TODO read lyrics.csv into a DataFrame
df = pd.read_csv('lyrics.csv')

# TODO what are the columns?
print df.columns

# TODO how many rows does it have?
print df.shape

# <codecell>

# TODO assign the 'Artist' column to y and the 'Lyrics' column to X
y = df['Artist']
X = df['Lyrics']

# <codecell>

# TODO import TfidfVectorizer, LogisticRegression, Pipeline, and cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score

# <codecell>

# TODO create a Pipeline containing a TfidfVectorizer and a logistic regressor
pipeline = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# TODO fit and evaluate the model with 3-fold CV
print cross_val_score(pipeline, X, y)

# <codecell>

# TODO import train_test_split
from sklearn.cross_validation import train_test_split

# TODO train/test split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y)

# TODO fit the pipeline on the training data
pipeline.fit_transform(X_train, y_train)

# TODO make predictions for the test set
predictions = pipeline.predict(X_test)

# TODO import classification_report
from sklearn.metrics import classification_report

# TODO print the classification report
print classification_report(y_test, predictions)

# <codecell>


