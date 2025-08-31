import json
import os
import requests

def check_endpoint_status():
    """Check the current status of the SHMT endpoint"""
    endpoint_id = os.getenv("RUNPOD_ENDPOINT_ID", "YOUR_ENDPOINT_ID_HERE")
    api_key = os.getenv("RUNPOD_API_KEY", "YOUR_RUNPOD_API_KEY_HERE")
    url = f"https://api.runpod.ai/v2/{endpoint_id}/status"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("📋 Endpoint Status:")
            print(json.dumps(result, indent=2))
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

def test_simple_request():
    """Test a simple request to see if the endpoint is working"""
    endpoint_id = os.getenv("RUNPOD_ENDPOINT_ID", "YOUR_ENDPOINT_ID_HERE")
    api_key = os.getenv("RUNPOD_API_KEY", "YOUR_RUNPOD_API_KEY_HERE")
    url = f"https://api.runpod.ai/v2/{endpoint_id}/runsync"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Simple test payload
    payload = {
        "input": {
            "source_url": "https://example.com/test.jpg",
            "reference_url": "https://example.com/test2.jpg"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"Test Status Code: {response.status_code}")
        print(f"Test Response: {response.text}")
        
    except Exception as e:
        print(f"❌ Test Exception: {e}")

if __name__ == "__main__":
    print("🔍 Checking endpoint status...")
    check_endpoint_status()
    
    print("\n🧪 Testing simple request...")
    test_simple_request()
