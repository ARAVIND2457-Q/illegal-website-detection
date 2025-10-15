import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import math
import re

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
    """Extract features from URL."""
    features = {
        'length': len(url),
        'num_digits': sum(c.isdigit() for c in url),
        'contains_hyphen': 1 if '-' in url else 0,
        'num_special_chars': len(re.findall(r'[^a-zA-Z0-9]', url)),
        'illegal_keyword': 1 if any(keyword in url.lower() for keyword in ["bet", "casino", "gambling", "rajbet", "xbet", "porn", "xxx", "hack", "crack"]) else 0,
        'domain_length': len(url.split('.')[-2]) if len(url.split('.')) > 1 else len(url),
        'subdomain_count': len(url.split('.')) - 2 if len(url.split('.')) > 2 else 0,
        'tld_check': 1 if url.split('.')[-1].lower() in ['com', 'org', 'net', 'edu', 'gov'] else 0,
        'entropy': calculate_entropy(url)
    }
    return features

# Expanded training data (30 samples: 15 illegal, 15 legal)
urls = [
    # Illegal URLs
    "1rajbet.in", "bet365.com", "casinoonline.net", "gamblinghub.org", "rajbet.co",
    "xbet.ru", "pornstar.com", "xxxvideos.net", "hacktools.io", "cracksoftware.com",
    "darkwebmarket.onion", "illegalbetting.site", "scamcasino.biz", "fraudgambling.info", "blackjackcheat.app",

    # Legal URLs
    "google.com", "github.com", "stackoverflow.com", "wikipedia.org", "youtube.com",
    "amazon.com", "facebook.com", "twitter.com", "linkedin.com", "reddit.com",
    "microsoft.com", "apple.com", "netflix.com", "spotify.com", "dropbox.com"
]

labels = [1] * 15 + [0] * 15  # 1 for illegal, 0 for legal

# Extract features for all URLs
data = [extract_features(url) for url in urls]

# Create DataFrame
df = pd.DataFrame(data)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(df, labels)

# Save the model
joblib.dump(model, 'illegal_website_model.pkl')

print("Model trained with expanded data and new features, saved as 'illegal_website_model.pkl'")
