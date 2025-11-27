import os

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///birthdays.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if name and month and day:
            try:
                birthday = Birthday(name=name, month=int(month), day=int(day))
                db.session.add(birthday)
                db.session.commit()
            except Exception:
                db.session.rollback()

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        # Display the entries in the database on index.html
        birthdays = Birthday.query.all()
        return render_template("index.html", birthdates=birthdays, birthdays=birthdays)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    b = Birthday.query.get(id)
    if b:
        db.session.delete(b)
        db.session.commit()
    return redirect("/")
    
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        b = Birthday.query.get(id)
        if b:
            b.name = name
            b.month = int(month)
            b.day = int(day)
            db.session.commit()

        return redirect("/")

    b = Birthday.query.get(id)
    if not b:
        return redirect("/")
    return render_template("edit.html", birthday=b)
