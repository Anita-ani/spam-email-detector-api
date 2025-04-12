from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import joblib
import os
from dotenv import load_dotenv  # ✅ dotenv for loading API key
import logging

# Setup logging
logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ✅ Load environment variables
load_dotenv()

# ✅ Read the API key after loading .env
API_KEY = ""
print(f"Loaded API_KEY: {API_KEY}")  # ✅ Debug print AFTER assignment
# ✅ Load the model using absolute path
model_path = os.path.join(os.path.dirname(__file__), "spam_model_pipeline.joblib")
model = joblib.load(model_path)

# 🎨 Brand your API
app = FastAPI(
    title="Spam Email Detector API 🚫📧",
    description="""
An intelligent spam and phishing email detection API.

⚡ Paste email text, get a spam prediction in seconds.
🔐 Built for security-conscious users, businesses, and developers.
""",
    version="1.0.0"
)

# 📨 Schema for email input
class EmailRequest(BaseModel):
    email: str

# ✅ Root route
@app.get("/")
def root():
    return {"message": "Welcome to the Spam Email Detector API!"}

# 🔍 Prediction route with confidence score and API key check
@app.post("/predict")
def predict(request: EmailRequest, x_api_key: str = Header(..., alias="x-api-key")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    prediction = model.predict([request.email])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    probabilities = model.predict_proba([request.email])[0]
    confidence = max(probabilities)

    return {
        "prediction": result,
        "confidence": f"{round(confidence * 100, 2)}%"
    }
