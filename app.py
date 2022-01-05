from flask import Flask, render_template, redirect, session
from flask import url_for, request
from Pages.assignment10.assignment10 import assignment10

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(assignment10)


@app.route('/')
def Home_page():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', user={'name': "Ofir schwartz", 'age': 'twenty'}, hobbies=['soccer', 'surf', 'guitar'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    search, username, = '', ''
    user_curr = ({"id": 1, "email": "ofir.schwartz@gmail.co", "first_name": "Ofir", "last_name": "Schwartz"},
                 {"id": 2, "email": "Bogdan.Planich@gmail.co", "first_name": "Bogdan", "last_name": "Planich"},
                 {"id": 3, "email": "Dolev.Haziza@gmail.co", "first_name": "Dolev", "last_name": "Haziza"},
                 {"id": 4, "email": "Omer.Atzili@gmail.co", "first_name": "Omer", "last_name": "Atzili"},
                 {"id": 5, "email": "Din.David@gmail.co", "first_name": "Din", "last_name": "David"},
                 {"id": 6, "email": "Cheron.Chery@gmail.co", "first_name": "Cheron", "last_name": "Chery"})
    curr_method = request.method
    if curr_method == 'GET':
        if 'searchInput' in request.args:
            search = request.args['searchInput']
            return render_template('assignment9.html', search=search, users=user_curr)

    if curr_method == 'POST':
        username = request.form['name']
        session['logged_in'] = True
        session['username'] = username
    return render_template('assignment9.html', request_method=request.method, username=username)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    session['username'] = ' '
    return redirect(url_for('assignment9'))


@app.route('/assignment10')
def assignment10():
    return render_template('assignment10.html')


if __name__ == '__main__':
    app.run()


