from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 60000, "image": "https://via.placeholder.com/200"},
    {"id": 2, "name": "Smartphone", "price": 20000, "image": "https://via.placeholder.com/200"},
    {"id": 3, "name": "Headphones", "price": 2000, "image": "https://via.placeholder.com/200"},
    {"id": 4, "name": "Watch", "price": 5000, "image": "https://via.placeholder.com/200"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
