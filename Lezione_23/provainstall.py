'''
app.run() sempre a fine file, 2 modi per far partire il server:

    1 - python3 nome_file.py        modo ottimale(dentro la directory) serve app.run()

    oppure

    2 - flask --app nome_file run --port 4000

    senza app.run()

    1 - flask run --port 4000
'''

from flask import Flask, url_for

#------------------------------------------------------------------
# app = Flask(__name__)
# app.run(debug=True) # , host='127.0.0.1', port=5000 no preferenze
#------------------------------------------------------------------

# RICHIESTA GET AL SERVER

# STATIC ROUTES
#------------------------------------------------------------------
app = Flask(__name__)

@app.route('/') # su .route è possibile implementare diversi metodi .route('/', methods='')
def home() -> str:

    return "<h3>Hello, world!</h3>"

#------------------------------------------------------------------

# DYNAMIC ROUTES
#------------------------------------------------------------------
@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int) -> str:

    return f"Profilo di {username}: {age} anni"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:

    return f"Post {post_id}"

app.run(debug=True)

# URL BUILDING WITH URL_FOR() <- non è un ciclo!
# from flask import url_for

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show user profile', username='John Doe', age=30))
    print(url_for('show_post', post_id=42))

# app.run(debug=True)