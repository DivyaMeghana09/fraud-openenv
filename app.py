import gradio as gr

def health():
    return "Fraud API is running ✅"

def reset():
    return "reset successful"

with gr.Blocks() as demo:
    gr.Markdown("# Fraud API is running ✅")
    btn = gr.Button("Check")
    output = gr.Textbox()
    
    btn.click(fn=health, inputs=[], outputs=output)

# ✅ THIS LINE IS CRITICAL
demo.queue()

# ✅ THIS LINE IS CRITICAL
demo.launch(server_name="0.0.0.0", server_port=7860)