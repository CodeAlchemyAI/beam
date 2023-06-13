
import requests
import json

url = "https://apps.beam.cloud/cfut1"
payload = {"query": "Hello what is your name?"}
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic YOUR_API_KEY",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

response = requests.request("POST", url,
                            headers=headers,
                            data=json.dumps(payload)
                            )

print(response.content)
