from flask import Flask, render_template
from product import Product
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='images')
app = Flask(__name__, static_folder='images')
app = Flask(__name__)

@app.route("/")
# Initialize money and coffee count
money = 0
coffee_count = 0

@app.route('/')
def index():
    return render_template("index.html")
    global money, coffee_count
    return render_template('index.html', money=money, coffee_count=coffee_count)

@app.route('/buy_coffee', methods=['POST'])
def buy_coffee():
    global money, coffee_count
    coffee_price = 10
    if money >= coffee_price:
        money -= coffee_price
        coffee_count += 1
    return redirect(url_for('index'))

@app.route('/increase_money', methods=['POST'])
def increase_money():
    global money
    money += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)