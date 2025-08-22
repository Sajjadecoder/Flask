from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
      item_id = db.Column(db.Integer(),primary_key = True)
      name = db.Column(db.String(length=30),nullable=False) # name <= 30 characters & not null
      price = db.Column(db.Integer(),nullable=False)
      barcode = db.Column(db.String(length=12),nullable = False,unique = True)
      description = db.Column(db.String(length=100),nullable=False)
      def __repr__(self):
            return f'Item name: {self.name}'

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
