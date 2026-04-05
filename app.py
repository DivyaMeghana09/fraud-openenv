import gradio as gr

def health():
    return "Fraud API is running ✅"

iface = gr.Interface(fn=health, inputs=[], outputs="text")

iface.launch(server_name="0.0.0.0", server_port=7860)