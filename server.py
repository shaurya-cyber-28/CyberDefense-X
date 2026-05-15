import os
from flask import Flask, render_template

app = Flask(__name__)

attack_data = {
    "ddos": {
        "name": "DDoS Attack",
        "risk": "High",
        "score": 82,
        "compromised": 2,
        "status": "Server overloaded by abnormal traffic flood."
    },
    "malware": {
        "name": "Malware Injection",
        "risk": "Critical",
        "score": 94,
        "compromised": 4,
        "status": "Malicious payload executed inside endpoint system."
    },
    "phishing": {
        "name": "Phishing Attack",
        "risk": "Medium",
        "score": 68,
        "compromised": 1,
        "status": "User credentials captured through fake login flow."
    },
    "mitm": {
        "name": "Man-in-the-Middle Attack",
        "risk": "High",
        "score": 78,
        "compromised": 3,
        "status": "Communication intercepted between client and server."
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate/<attack_name>")
def simulate(attack_name):
    attack = attack_data.get(attack_name)

    if attack is None:
        return "Invalid attack selected", 404

    return render_template(
        "simulate.html",
        attack=attack,
        attack_key=attack_name
    )


@app.route("/report/<attack_name>")
def report(attack_name):
    attack = attack_data.get(attack_name)

    if attack is None:
        return "Invalid attack selected", 404

    return render_template("report.html", attack=attack)


if __name__ == "__main__":
    # Render assigns a dynamic port; locally it defaults back to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # host="0.0.0.0" opens the server to external web traffic
    app.run(host="0.0.0.0", port=port, debug=True)
