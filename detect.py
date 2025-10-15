from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import re

app = Flask(__name__)

# Load trained model
model = joblib.load("illegal_website_model.pkl")

illegal_keywords = ["bet", "casino", "gambling", "rajbet", "xbet"]

def extract_features(url):
    """Extract domain-based features."""
    features = {
        'length': len(url),
        'num_digits': sum(c.isdigit() for c in url),
        'contains_hyphen': 1 if '-' in url else 0,
        'num_special_chars': len(re.findall(r'[^a-zA-Z0-9]', url)),
        'illegal_keyword': any(keyword in url.lower() for keyword in illegal_keywords),
    }
    return features

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    features_df = pd.DataFrame([extract_features(url)])
    prediction = model.predict(features_df)
    result = "Illegal" if prediction[0] == 1 else "Legal"
    return jsonify({"url": url, "classification": result})

if __name__ == '__main__':
    app.run(debug=True)
