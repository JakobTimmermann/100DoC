from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    name = StringField('Kneipenname', validators=[DataRequired()])
    gmaps_url = URLField('Kneipen Addresse (Google Maps URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Tür auf z.B. 18 Uhr', validators=[DataRequired()])
    closing_time = StringField('Tür zu z.B. 2 Uhr', validators=[DataRequired()])
    bar_rating = SelectField('Allgemeines Ranking', choices=["🍺", "🍺🍺", "🍺🍺🍺", "🍺🍺🍺🍺", "🍺🍺🍺🍺🍺"])
    wifi_rating = SelectField('Rüscherl Preis', choices=["✘", "🥃", "🥃🥃", "🥃🥃🥃", "🥃🥃🥃🥃", "🥃🥃🥃🥃"])
    woodwork = SelectField('Holzvertäfelungslevel', choices=["✘", "🪵", "🪵🪵", "️🪵🪵🪵", "🪵🪵🪵🪵", "🪵🪵🪵🪵🪵"])
    submit = SubmitField('Ab damit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([element.data for element in [form.name, form.gmaps_url, form.open_time, form.closing_time, form.bar_rating, form.wifi_rating, form.woodwork]])
        print(csv_data)
        print(form.gmaps_url.data)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows[1:])
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)
