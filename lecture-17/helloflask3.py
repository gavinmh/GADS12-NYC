# Let's make an app that we can use to get predictions
# from our classifier. We will train a classifier when
# the app initializes, and provide an endpoint that makes
# predictions for lyrics provided as path parameters.
# TODO import pandas as pd
import pandas as pd
# TODO import TfidfVectorizer, LogisticRegression, and Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
# TODO import Flask
from flask import Flask
# TODO the training data has been stemmed in a particular way.
# We must transform the test data consistently using the
# transformLyrics function from msd.stem. Import this function.
from msd.stem import transformLyrics

app = Flask(__name__)
df = pd.read_csv('lyrics.csv')
# TODO load the data, create a pipeline, and fit it.
pipeline = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
X = df['Lyrics']
y = df['Artist']
pipeline.fit(X, y)
# TODO create a view called predict_artist/
# It should have one parameter called lyrics.
# TODO wrap it in the app.route decorator and bind it
# to the path '/<string:lyrics>'
@app.route('/<string:lyrics>')
def predict_artist(lyrics):
    # TODO transform (stem) the lyrics
    lyrics = transformLyrics(lyrics)
    # TODO predict the artist for the lyrics. Note that predict will
    # interpret the argument as a list.
    prediction = pipeline.predict([lyrics])
    # TODO return a string naming the predicted artist.
    return 'Predicted Artist: %s' % prediction


# TODO create a main-block to run the app.
if __name__ == '__main__':
    app.debug = True
    app.run()