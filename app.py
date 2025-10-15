from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import re
import math

app = Flask(__name__)

# Load trained model
model = joblib.load("illegal_website_model.pkl")

illegal_keywords = ["bet", "casino", "gambling", "rajbet", "xbet"]

def calculate_entropy(s):
    """Calculate Shannon entropy of a string."""
    if not s:
        return 0
    entropy = 0
    for c in set(s):
        p = float(s.count(c)) / len(s)
        entropy -= p * math.log2(p)
    return entropy

def extract_features(url):
    """Extract domain-based features."""
    features = {
        'length': len(url),
        'num_digits': sum(c.isdigit() for c in url),
        'contains_hyphen': 1 if '-' in url else 0,
        'num_special_chars': len(re.findall(r'[^a-zA-Z0-9]', url)),
        'illegal_keyword': 1 if any(keyword in url.lower() for keyword in illegal_keywords) else 0,
        'domain_length': len(url.split('.')[-2]) if len(url.split('.')) > 1 else len(url),
        'subdomain_count': len(url.split('.')) - 2 if len(url.split('.')) > 2 else 0,
        'tld_check': 1 if url.split('.')[-1].lower() in ['com', 'org', 'net', 'edu', 'gov'] else 0,
        'entropy': calculate_entropy(url)
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
