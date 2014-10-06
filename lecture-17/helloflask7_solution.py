from flask import Flask, render_template, request
from msd.stem import transformLyrics
from sklearn.externals import joblib

app = Flask(__name__)


print 'Loading model...'
pipeline = joblib.load('lyrics_pipeline.pkl')
print 'Model loaded!'


@app.route('/')
def lyrics_form():
    return render_template('lyrics_form.html')

@app.route('/predictions', methods=['POST'])
def predict_artist():
    lyrics = request.form['lyrics']
    lyrics = transformLyrics(lyrics)
    print 'predicting artist for %s' % lyrics
    prediction = pipeline.predict([lyrics])
    d = {
        'lyrics': lyrics,
        'artist': prediction[0]
    }
    return render_template('prediction.html', d=d)

if __name__ == '__main__':
    app.debug = True
    app.run()