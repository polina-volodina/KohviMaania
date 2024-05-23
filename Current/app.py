from flask import Flask, render_template
from product import Product

app = Flask(__name__, template_folder='templates', static_folder='images')
app = Flask(__name__, static_folder='images')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)