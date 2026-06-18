
from flask import Flask, jsonify

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Paneer Tikka", "price": 199},
    {"id": 2, "name": "Margherita", "price": 149},
    {"id": 3, "name": "Farmhouse", "price": 229},
    {"id": 4, "name": "Mexican", "price": 249}
]

# 🌐 WEB PAGE (IMPORTANT)
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>🍕 Cloud Pizza Factory</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
                color: white;
                text-align: center;
            }

            .card {
                background: rgba(255,255,255,0.1);
                margin: 20px auto;
                padding: 20px;
                width: 60%;
                border-radius: 15px;
            }

            button {
                padding: 10px;
                margin: 5px;
                cursor: pointer;
            }

            .menu-item {
                color: #00ffcc;
                font-size: 18px;
            }
        </style>
    </head>

    <body>

        <h1>🍕 CLOUD PIZZA FACTORY</h1>

        <div class="card">
            <h2>🍕 MENU</h2>
            <button onclick="loadMenu()">Load Menu</button>
            <div id="menu"></div>
        </div>

        <div class="card">
            <h2>⚡ STATUS</h2>
            <button onclick="loadStatus()">Check Status</button>
            <div id="status"></div>
        </div>

        <script>

        function loadMenu(){
            fetch("/menu")
            .then(res => res.json())
            .then(data => {
                let html = "";
                data.forEach(item => {
                    html += `<p class="menu-item">${item.name} - ₹${item.price}</p>`;
                });
                document.getElementById("menu").innerHTML = html;
            });
        }

        function loadStatus(){
            fetch("/status")
            .then(res => res.json())
            .then(data => {
                document.getElementById("status").innerHTML =
                `<p>Kitchen: ${data.kitchen}</p>
                 <p>Orders: ${data.orders}</p>
                 <p>Delivery: ${data.delivery}</p>`;
            });
        }

        </script>

    </body>
    </html>
    """

# 📦 API
@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/status")
def status():
    return jsonify({
        "kitchen": "ACTIVE",
        "orders": "ACCEPTING",
        "delivery": "FAST",
        "system": "HEALTHY"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)