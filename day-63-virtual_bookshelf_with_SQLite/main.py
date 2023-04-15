from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
Bootstrap(app)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    book_author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Book {self.title}'


class BookEntryForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=list(range(1, 11)))
    submit = SubmitField('Submit')


class BookUpdateForm(FlaskForm):
    rating = SelectField('Update Rating', choices=list(range(1, 11)))
    submit = SubmitField('Update')


@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        db.create_all()
        all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookEntryForm()
    if form.validate_on_submit():
        with app.app_context():
            db.create_all()
            if form.title.data in [book.title for book in db.session.query(Book).all()]:
                all_books = db.session.query(Book).all()
                return render_template("index.html", books=all_books)
            new_book = Book(title=form.title.data, book_author=form.book_author.data, rating=form.rating.data)
            db.session.add(new_book)
            db.session.commit()
            all_books = db.session.query(Book).all()
        return render_template("index.html", books=all_books)
    return render_template("add.html", form=form)


@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    form = BookUpdateForm()
    with app.app_context():
        book_to_update = Book.query.get(book_id)
        if form.validate_on_submit():
            book_to_update.rating = form.rating.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", book=book_to_update, form=form)


@app.route("/delete/<book_id>", methods=['GET', 'POST'])
def delete(book_id):
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
