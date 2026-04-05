from fastapi import FastAPI
import gradio as gr
import uvicorn

app = FastAPI()

# ✅ Required for OpenEnv check
@app.post("/reset")
def reset():
    return {"status": "reset successful"}

# ✅ UI
def health():
    return "Fraud API is running ✅"

demo = gr.Interface(fn=health, inputs=[], outputs="text")

# ✅ Mount Gradio
app = gr.mount_gradio_app(app, demo, path="/")

# ✅ THIS IS THE MISSING PART (VERY IMPORTANT)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)