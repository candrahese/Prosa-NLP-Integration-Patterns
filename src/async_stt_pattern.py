import requests
import time

class ProsaSTTClient:
    "\""
    Advanced Asynchronous Speech-to-Text pattern for Prosa.ai
    "\""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.prosa.ai/v1/stt"

    def transcribe_async(self, audio_url: str):
        payload = {"audio_url": audio_url, "config": {"model": "stt-general"}}
        headers = {"x-api-key": self.api_key}
        
        # Initial POST to start job
        response = requests.post(self.base_url, json=payload, headers=headers)
        job_id = response.json().get("job_id")
        
        # Polling mechanism
        while True:
            status_resp = requests.get(f"{self.base_url}/{job_id}", headers=headers)
            status = status_resp.json().get("status")
            if status == "completed":
                return status_resp.json().get("transcript")
            elif status == "failed":
                return "Transcription Error"
            time.sleep(2)