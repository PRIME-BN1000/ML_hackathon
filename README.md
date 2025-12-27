👗 Vibe Check AI
AI Stylist • Fit Judge • Fashion Advisor

Vibe Check AI is a Streamlit-based fashion assistant that analyzes a user’s movement video and a product link to provide AI-powered outfit fit advice, size recommendations, and styling insights using Google Gemini.

✨ Features
🎥 Upload a full-body walking video
👚 Paste a dress/product link (Amazon, Flipkart, Myntra, etc.)
🤖 AI stylist analyzes:
Fabric & quality
Size-wise fit (XS–XXL)
Best size recommendation
Fit score (0–10)
Similar dress suggestions
Price comparison in INR
🎨 Clean fashion-app themed UI
📱 Fully responsive (mobile & desktop)
💾 Results stay visible using Streamlit session state

📂 Project Structure
Vibe-Check-AI/
│
├── app.py              # Main Streamlit application
├── .env                # API keys (not committed)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

1️⃣ Clone the repository
git clone https://github.com/PRIME-BN1000/ML_hackathon

2️⃣ Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up environment variables
Create a .env file:

GEMINI_API_KEY=your_google_gemini_api_key_here

▶️ Run the App
streamlit run app.py
