import os
from zcrmsdk import ZCRMRestClient, ZCRMRecord, ZCRMException
import logging

logger = logging.getLogger(__name__)

class ZohoIntegration:
    def __init__(self):
        self.config = {
            "client_id": os.getenv("ZOHO_CLIENT_ID"),
            "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
            "redirect_uri": "http://localhost:8000/callback",
            "access_token": os.getenv("ZOHO_ACCESS_TOKEN")
        }
        self.initialize_zoho_crm()

    def initialize_zoho_crm(self):
        try:
            ZCRMRestClient.initialize(self.config)
            logger.info("Zoho CRM initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Zoho CRM: {str(e)}")
            raise

    def get_next_video_idea(self):
        try:
            module_ins = ZCRMRestClient.get_instance().get_module_instance('Video_Ideas')
            resp = module_ins.get_records()
            if resp.data:
                idea = resp.data[0].get_field_value('Name')  # Assuming 'Name' field contains the idea
                return idea
            else:
                return "No video ideas found in Zoho CRM"
        except ZCRMException as e:
            logger.error(f"Error fetching video idea from Zoho CRM: {str(e)}")
            raise

    def update_video_status(self, video_id, status):
        try:
            record = ZCRMRecord.get_instance('Videos', video_id)
            record.set_field_value('Status', status)
            resp = record.update()
            return f"Updated status of video {video_id} to {status}"
        except ZCRMException as e:
            logger.error(f"Error updating video status in Zoho CRM: {str(e)}")
            raise