import requests
import json
import sys

# Configuration
BASE_URL = "http://localhost:5000"
ENDPOINT = f"{BASE_URL}/ask"

def test_api():
    print(f"Testing API at {ENDPOINT}...")
    
    payload = {
        "context": "The quick brown fox jumps over the lazy dog.",
        "question": "What does the fox jump over?"
    }
    
    try:
        response = requests.post(ENDPOINT, json=payload)
        response.raise_for_status()
        
        data = response.json()
        print("Status Code: 200 OK")
        print("Response:", json.dumps(data, indent=2))
        
        # Basic validation
        if "answer" in data and "confidence_score" in data:
            print("✅ Test Passed: Valid response structure.")
        else:
            print("❌ Test Failed: Invalid response structure.")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection Error: Is the server running at {BASE_URL}?")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_api()
