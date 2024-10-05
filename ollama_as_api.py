# Using ollama with an api

import requests
import json

endpoint = "http://localhost:11434/api/generate"

payload = json.dumps({"model":"gemma:2b", "prompt":"What is the temperature of the sun?", "stream":False})

response = requests.post(url=endpoint, data=payload)
# what are we doing here?
response = response.json()

print(response["response"])