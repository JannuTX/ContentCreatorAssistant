Content Creator Assistant - Keeping this master until full implemetation



Overview
Content Creator Assistant is a Python-based application that integrates Zoho CRM and Hugging Face AI to streamline the content creation process. It provides a simple interface for content creators to fetch video ideas from their Zoho CRM, generate content briefs using AI, and update video statuses.
Features

Fetch next video idea from Zoho CRM
Generate content briefs using Hugging Face's GPT-2 model
Update video statuses in Zoho CRM
User-friendly Gradio web interface

Prerequisites

Python 3.7+
Zoho CRM account with API access
Hugging Face account with API access

Installation

Clone the repository:
Copygit clone https://github.com/JannuTX/ContentCreatorAssistant/edit/master
cd content-creator-assistant

Create a virtual environment (optional but recommended):
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
Copypip install gradio zcrmsdk requests python-dotenv

Set up your environment variables:
Create a .env file in the project root and add your API keys:
CopyZOHO_CLIENT_ID=your_zoho_client_id
ZOHO_CLIENT_SECRET=your_zoho_client_secret
ZOHO_ACCESS_TOKEN=your_zoho_access_token
HUGGINGFACE_API_TOKEN=your_huggingface_api_token


Project Structure





CopyContentCreatorAssistant/
│
├── src/
│   ├── __init__.py
│   ├── assistant.py
│   ├── zoho_integration.py
│   └── huggingface_integration.py
│
├── .env
├── main.py
└── README.md




Usage

Run the application:
Copypython main.py

Open the Gradio interface URL displayed in the console.
In the Gradio interface, you can use commands like:

"Get next video idea"
"Update status of video 123 to editing" (replace 123 with an actual video ID from your Zoho CRM)



Customization

Modify src/zoho_integration.py to adjust Zoho CRM module names or fields according to your CRM setup.
Update src/huggingface_integration.py to use a different AI model or customize the prompt for content brief generation.

Troubleshooting

If you encounter authentication issues with Zoho CRM, ensure your API tokens are correct and have the necessary permissions.
For Hugging Face API errors, check your API token and ensure you have access to the GPT-2 model.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Zoho CRM for providing the CRM functionality
Hugging Face for the AI model access
Gradio for the easy-to-use web interface
