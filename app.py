from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def Home_page():  # put application's code here
    return render_template('cv.html')

@app.route('/assignment8')
def assignment8():  # put application's code here
    return render_template('assignment8.html', user={'name': "Ofir schwartz", 'age': 'twenty'}, hobbies=['soccer', 'surf', 'guitar'])


if __name__ == '__main__':
    app.run()
