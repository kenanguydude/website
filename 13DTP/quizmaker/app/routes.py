from flask import Flask, render_template, request, make_response
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database/quizmaker.db')
cur = conn.cursor()

# routes


@app.route("/")
def home():
    """The page it brings you to when you open the website."""
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)