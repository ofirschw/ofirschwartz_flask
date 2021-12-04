from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def ;():  # put application's code here
    return 'Hello to assignment 7!'


@app.route('/home')
def hello_home():  # put application's code here
    return redirect(url_for('assignment_7'))

@app.route('/contact')
def contact():  # put application's code here
    return redirect('/')

if __name__ == '__main__':
    app.run()
