# illegal-website-detection
=======
# Illegal Website Detection and Blocking

## Overview
This project uses machine learning to detect and classify illegal websites, particularly gambling and betting domains that frequently change their domain names. The model is trained to recognize patterns in domain names and classify them as either "Illegal" or "Legal."

## Features
- Extracts domain-based features such as length, number of digits, special characters, and presence of illegal keywords.
- Trains a `RandomForestClassifier` to classify websites.
- Deploys a Flask-based API for real-time classification.
- Saves and loads the trained model using `joblib`.

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- BeautifulSoup
- Joblib
- Regular Expressions (Regex)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ARAVIND2457-Q/illegal-website-detection.git
   cd illegal-website-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the model training script to generate `illegal_website_model.pkl`:
   ```bash
   python Illegal_Website_Detection.py
   ```
4. Start the Flask API:
   ```bash
   python app.py
   ```

## API Usage
The API provides an endpoint to classify a given URL:
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request Body:** JSON containing `{"url": "example.com"}`
- **Response:** JSON with classification result, e.g., `{ "url": "example.com", "classification": "Illegal" }`

### Example Usage (Using `curl`)
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"url": "1rajbet.in"}'
```

## Future Improvements
- Enhance feature extraction with more advanced NLP techniques.
- Implement real-time web scraping for continuously updating the dataset.
- Develop a frontend UI for user-friendly interaction.
- Expand classification to cover more types of illegal websites.

## Author
Aravind Dumpoju

---
Feel free to contribute, raise issues, or suggest improvements! 🚀

=======
# illegal-website-detection
>>>>>>
