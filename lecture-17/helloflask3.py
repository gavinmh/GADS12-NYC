# Let's make an app that we can use to get predictions
# from our classifier. We will train a classifier when
# the app initializes, and provide an endpoint that makes
# predictions for lyrics provided as path parameters.
# TODO import pandas as pd

# TODO import TfidfVectorizer, LogisticRegression, and Pipeline

# TODO import Flask

# TODO the training data has been stemmed in a particular way.
# We must transform the test data consistently using the
# transformLyrics function from msd.stem. Import this function.



app = Flask(__name__)


# TODO load the data, create a pipeline, and fit it.


# TODO create a view called predict_artist/
# It should have one parameter called lyrics.
# TODO wrap it in the app.route decorator and bind it
# to the path '/<string:lyrics>'

    # TODO transform (stem) the lyrics

    # TODO predict the artist for the lyrics. Note that predict will
    # interpret the argument as a list.

    # TODO return a string naming the predicted artist.



# TODO create a main-block to run the app.
