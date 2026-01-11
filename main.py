import requests
import json

# webhook_url = "https://webhook.site/8a64fb24-3ff4-47b1-9394-be3df1e0eee2"
webhook_url = "http://127.0.0.1:5000/webhook"

data = {
    "name": "Jorgeeyy",
    "msg": "testing"
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})