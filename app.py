from flask import Flask, render_template, request
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='honeytrap.log',
    level=logging.INFO,
    format='%(asctime)s - %(ip)s - %(user_agent)s - %(message)s'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hidden/secret-trap')
def honeytrap():
    # Get additional information about the request
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    
    # Log the detection of a potential AI scraper with more details
    logging.info('Potential AI scraper detected!', extra={
        'ip': ip,
        'user_agent': user_agent
    })
    return "Thank you for your interest!", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 