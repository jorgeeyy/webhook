import requests
import json

# webhook_url = "your-webhook-url"
webhook_url = "http://127.0.0.1:5000/webhook"

data = {
    "name": "Jorgeeyy",
    "msg": "testing"
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})