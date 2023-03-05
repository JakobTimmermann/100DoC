from flask import Flask
import random

CORRECT_NUMBER = random.randint(0, 10)
print(f"Correct answer is {CORRECT_NUMBER}")
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<h3 style="text-align: center">And add it to the address</h3>' \
           '<p style="text-align: center"> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></p>'


@app.route('/<int:user_number>')
def check_number(user_number):
    if user_number == CORRECT_NUMBER:
        return '<h2 style="color:green; text-align:center" >Correct answer</h2>' \
               '<p style="text-align:center"><img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"></p>'
    elif user_number < CORRECT_NUMBER:
        return '<h2 style="color:red; text-align:center" >Too low</h2>' \
               '<p style="text-align:center"><img src="https://media.giphy.com/media/UVgARihN5UEb6/giphy.gif"></p>'
    else:
        return '<h2 style="color:red; text-align:center" >Too high</h2>' \
               '<p style="text-align:center"><img src="https://media.giphy.com/media/auxDaJxhVa2By/giphy.gif"></p>'


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
