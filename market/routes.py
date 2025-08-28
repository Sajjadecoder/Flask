from market import app,render_template,db
from market.models import Item,User
from flask import redirect,url_for,flash,request
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from flask_login import login_user,logout_user,login_required,current_user
@app.route("/")
@app.route("/home")
#display the home page in both of the routes
def home_page():
    return render_template('home.html')
@app.route('/market',methods = ['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method=='POST':
        #Purchase item 
        print('here')
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first() 
        if p_item_object:
            if p_item_object.price > current_user.budget:
                flash(f'{purchased_item} price exceeds your budget',category='danger')
            else:
                p_item_object.buy(current_user)
                flash(f'{purchased_item} bought for {p_item_object.price}$',category='success')

        #Sell item
        sell_item = request.form.get('sold_item')
        sell_item_object = Item.query.filter_by(name=sell_item).first() 
        print('here2')
        if sell_item_object:
            if current_user.can_sell(sell_item_object):
                sell_item_object.sell(current_user)
                flash(f'{sell_item_object.name} sold for {sell_item_object.price}$',category='success')
            else:
                flash(f'Unable to sell {sell_item_object.name} for {sell_item_object.price}$',category='danger')

 
        return redirect(url_for('market_page'))
    if request.method == 'GET':
        items = Item.query.filter_by(owner=None).all()
        owned_items = Item.query.filter_by(owner = current_user.id)
        return render_template('market.html',items = items,purchase_form=purchase_form,owned_items = owned_items,selling_form = selling_form) 

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
