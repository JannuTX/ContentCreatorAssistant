import gradio as gr
from src.assistant import ContentCreatorAssistant

def main():
    assistant = ContentCreatorAssistant()

    def gradio_interface(command):
        return assistant.process_command(command)

    iface = gr.Interface(
        fn=gradio_interface,
        inputs=gr.Textbox(lines=2, placeholder="Enter your command here..."),
        outputs="text",
        title="Content Creator Assistant",
        description="Ask for the next video idea or update a video status. Try commands like 'Get next video idea' or 'Update status of video 123 to editing'."
    )

    iface.launch()

if __name__ == "__main__":
    main()