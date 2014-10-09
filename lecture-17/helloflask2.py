from flask import Flask
app = Flask(__name__)

# TODO
# Let's make the app more interactive
# by greeting users by name.
# Update the hello_flask function to accept
# a parameter called name.
# TODO
# Update the decorator to include a placeholder
# for a URL path parameter called name that is
# the type string.
@app.route('/<string:name>')
def hello_flask(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.debug = True
    app.run()