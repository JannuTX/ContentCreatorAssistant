from .zoho_integration import ZohoIntegration
from .huggingface_integration import HuggingFaceIntegration
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContentCreatorAssistant:
    def __init__(self):
        self.zoho = ZohoIntegration()
        self.huggingface = HuggingFaceIntegration()

    def process_command(self, command):
        try:
            if "next video idea" in command.lower():
                idea = self.zoho.get_next_video_idea()
                brief = self.huggingface.generate_content_brief(idea)
                return f"Next video idea: {idea}\n\nBrief:\n{brief}"
            elif "update status" in command.lower():
                parts = command.split()
                video_id = parts[parts.index("video") + 1]
                status = parts[parts.index("to") + 1]
                return self.zoho.update_video_status(video_id, status)
            else:
                return "I didn't understand that command. Try asking for the next video idea or updating a video status."
        except Exception as e:
            logger.error(f"Error processing command: {str(e)}")
            return f"An error occurred: {str(e)}"