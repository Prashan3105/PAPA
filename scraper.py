
import requests
from bs4 import BeautifulSoup

def get_mandi_data(state=None, district=None):
    # Dummy data — replace with actual scraping logic
    return {
        "state": state,
        "district": district,
        "date": "18-06-2025",
        "crops": [
            {"crop": "गेहूं", "rate": "₹2200/क्विंटल"},
            {"crop": "चना", "rate": "₹4800/क्विंटल"},
        ]
    }
