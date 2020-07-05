from flask import Flask, redirect, render_template, request, session

from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = '12345678'

client = MongoClient(
    "mongodb+srv://minh:123@cluster0.yyfoe.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


# mongo = PyMongo(app)

@app.route('/free')
def fri():
    return render_template('main.html')


@app.route('/')
def index():
    if 'email' in session:
        return render_template('main.html')
    else:

        return redirect('/login')
        # print(session)


@app.route('/login', methods=['GET', 'POST'])
def logiin():
    if request.method == 'GET':
        return render_template('logi.html')
    elif request.method == 'POST':
        # form = request.form
        # email = form['email']
        # passwd = form['password']
        login_user = db.users.find_one({'email': request.form['email']})

        if login_user:
            if login_user['password'] == request.form['password']:
                session['email'] = request.form['email']
                return render_template('main.html')
            else:
                return redirect('/login')
        else:
            return redirect('/login')

        # return "Invalid name or password"


@app.route('/register', methods=['GET', 'POST'])
def regis():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # form = request.form
        # email = form['email']
        # passwd = form['password']
        new_user = db.users.find_one({'email': request.form['email']})

        if new_user is None:
            db.users.insert_one(
                {'email': request.form['email'], 'password': request.form['password'], 'fullname': request.form['firstname'] + ' ' + request.form['lastname']})
            session['email'] = request.form['email']
            return redirect('/')

        return redirect('/register')


@app.route('/logout')
def out():
    session.pop('email')
    return redirect('/')


@app.route('/exercises')
def exe():
    if 'email' not in session:
        return redirect('/')
    return render_template('exercises.html')


@app.route('/shoulder')
def shoul():
    if 'email' not in session:
        return redirect('/')
    return render_template('shoulder.html')


@app.route('/chest')
def ches():
    if 'email' not in session:
        return redirect('/')
    return render_template('chest.html')


@app.route('/back')
def bak():
    if 'email' not in session:
        return redirect('/')
    return render_template('back.html')


@app.route('/abs')
def abs():
    if 'email' not in session:
        return redirect('/')
    return render_template('abscore.html')


@app.route('/legs')
def leg():
    if 'email' not in session:
        return redirect('/')
    return render_template('legs.html')


@app.route('/profiles')
def pro():
    if 'email' not in session:
        return redirect('/')
    # return '''<nav class="mb-1 navbar navbar-expand-lg navbar-dark default-color">
    #     <a class="navbar-brand" href="/">Fitness Guru</a>
    #     <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-333"
    #         aria-controls="navbarSupportedContent-333" aria-expanded="false" aria-label="Toggle navigation">
    #         <span class="navbar-toggler-icon"></span>
    #     </button>
    #     <div class="collapse navbar-collapse" id="navbarSupportedContent-333">
    #         <ul class="navbar-nav mr-auto">
    #             <li class="nav-item active">
    #                 <a class="nav-link" href="#">Home
    #                     <span class="sr-only">(current)</span>
    #                 </a>
    #             </li>
    #             <li class="nav-item">
    #                 <a class="nav-link" href="/exercises">Exercises</a>
    #             </li>
    #         </ul>
    #         <ul class="navbar-nav ml-auto nav-flex-icons">
    #             <li class="nav-item">
    #                 <a class="nav-link waves-effect waves-light">
    #                     <i class="fab fa-twitter"></i>
    #                 </a>
    #             </li>
    #             <li class="nav-item">
    #                 <a class="nav-link waves-effect waves-light">
    #                     <i class="fab fa-google-plus-g"></i>
    #                 </a>
    #             </li>
    #             <li class="nav-item dropdown">
    #                 <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink-333" data-toggle="dropdown"
    #                     aria-haspopup="true" aria-expanded="false">
    #                     <i class="fas fa-user"></i>
    #                 </a>
    #                 <div class="dropdown-menu dropdown-menu-right dropdown-default"
    #                     aria-labelledby="navbarDropdownMenuLink-333">
    #                     <a class="dropdown-item" href="#">My plan</a>
    #                     <a class="dropdown-item" href="#">Log out</a>
    #                 </div>
    #             </li>
    #         </ul>
    #     </div>
    # </nav>
    myuser = db.users.find_one({'email': session['email']})
    full = myuser['fullname']
    return '''
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <link rel="stylesheet" href="../static/css/bootstrap.min.css">
    <link rel="stylesheet" href="../static/css/mdb.min.css">
    <link rel="stylesheet" href="../static/css/style.css">
    <script type="text/javascript" src="../static/js/jquery.min.js"></script>
    <script type="text/javascript" src="../static/js/popper.min.js"></script>
    <script type="text/javascript" src="../static/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="../static/js/mdb.min.js"></script>
    <nav class="mb-1 navbar navbar-expand-lg navbar-dark default-color">
        <a class="navbar-brand" href="/">Fitness Guru</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-333"
            aria-controls="navbarSupportedContent-333" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent-333">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home
                        <span class="sr-only">(current)</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/exercises">Exercises</a>
                </li>
            </ul>
            <ul class="navbar-nav ml-auto nav-flex-icons">
                <li class="nav-item">
                    <a class="nav-link waves-effect waves-light">
                        <i class="fab fa-twitter"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link waves-effect waves-light">
                        <i class="fab fa-google-plus-g"></i>
                    </a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink-333" data-toggle="dropdown"
                        aria-haspopup="true" aria-expanded="false">
                        <i class="fas fa-user"></i>
                    </a>
                    <div class="dropdown-menu dropdown-menu-right dropdown-default"
                        aria-labelledby="navbarDropdownMenuLink-333">
                        <a class="dropdown-item" href="/profiles">My profile</a>
                        <a class="dropdown-item" href="/logout">Log out</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
    <h1 style="text-align: center;">You are currently logged in as {} </h1>'''.format(full)


if __name__ == '__main__':
    app.run()
