import json
import os
import requests

def check_runpod_logs(request_id):
    """Check logs for a specific RunPod request"""
    endpoint_id = os.getenv("RUNPOD_ENDPOINT_ID", "YOUR_ENDPOINT_ID_HERE")
    api_key = os.getenv("RUNPOD_API_KEY", "YOUR_RUNPOD_API_KEY_HERE")
    url = f"https://api.runpod.ai/v2/{endpoint_id}/status"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "id": request_id
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("📋 Request Status:")
            print(json.dumps(result, indent=2))
            
            # Check for error details
            if 'error' in result:
                print(f"\n❌ Error: {result['error']}")
            
            # Check for logs
            if 'logs' in result:
                print(f"\n📝 Logs:")
                for log in result['logs']:
                    print(f"  {log}")
                    
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    request_id = "sync-d02e35a8-b917-4bfd-99e3-27a0ec51f99b-e1"
    print(f"🔍 Checking logs for request: {request_id}")
    check_runpod_logs(request_id)
