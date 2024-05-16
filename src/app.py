from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for username and password
user_credentials = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_credentials['username'] = username
    user_credentials['password'] = password
    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Fetch additional user information
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        gender = request.form['gender']
        # You can do whatever you want with this information, for now, let's just display it
        return render_template('profile.html', user=user_credentials, name=name, age=age, email=email, gender=gender)
    else:
        return render_template('profile.html', user=user_credentials)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
