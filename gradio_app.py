import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/predict"
API_KEY = "f7d3243e-b3ef-472f-9e47-28cd640f5f89"

def classify_email(email):
    response = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        },
        json={"email": email}
    )
    if response.status_code == 200:
        result = response.json()
        return f"Prediction: {result['prediction']} (Confidence: {result['confidence']})"
    else:
        return f"❌ Error: {response.status_code} - {response.json()['detail']}"

demo = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(lines=7, placeholder="Paste your email content here..."),
    outputs="text",
    title="Spam Email Detector 🚫📧",
    description="Paste your email below to check if it's spam. Powered by FastAPI and ML 💡"
)

demo.launch()
