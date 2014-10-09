import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

print 'Training model...'
df = pd.read_csv('lyrics.csv')
y = df['Artist']
X = df['Lyrics']

pipeline = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
pipeline.fit(X, y)

# TODO import joblib from sklearn.externals
from sklearn.externals import joblib
# TODO dump the fitted pipeline to a pickle called lyrics_pipeline.pkl
joblib.dump(pipeline, 'lyrics_pipeline.pkl')