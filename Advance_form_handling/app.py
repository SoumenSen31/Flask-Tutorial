from flask import Flask , flash,url_for,request,redirect,render_template
from form import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['WTF_CSRF_SECRET_KEY'] = 'anothersupersecretkey'  # Required for csrf protection

@app.route('/' , methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"welcome {name}! You Registered successfully", "success")
        return redirect(url_for('home'))
    return render_template('form.html',form = form)

@app.route('/home')
def home():
    return render_template('home.html')