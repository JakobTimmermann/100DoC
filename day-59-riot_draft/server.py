from flask import Flask, render_template, request
import requests
import datetime
import smtplib
import os
YEAR = datetime.date.today().year

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/8b9615625ad7fe992710"
    responses = requests.get(blog_url)
    all_posts = responses.json()
    return render_template("index.html", posts=all_posts, year=YEAR)


@app.route('/about')
def about():
    return render_template("about.html", year=YEAR)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    data = request.form
    if request.method == "POST":
        send_mail(data)
        return render_template("contact.html", header="Successfully sent your message", year=YEAR)
    return render_template("contact.html", header="Contact Us", year=YEAR)


@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/8b9615625ad7fe992710"
    responses = requests.get(blog_url)
    current_post = responses.json()[int(num)-1]
    return render_template("post.html", post=current_post, year=YEAR)


def send_mail(data):
    body = []
    for info, message in data.items():
        body.append(f"{info.capitalize()}: {message}")
    body = "\n".join(body)
    my_email = "daisiduuke@gmail.com"
    app_password = os.getenv("DAISI_PASSWORD")
    print(app_password)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"jason-ti@web.de",
            msg=f"Subject:New Riot! fan message.\n\n{body}")


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
