# TODO List for Illegal Website Detection Modifications

## 1. Update Training Data and Features in Illegal_Website_Detection.py
- [x] Expand training data from 10 to 30 samples (15 illegal, 15 legal)
- [x] Add new features: domain_length, subdomain_count, tld_check, entropy

## 2. Update Feature Extraction in app.py
- [x] Modify extract_features function to include new features

## 3. Redesign Web Interface in templates/index.html
- [x] Update to modern design with better colors, icons, responsive layout
- [x] Improve result display

## 4. Retrain the Model
- [x] Run Illegal_Website_Detection.py to retrain with new data and features

## 5. Restart Flask App
- [x] Stop current app and restart with updated code
