from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
#display the home page in both of the routes
def home_page():
      return render_template('home.html')
@app.route('/market')
def market_page():
       return render_template('market.html',item_name = 'Phone') 



# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
