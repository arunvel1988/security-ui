from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("shop.db")
    return conn

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    user = request.form["username"]
    pwd = request.form["password"]

    conn = get_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
    print("Executing Query:", query)

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return f"<h1>Welcome {user}</h1>"
    else:
        return "<h1>Invalid Credentials</h1>"

app.run(host="0.0.0.0", port=5000)
