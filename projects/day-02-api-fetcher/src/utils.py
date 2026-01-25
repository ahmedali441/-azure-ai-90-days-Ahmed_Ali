"""
Utility functions for API operations
"""

import requests
import json
from datetime import datetime

def make_api_request(url, params=None, headers=None, timeout=10):
    """
    Make a safe API request with error handling
    
    Args:
        url: API endpoint URL
        params: Query parameters (dict)
        headers: Request headers (dict)
        timeout: Request timeout in seconds
    
    Returns:
        Response data or None if error
    """
    try:
        response = requests.get(
            url, 
            params=params, 
            headers=headers, 
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Timeout error for {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"API error for {url}: {e}")
        return None

def save_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filename}")

def load_json(filename):
    """Load data from JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

def format_api_response(data, max_items=5):
    """Format API response for display"""
    if isinstance(data, list):
        return f"List with {len(data)} items. First {min(max_items, len(data))} items shown."
    elif isinstance(data, dict):
        return f"Dictionary with {len(data)} keys: {', '.join(list(data.keys())[:max_items])}..."
    else:
        return str(type(data))
