from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" 

@app.route('/about')
def about_page():
    return "<h1>About page!</h1>" 

# dynamic routes
@app.route('/about/<username>')
def dynamic_about_page(username):
    return f'<h1>About page of {username}!</h1>' 
