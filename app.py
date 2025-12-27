import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# --- INITIALIZATION ---
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

if "verdict" not in st.session_state:
    st.session_state.verdict = None

st.set_page_config(
    page_title="Vibe Check AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LIGHT FASHION UI (SAFE) ---
st.markdown("""
<style>
.vibe-title {
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
}

.vibe-subtitle {
    text-align: center;
    opacity: 0.8;
    margin-bottom: 1rem;
}

.vibe-card {
    background-color: rgba(255,255,255,0.04);
    border-radius: 14px;
    padding: 1rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="vibe-title">👗 Vibe Check</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="vibe-subtitle">AI Stylist • Fit Judge • Fashion Advisor</div>',
    unsafe_allow_html=True
)

# --- STYLIST FUNCTION ---
def get_stylist_advice(dress_url, shoulder_hip_ratio=1.1):
    body_shape = "Inverted Triangle" if shoulder_hip_ratio > 1.05 else "Hourglass / Pear"

    prompt = f"""
You are a professional fashion designer and personal stylist.


DRESS URL:
{dress_url}

TASK:
    Analyze the dress from the URL and provide:
    1. **Fabric & Quality**: Judge the drape and material based on visuals/description.
    2. **Size-Specific Fit**: 
       - How would a **Size XS** fit this body?
       - How would a **Size S** fit this body?
       - How would a **Size M** fit?
       - How would a **Size L** fit?
       - How would a **Size XL** fit?
       - How would a **Size XXL** fit?
       formulate this in a table with columns for Size, Chest size in cm, Fit Description, and Recommendation.
    3. **Final Verdict**: Give a Fit Score (0-10) and the recommended size for the 'Perfect Vibe'.
    4. **Similar Recommendations**: Suggest 3 similar dresses that would suit this body shape.
    5. **Compare those dresses among their details and price in INR and show in a tabular format.
    

Use clean markdown formatting.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Stylist Brain Error: {e}"

# --- SIDEBAR ---
with st.sidebar:
    st.header("🧍 Your Profile")
    user_video = st.file_uploader(
        "Upload walking video",
        type=["mp4", "mov"]
    )

    st.header("👚 Dress Link")
    dress_url = st.text_input(
        "Paste product URL",
        placeholder="Amazon / Flipkart / Myntra"
    )

# --- VIDEO DISPLAY (KEY FIX HERE) ---
if user_video:
    st.markdown('<div class="vibe-card">', unsafe_allow_html=True)

    # Narrow centered column forces video to fit viewport
    left, center, right = st.columns([1.5, 1, 1.5])
    with center:
        st.video(user_video)
        st.caption("10–15 sec full-body walking video")

    st.markdown('</div>', unsafe_allow_html=True)

# --- ACTION BUTTON ---
st.markdown("<br>", unsafe_allow_html=True)
l, c, r = st.columns([1.5, 1, 1.5])

with c:
    if st.button("✨ Run Vibe Check", use_container_width=True):
        if user_video and dress_url:
            with st.spinner("Analyzing your vibe..."):
                mock_ratio = 1.15
                st.session_state.verdict = get_stylist_advice(
                    dress_url, mock_ratio
                )
        else:
            st.warning("Please upload a video and add a dress link.")

# --- VERDICT ---
if st.session_state.verdict:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="vibe-card">', unsafe_allow_html=True)
    st.subheader("✨ AI Style Verdict")
    st.markdown(st.session_state.verdict)
    st.markdown('</div>', unsafe_allow_html=True)
