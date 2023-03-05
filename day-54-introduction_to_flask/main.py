from flask import Flask
import time


def speed_calc_decorator(function):
    def wrapper_function():
        t0 = time.time()
        function()
        t1 = time.time()
        print(f"{function.__name__} run speed: {t1-t0}")
    return wrapper_function


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


app = Flask(__name__)


# Add some HTML and CSS to the return function
@app.route('/')
def hello_world():
    return '<h2 style="text-align: center">Hello World</h2><p>This is a paragraf</p>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">'


@app.route('/bye')
@make_bold
@make_emphasis
def bye():
    return "Bye!"


# Creating variable paths and converting the paths to specific data type
@app.route('/user/<name>/<int:number>')
def greet(name):
    return f"Hello there {name}, your number is {number}!"


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
