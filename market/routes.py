from market import app,render_template
from market.models import Item

@app.route("/")
@app.route("/home")
#display the home page in both of the routes
def home_page():
    return render_template('home.html')
@app.route('/market')

def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items) 



# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
