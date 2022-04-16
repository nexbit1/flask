from flask import Flask
import random
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# @app.route('/bye')
# def bye():
#     return "bye!"
#
# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f'hello there {name}, you are {number} years old!'

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')

def home():
    return '<h1>Guess a number between 1 and 9</h1>' \
           '<img src=""/>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/eSwGh3YK54JKU/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/u2LJ0n4lx6jF6/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media1.giphy.com/media/ErZ8hv5eO92JW/giphy.gif?cid=ecf05e47rtugoys3375agnyxadwjoqkit9yl3siy2kc0h29k&rid=giphy.gif&ct=g'/>"


if __name__ == '__main__':
    app.run(debug=True) #to autoreload the server

