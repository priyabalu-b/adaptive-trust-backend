import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from feature_extractor import extract_features
from trust_engine import calculate_trust_score, classify_risk

app = Flask(__name__)
CORS(app)

# 🔹 Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# 🔹 Analyze API
@app.route("/analyze", methods=["POST"])
def analyze_url():
    data = request.get_json(force=True)
    url = data.get("url") if data else None

    if not url:
        return jsonify({"error": "URL not provided"}), 400

    # 🔹 Feature extraction
    features = extract_features(url)

    # 🔹 Trust calculation
    trust_score, reasons = calculate_trust_score(features)
    risk = classify_risk(trust_score)

    # 🔹 Logging (ADS / ATTACK LOG)
    log_entry = f"{datetime.datetime.now()} | {url} | {trust_score} | {risk}\n"
    with open("logs.txt", "a") as f:
        f.write(log_entry)

    return jsonify({
        "trust_score": trust_score,
        "risk_level": risk,
        "reasons": reasons
    })

# 🔹 History page
@app.route("/history")
def history():
    try:
        with open("logs.txt", "r") as f:
            return "<pre>" + f.read() + "</pre>"
    except:
        return "No history available"

if __name__ == "__main__":
    app.run(debug=True)
