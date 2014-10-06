# Interacting with the app using URL paths and reading strings
# is limiting. Let's display the prediction in an HTML document.
# TODO import the render_template function from flask
from flask import Flask
from msd.stem import transformLyrics
from sklearn.externals import joblib

app = Flask(__name__)


print 'Loading model...'
pipeline = joblib.load('lyrics_pipeline.pkl')
print 'Model loaded!'


@app.route('/<string:lyrics>')
def predict_artist(lyrics):
    lyrics = transformLyrics(lyrics)
    print 'predicting artist for %s' % lyrics
    prediction = pipeline.predict([lyrics])
    # TODO instead of returning a string, render the prediction.html template.
    # TODO create a dictionary containing the keys 'lyrics' and 'artists' that
    # TODO will be used to complete the template.
    d = {
        'lyrics': lyrics,
        'artist': prediction[0]
    }


if __name__ == '__main__':
    app.debug = True
    app.run()