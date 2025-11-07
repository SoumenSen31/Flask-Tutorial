from flask import Flask,request,render_template,redirect

app  = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")
@app.route('/submit', methods=["POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    valid_user = {
        'admin':'123',
        'soumen':'sen',
        'user':'raj'
    }
    if username in valid_user and password in valid_user[username]:
        return render_template('welcome.html',name = username)
    else:
        return "Invalid credentials"