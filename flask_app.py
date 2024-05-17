from flask import Flask, jsonify, render_template, request
import requests  

app = Flask(__name__)

API_URL ="http://127.0.0.1:8000"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        response = requests.post(f"{API_URL}/login", json=data) 
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
