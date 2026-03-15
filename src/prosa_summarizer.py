import requests
import json

class ProsaSummarizer:
    "\""
    Integration pattern for Prosa.ai NLP Text Summarization.
    "\""
    def __init__(self, api_key: str):
        self.endpoint = "https://api.prosa.ai/v1/summarization"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def summarize(self, text: str) -> str:
        payload = {"text": text}
        response = requests.post(self.endpoint, headers=self.headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            return response.json().get("summary", "")
        else:
            raise Exception(f"Prosa API Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    summarizer = ProsaSummarizer("MOCK_API_KEY")
    # print(summarizer.summarize("Long text goes here..."))