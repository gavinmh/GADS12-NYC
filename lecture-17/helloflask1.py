# TODO import the class Flask from the module flask
from flask import Flask
# TODO create a new Flask app. Pass the argument __name__ to the constructor.
app = Flask(__name__)


# TODO
# In Flask, views are functions.
# Create a function called hello_flask that
# returns the string 'hello Flask!'
# TODO
# Add the app.route view decorator to the
# function to bind the function to the path '/'.
@app.route('/')
def hello_flask():
    return 'hello flask'

# TODO
# call app.run() from a main-protected block to start the application.
# Before calling run(), set the debug attribute of app to True
if __name__ == '__main__':
    app.debug = True
    app.run()