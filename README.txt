
📦 Mandi Bhav API – Complete Setup

Files:
- mandi_api.py → Flask API
- scraper.py → Dummy data fetcher (ready for real scraping)
- requirements.txt → All required packages including gunicorn
- render_start.txt → Shows gunicorn start command for Render
- README.txt → This help file

Run locally:
1. pip install -r requirements.txt
2. python mandi_api.py
3. Open http://127.0.0.1:5000/mandi?state=Madhya%20Pradesh&district=Chhindwara

Deploy on Render:
1. Push to GitHub
2. Create Web Service on Render.com
3. Set start command as: gunicorn mandi_api:app
