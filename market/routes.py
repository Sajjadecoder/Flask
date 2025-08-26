from market import app,render_template,db
from market.models import Item,User
from flask import redirect,url_for,flash
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from flask_login import login_user,logout_user,login_required
@app.route("/")
@app.route("/home")
#display the home page in both of the routes
def home_page():
    return render_template('home.html')
@app.route('/market')
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    items = Item.query.all()
    return render_template('market.html',items = items,purchase_form=purchase_form) 

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        newUser = User(username = form.username.data,
                       email = form.email.data,
                       password = form.password1.data) #this line executes the @password_setter method inside models.py 
    
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser.username)
        flash(f'Account Created and Successfully logged in as {newUser.username}',category='success')
        
        
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

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'Logged Out Successfully',category='info')
    return redirect(url_for('home_page'))    









# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
