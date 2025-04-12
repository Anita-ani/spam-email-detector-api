# spam-email-detector-api

# 🚫📧 Spam Email Detector API

An intelligent machine learning API that classifies emails as **Spam** or **Not Spam**, with confidence scores and secure access.

Built with **FastAPI**, **scikit-learn**, and **Joblib**, this API includes:
- 🔐 API key authentication
- 📈 ML-based spam detection (Logistic Regression)
- 📝 Logging for audit trails
- ⚡ Fast, lightweight, and easy to deploy



🚀 Getting Started

 1. Clone the repository


git clone https://github.com/Anita-ani/spam-email-detector-api.git
cd spam-email-detector-api

 Install dependencies
pip install -r requirements.txt

 Run the API locally
uvicorn app.main:app --reload

🔐 Authentication
This API uses an API key for access.
API_KEY=your_secret_api_key
Or use the hardcoded key for quick testing:
API_KEY = "your_secret_api_key"


📂 Project Structure

spam-email-detector-api/
│
├── app/
│   └── main.py                 # FastAPI backend
├── spam_model_pipeline.joblib # Trained ML model
├── .env                       # API key (excluded from Git)
├── api.log                    # Logs of requests and responses
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation


🛡️ Security & Logging
API key is required for access

All prediction requests and results are logged to api.log

🔒 Rate limiting & IP blacklisting can be added for production

💡 Built By
Anita Ani
Cybersecurity | DevSecOps | Cloud Security | Network Security Engineer


📢 License
MIT — Free to use, customize, and share. Just give credit where due!


📌 What’s Next?

You can now:

✅ Create the `README.md` file in VS Code  
✅ Paste this content  
✅ Save and commit:

git add README.md
git commit -m "Add project README"
git push
