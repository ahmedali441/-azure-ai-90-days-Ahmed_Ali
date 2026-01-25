# Day 2: Smart API Data Fetcher

## 📋 Description
A Python script that fetches data from multiple public APIs and saves it in different formats (JSON, CSV).

## 🎯 Learning Objectives
- [x] Make HTTP requests to REST APIs
- [x] Parse JSON responses
- [x] Handle API errors gracefully
- [x] Save data in multiple formats
- [x] Generate API usage reports

## 🛠️ Technologies Used
- Python 3.9+
- Requests library (HTTP client)
- Pandas (data processing)
- JSON (data interchange)

## 📊 APIs Used
1. **JSONPlaceholder**: Fake user data for testing
2. **Weather API**: Current weather information
3. **News API**: Latest news headlines
4. **GitHub API**: User profile information

## 🚀 Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run the API fetcher
python src/main.py

# Check generated files
ls data/      # JSON files from APIs
ls outputs/   # CSV files and report
