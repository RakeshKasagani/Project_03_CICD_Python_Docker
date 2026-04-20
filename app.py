from flask import Flask, render_template

app = Flask(__name__)

# Sample product data with FIXED image URLs
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 60000,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=300&h=200&fit=crop"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 20000,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=300&h=200&fit=crop"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000,
        "image": "https://images.unsplash.com/photo-1518449033319-6cdbb6b0d8c0?w=300&h=200&fit=crop"
    },
    {
        "id": 4,
        "name": "Watch",
        "price": 5000,
        "image": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?w=300&h=200&fit=crop"
    }
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
