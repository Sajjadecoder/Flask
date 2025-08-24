from market import app,render_template,db
from market.models import Item,User
from flask import redirect,url_for
from market.forms import RegisterForm
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
                       password_hash = form.password1.data)
    
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors!={}: #a check for errors in form input
        for err_msg in form.errors.values():
            print(f'Error encountered while registering User: {err_msg}')
    return render_template('register.html',form=form)



@app.route('/login')
def login_page():
    # form = RegisterForm()
    return f'<h1>Login page</h1>'

# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
