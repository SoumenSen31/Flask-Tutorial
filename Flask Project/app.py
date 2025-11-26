from flask import Flask, render_template,request

app = Flask(__name__)
REGISTRANTS = {}
@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        Name = request.form.get('Name')
        if not Name:
            return render_template('error.html',message = "Missing Name")
        Email = request.form.get('Email')
        if not Email:
            return render_template('error.html',message = "Missing Email")
        REGISTRANTS[Name] = Email
        return render_template('welcome.html',name = Name,email = Email)
    else:
        return render_template('home.html')
@app.route('/registrants')
def registrants():
    return render_template('registrants.html',registrants = REGISTRANTS)