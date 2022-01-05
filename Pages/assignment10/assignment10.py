from flask import redirect, request, Blueprint, render_template
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10.py',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='@ofiR1994', database='ofirweb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/insertion', methods=['GET', 'POST'])
def insertion():
    if request.method == 'POST':
        idnum = request.form['id']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        query = "Insert into users (idUsers, Email, first_name, last_name) VALUES ('%s', '%s', '%s', '%s')" % (
        idnum, email, first_name, last_name)
        interact_db(query, 'commit')
    return render_template('assignment10.html')


@assignment10.route('/Deletion', methods=['GET', 'POST'])
def Deletion():
    if request.method == 'POST':
        idnum = request.form['id']
        query = "DELETE FROM users WHERE idUsers='%s';" % idnum
        interact_db(query, 'commit')
        return redirect('/assignment10')


@assignment10.route('/updating', methods=['GET', 'POST'])
def updating():
    if request.method == 'POST':
        idnum = request.form['id']
        email = request.form['email']
        query = "UPDATE users SET Email = '%s' WHERE idUsers = '%s' " % (email, idnum)
        interact_db(query, query_type='commit')
        return redirect('/assignment10')


@assignment10.route('/assignment10')
@assignment10.route('/users')
def users():
    query = "select * from users;"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


