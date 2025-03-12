from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your Google Apps Script Web App URL
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbywY8lU0LMWhwyfCBJVL0v430xQZKNOTGevpkHWumJzbQlgo5B1icnC2ztaSf_GzAAv/exec"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update_qr", methods=["POST"])
def update_qr():
    data = request.json
    old_qr = data.get("oldQR")
    new_qr = data.get("newQR")

    if not old_qr or not new_qr:
        return jsonify({"error": "Please scan both QR codes."}), 400

    params = {"oldQR": old_qr, "newQR": new_qr}
    response = requests.get(SCRIPT_URL, params=params)
    
    if response.status_code == 200:
        return jsonify({"message": f"Updated QR Code for {old_qr} -> {new_qr}"})
    else:
        return jsonify({"error": "Failed to update QR code. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)
