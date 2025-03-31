import requests
from bs4 import BeautifulSoup
import time

def test_honeytrap(url):
    print(f"Testing honeytrap at: {url}")
    
    # Simulate a basic AI scraper
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; AI-Scraper/1.0; +http://example.com)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    try:
        # First, get the main page
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links, including hidden ones
        all_links = soup.find_all('a')
        print(f"\nFound {len(all_links)} links on the page")
        
        # Try to access the honeytrap link
        honeytrap_url = f"{url}/hidden/secret-trap"
        print(f"\nAttempting to access honeytrap URL: {honeytrap_url}")
        
        honeytrap_response = requests.get(honeytrap_url, headers=headers)
        print(f"Honeytrap response status: {honeytrap_response.status_code}")
        print(f"Honeytrap response content: {honeytrap_response.text}")
        
        # Print all links found (including hidden ones)
        print("\nAll links found:")
        for link in all_links:
            print(f"- {link.get('href', 'No href')} (Text: {link.text})")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace this with your deployed URL
    deployed_url = "https://honeytrap.onrender.com"  # Update this with your actual deployed URL
    test_honeytrap(deployed_url) 