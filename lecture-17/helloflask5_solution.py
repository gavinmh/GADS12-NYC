from flask import Flask
from msd.stem import transformLyrics
from sklearn.externals import joblib
app = Flask(__name__)


# TODO instead of training the model on startup,
# load the pickled pipeline
print 'Loading model...'
pipeline = joblib.load('lyrics_pipeline.pkl')
print 'Model loaded!'


@app.route('/<string:lyrics>')
def predict_artist(lyrics):
    lyrics = transformLyrics(lyrics)
    print 'predicting artist for %s' % lyrics
    prediction = pipeline.predict([lyrics])
    return 'Predicted Artist: %s' % prediction

if __name__ == '__main__':
    app.debug = True
    app.run()