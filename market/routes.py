from market import app,render_template,db
from market.models import Item,User
from flask import redirect,url_for,flash
from market.forms import RegisterForm,LoginForm
from flask_login import login_user
@app.route("/")
@app.route("/home")
#display the home page in both of the routes
def home_page():
    return render_template('home.html')
@app.route('/market')

def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items) 

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        newUser = User(username = form.username.data,
                       email = form.email.data,
                       password = form.password1.data) #this line executes the @password_setter method inside models.py 
    
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors!={}: #a check for errors in form input
        for err_msg in form.errors.values():
            flash(f'Error encountered while registering User: {err_msg}',category='danger')
    return render_template('register.html',form=form)



@app.route('/login',methods = ['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(original_password = form.password.data):
            login_user(attempted_user)
            flash(f'Successfully logged in as {attempted_user.username}!',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username or password do not match',category='danger')
    return render_template('login.html',form = form)

# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
