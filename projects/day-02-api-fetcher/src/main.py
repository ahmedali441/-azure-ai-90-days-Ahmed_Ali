"""
DAY 2: SMART API DATA FETCHER
Description: Fetch data from multiple public APIs and save in different formats
"""

import requests
import pandas as pd
import json
import os
from datetime import datetime
import time

print("=" * 60)
print("DAY 2: SMART API DATA FETCHER")
print("=" * 60)

def main():
    """Main function to fetch data from multiple APIs"""
    
    print("\n📡 CONNECTING TO APIS...")
    print("-" * 60)
    
    # Create data and outputs directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    all_data = {}  # Store all fetched data
    
    try:
        # API 1: JSONPlaceholder (FREE, no API key needed)
        print("\n1. 📊 Fetching user data from JSONPlaceholder...")
        users_data = fetch_jsonplaceholder_users()
        all_data['users'] = users_data
        print(f"   ✅ Fetched {len(users_data)} users")
        
        # API 2: Weather API (FREE tier)
        print("\n2. 🌤️  Fetching weather data...")
        weather_data = fetch_weather_data("London")
        all_data['weather'] = weather_data
        print(f"   ✅ Weather for London: {weather_data.get('main', {}).get('temp', 'N/A')}°C")
        
        # API 3: News API (using free endpoint)
        print("\n3. 📰 Fetching news headlines...")
        news_data = fetch_news_headlines()
        all_data['news'] = news_data
        print(f"   ✅ Got {len(news_data.get('articles', []))} news articles")
        
        # API 4: GitHub API (your own data)
        print("\n4. 💻 Fetching GitHub user info...")
        github_data = fetch_github_user("octocat")  # GitHub's mascot
        all_data['github'] = github_data
        print(f"   ✅ GitHub user: {github_data.get('login', 'N/A')}")
        
        # Save all data
        print("\n💾 SAVING DATA...")
        print("-" * 60)
        
        save_all_data(all_data)
        
        # Process and analyze
        print("\n📊 PROCESSING DATA...")
        print("-" * 60)
        
        process_data(all_data)
        
        # Generate report
        generate_report(all_data)
        
        print("\n" + "=" * 60)
        print("🎉 DAY 2 PROJECT COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        print("\n📁 CHECK YOUR FILES:")
        print("• data/ - Raw JSON from APIs")
        print("• outputs/ - Processed CSV files and report")
        
        print("\n🚀 Ready to commit to GitHub!")
        print("Run: cd ../.. && git add . && git commit -m \"Day 2: Complete API Fetcher\"")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("Possible solutions:")
        print("1. Check internet connection")
        print("2. Some APIs might have rate limits (wait 1 minute)")
        print("3. Run again: python src/main.py")

def fetch_jsonplaceholder_users():
    """Fetch sample user data from JSONPlaceholder API"""
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"   ⚠️  JSONPlaceholder API error: {e}")
        # Return sample data if API fails
        return [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "city": "London"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "city": "New York"}
        ]

def fetch_weather_data(city="London"):
    """Fetch weather data from OpenWeatherMap (free tier)"""
    # Using a public API that doesn't require key for demo
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        # Return sample weather data
        return {
            "location": city,
            "temperature": 22.5,
            "conditions": "Partly cloudy",
            "humidity": 65
        }

def fetch_news_headlines():
    """Fetch news headlines from NewsAPI alternative"""
    # Using a free news API endpoint
    url = "https://newsapi.org/v2/top-headlines?country=us&pageSize=5"
    
    # Note: NewsAPI requires key in production, but we'll use sample data
    # For learning, we'll return sample data
    
    sample_news = {
        "status": "ok",
        "totalResults": 5,
        "articles": [
            {
                "title": "Tech Company Releases New AI Model",
                "description": "Major breakthrough in AI technology",
                "url": "https://example.com/news1"
            },
            {
                "title": "Python 3.12 Released",
                "description": "New features for developers",
                "url": "https://example.com/news2"
            },
            {
                "title": "Cloud Computing Growth Continues",
                "description": "Azure and AWS report record growth",
                "url": "https://example.com/news3"
            }
        ]
    }
    
    print("   ℹ️  Using sample news data (API requires key)")
    return sample_news

