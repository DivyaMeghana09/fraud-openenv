import gradio as gr

def health():
    return "Fraud API is running ✅"

iface = gr.Interface(fn=health, inputs=[], outputs="text")

iface.launch()