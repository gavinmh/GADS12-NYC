# Interacting with the app using URL paths and reading strings
# is limiting. Let's display the prediction in an HTML document.
# TODO import the render_template function from flask
from flask import Flask, render_template
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
    # TODO
    d = {
        'lyrics': lyrics,
        'artist': prediction[0]
    }
    return render_template('prediction.html', d=d)

if __name__ == '__main__':
    app.debug = True
    app.run()