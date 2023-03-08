from flask import Flask, render_template
import requests
import datetime
YEAR = datetime.date.today().year

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/8b9615625ad7fe992710"
    responses = requests.get(blog_url)
    all_posts = responses.json()
    return render_template("index.html", posts=all_posts, year=YEAR)


@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/8b9615625ad7fe992710"
    responses = requests.get(blog_url)
    current_post = responses.json()[int(num)-1]
    return render_template("post.html", post=current_post, year=YEAR)


if __name__ == "__main__":
    app.run(debug=True)
