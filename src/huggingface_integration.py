import os
import requests
import logging

logger = logging.getLogger(__name__)

class HuggingFaceIntegration:
    def __init__(self):
        self.api_token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.api_url = "https://api-inference.huggingface.co/models/gpt2"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def query_huggingface(self, payload):
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error querying Hugging Face API: {str(e)}")
            raise

    def generate_content_brief(self, idea):
        payload = {"inputs": f"Generate a brief outline for a video on: {idea}"}
        try:
            response = self.query_huggingface(payload)
            return response[0]['generated_text']
        except Exception as e:
            logger.error(f"Error generating content brief: {str(e)}")
            raise