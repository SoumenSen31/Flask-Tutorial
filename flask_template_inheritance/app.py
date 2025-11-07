from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def login():
    if(request.method == "POST"):
        phone = request.form.get("phone")
        password = request.form.get("password")
        if phone == '017' and password == 'soumen':          
            return redirect(url_for('home'))
        else:
            return "Invalid Credential"
    
    return render_template('login.html')
    

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)