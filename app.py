import streamlit as st
import os
import time
from google import genai
from dotenv import load_dotenv

# --- INITIALIZATION ---
load_dotenv()
# Initialize the modern Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Ensure the verdict stays on screen using Session State
if 'verdict' not in st.session_state:
    st.session_state.verdict = None

st.set_page_config(page_title="Vibe Check AI", layout="wide")
st.title("👗 Vibe Check: AI Stylist & Fit Judge")

# --- FUNCTIONS ---

def get_stylist_advice(dress_url, shoulder_hip_ratio=1.1):
    """Calls Gemini to act as a fashion designer/stylist."""
    
    # We pass the calculated ratio to the prompt
    body_shape = "Inverted Triangle" if shoulder_hip_ratio > 1.05 else "Hourglass/Pear"
    
    prompt = f"""
    You are a professional fashion designer and personal stylist.
    
    USER PROFILE:
    - Body Shape: {body_shape}
    - Measured Shoulder-to-Hip Ratio: {shoulder_hip_ratio}
    
    DRESS URL: {dress_url}
    
    TASK:
    Analyze the dress from the URL and provide:
    1. **Fabric & Quality**: Judge the drape and material based on visuals/description.
    2. **Size-Specific Fit**: 
       - How would a **Size S** fit this body?
       - How would a **Size M** fit?
       - How would a **Size L** fit?
       formulate this in a table with columns for Size, Chest size in cm, Fit Description, and Recommendation.
    3. **Final Verdict**: Give a Fit Score (0-10) and the recommended size for the 'Perfect Vibe'.
    4. **Similar Recommendations**: Suggest 3 similar dresses that would suit this body shape.
    5. **Compare those dresses among their details and price in INR and show in a tabular format.
    
    Format the output beautifully with bold headers, a table for sizes, and a bulleted list for similar products.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error connecting to Stylist Brain: {e}"

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("Step 1: Your Profile")
    user_video = st.file_uploader("Upload Walking Video", type=["mp4", "mov"])
    
    st.header("Step 2: The Dress")
    dress_url = st.text_input("Paste Dress URL (Flipkart, Amazon, Myntra etc.)")

# --- MAIN PAGE LOGIC ---
col1, col2 = st.columns([1, 1])

with col1:
    if user_video:
        st.video(user_video)
        st.caption("Your Uploaded Movement Reference")

with col2:
    if st.button("Run Vibe Check"):
        if user_video and dress_url:
            with st.spinner("👗 Stylist is analyzing fit..."):
                # 1. Simulate Body Analysis (Replace with your MediaPipe logic)
                mock_ratio = 1.15 
                
                # 2. Get the AI Verdict
                st.session_state.verdict = get_stylist_advice(dress_url, mock_ratio)
                
                # 3. Handle Video Generation (Mock path for now)
                # In a real run, this would save 'vibe_check_output.mp4'
        else:
            st.warning("Please provide both a video and a dress link.")

    # --- PERSISTENT DISPLAY ---
    if st.session_state.verdict:
        st.markdown("---")
        st.markdown(st.session_state.verdict)