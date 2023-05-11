from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

### # ## # ###
##  ROUTES  ##
### # ## # ###

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)


### # ### # ###
#  OLD STUFF  # (that I'll copy from)
### # ### # ###

# @app.route("/contact")
# def contact():
#     return render_template("contact.html", title="contact")

# @app.route("/about")
# def about():
#     return render_template("about.html", title="about")

# @app.route("/all_pizzas")
# def all_pizzas():
#     conn = sqlite3.connect('pizza.db')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM PIZZA")
#     results = cur.fetchall()
#     print(results)
#     return render_template("all_pizzas.html", title="all_pizzas", results=results)

# @app.route("/pizza/<int:id>")
# def pizza(id):
#     conn = sqlite3.connect('pizza.db')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM PIZZA WHERE id=?",(id,))
#     pizza = cur.fetchone()
#     cur.execute("SELECT name FROM BASE WHERE id=(SELECT base FROM PIZZA WHERE id=?)",(id,))
#     base = cur.fetchone()
#     cur.execute("SELECT name from TOPPING WHERE id IN (SELECT tid FROM PIZZATOPPING WHERE pid=?)",(id,))
#     topping = cur.fetchall()
    
#     return render_template("pizza.html", pizza=pizza, base=base, topping=topping)