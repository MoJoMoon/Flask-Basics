# Set up your imports here!
# import ...
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome to the Latin Puppy Emporium, where we transform your puppy name into it's PuppyLatin version. Simply go to /puppy_latin/name to see your name in puppy latin!<h1>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    latin = name[0:-1]
    if name[-1] == 'y':
        return f"Hi {name}, your puppy latin name is {latin}" + "iful!"
    else:
        return f"Hi {name}, your puppy latin name is {name}" + "y!"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