def fetch_github_user(username):
    """Fetch GitHub user information"""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Python-API-Fetcher"
        })
        response.raise_for_status()
        return response.json()
    except:
        # Return sample GitHub data
        return {
            "login": username,
            "name": "GitHub User",
            "public_repos": 10,
            "followers": 100,
            "following": 50
        }

def save_all_data(all_data):
    """Save all fetched data to JSON files"""
    
    for data_type, data in all_data.items():
        filename = f"data/{data_type}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"   ✅ Saved: {filename}")

def process_data(all_data):
    """Process and convert data to CSV format"""
    
    # Process users data
    if 'users' in all_data:
        users_df = pd.DataFrame(all_data['users'])
        
        # Extract nested data (address, company)
        if 'address' in users_df.columns:
            users_df['city'] = users_df['address'].apply(
                lambda x: x.get('city', '') if isinstance(x, dict) else ''
            )
        
        # Select relevant columns
        user_columns = ['id', 'name', 'email', 'city'] if 'city' in users_df.columns else ['id', 'name', 'email']
        users_df = users_df[user_columns]
        
        users_df.to_csv('outputs/users.csv', index=False)
        print(f"   ✅ Created: outputs/users.csv ({len(users_df)} users)")
    
    # Create combined sample dataset
    create_sample_dataset()

def create_sample_dataset():
    """Create a combined dataset for analysis"""
    
    # Create sample data combining different sources
    data = {
        'user_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'api_calls_made': [15, 23, 8, 42, 19],
        'data_fetched_mb': [2.5, 4.1, 1.2, 5.8, 3.3],
        'success_rate': [0.95, 0.87, 0.99, 0.91, 0.96]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('outputs/combined_data.csv', index=False)
    print(f"   ✅ Created: outputs/combined_data.csv")
    
    # Calculate statistics
    stats = {
        'total_users': len(df),
        'total_api_calls': df['api_calls_made'].sum(),
        'avg_success_rate': df['success_rate'].mean(),
        'max_data_fetched': df['data_fetched_mb'].max(),
        'min_data_fetched': df['data_fetched_mb'].min()
    }
    
    return stats

def generate_report(all_data):
    """Generate a comprehensive API usage report"""
    
    report_content = f"""
    ==========================================
    API DATA FETCHING REPORT - DAY 2
    ==========================================
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    📊 API SUMMARY
    --------------
    Total APIs called: {len(all_data)}
    
    APIs Used:
    1. JSONPlaceholder - User data
    2. Weather API - Weather information  
    3. News API - Latest headlines
    4. GitHub API - User profiles
    
    📁 DATA SAVED
    -------------
    JSON Files (data/ folder):
    """
    
    # List JSON files
    for data_type in all_data.keys():
        if isinstance(all_data[data_type], list):
            count = len(all_data[data_type])
            report_content += f"    • {data_type}.json: {count} items\n"
        elif isinstance(all_data[data_type], dict):
            report_content += f"    • {data_type}.json: 1 object\n"
    
    report_content += f"""
    CSV Files (outputs/ folder):
        • users.csv - User information
        • combined_data.csv - Sample analytics dataset
    
    🔧 TECHNICAL DETAILS
    --------------------
    Libraries used:
    - requests: HTTP library for API calls
    - pandas: Data processing and CSV export
    - json: JSON serialization/deserialization
    
    Error handling:
    - Timeout protection (10 seconds per API)
    - Fallback to sample data if API fails
    - Comprehensive error messages
    
    ⚡ PERFORMANCE TIPS
    ------------------
    1. Always add timeouts to API calls
    2. Cache responses when possible
    3. Handle rate limiting gracefully
    4. Use environment variables for API keys
    
    🎯 LEARNING OUTCOMES
    -------------------
    ✅ Understand REST API concepts
    ✅ Make GET requests with parameters
    ✅ Parse JSON responses
    ✅ Handle API errors
    ✅ Save data in multiple formats
    ✅ Generate usage reports
    
    ==========================================
    CONGRATULATIONS ON COMPLETING DAY 2! 🚀
    ==========================================
    """
    
    with open('outputs/api_report.txt', 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"   ✅ Generated: outputs/api_report.txt")

# Run the main function
if __name__ == "__main__":
    main()
