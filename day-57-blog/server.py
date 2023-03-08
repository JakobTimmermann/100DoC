from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=datetime.date.today().year)


@app.route('/guess/<name>')
def guess_age_and_gender(name : str):
    name = name.capitalize()
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    return render_template("age.html", name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/8b9615625ad7fe992710"
    responses = requests.get(blog_url)
    all_posts = responses.json()
    return render_template("blog.html",posts=all_posts)

if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
