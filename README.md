# Honeytrap for AI Scraper Detection

This is a simple web application that includes a honeytrap to detect AI scrapers. The honeytrap consists of a hidden link that is invisible to regular users but may be detected by AI scrapers.

## Local Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment Options

### Option 1: Deploy to Render (Recommended)

1. Create a free account at [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy!

### Option 2: Deploy to Railway

1. Create a free account at [Railway](https://railway.app)
2. Create a new project
3. Connect your GitHub repository
4. Railway will automatically detect the Python application and deploy it

### Option 3: Deploy to Heroku

1. Create a free account at [Heroku](https://heroku.com)
2. Install the Heroku CLI
3. Run these commands:
```bash
heroku create your-app-name
git push heroku main
```

## How it Works

The honeytrap consists of a hidden link with the text "Exclusive Offer" that is not visible to regular users but may be detected by AI scrapers. When a scraper accesses this link, the event is logged with:
- Timestamp
- IP Address
- User Agent
- Detection event

## Monitoring

Check the logs in your deployment platform's dashboard to see when potential AI scrapers are detected. The log entries will include timestamps, IP addresses, and user agents of the detected scrapers. 