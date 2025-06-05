import requests

headers = {
    "Accept": "text/event-stream",
    "Content-Type": "application/json"
}

data = {
    "jsonrpc": "2.0",
    "id": "1",
    "method": "add",
    "params": {
        "a": 3,
        "b": 5
    }
}

response = requests.post("http://localhost:8000/mcp", headers=headers, json=data)
print(response.text)
