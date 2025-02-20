import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Growth Mindset Project",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Title (kept from your original)
st.title("Growth Mindset Challenge")

# Welcome Section
st.header("🎉 Begin Your Growth Journey")
st.write("""
    Welcome to an empowering experience designed to help you embrace challenges, 
    learn from setbacks, and realize your full potential. This application provides 
    a structured platform to support your personal and professional development.
""")

# Quote Section
st.header("💫 Daily Inspiration")
quote = "Success is not final; failure is not fatal: It is the courage to continue that counts."
st.markdown(f"> {quote}  \n> *— Winston Churchill*")

# Challenge Section
st.header("⚙️ Identify Your Current Challenge")
user_input = st.text_input(
    "Please describe a challenge you are currently addressing:",
    placeholder="Enter your challenge here"
)

if user_input:
    st.success(
        f"Your current challenge: '{user_input}'. Stay focused and proactive in pursuing your goals."
    )
else:
    st.warning("Please enter a challenge to begin your progress tracking.")

# Reflection Section
st.header("🧠 Reflect on Your Insights")
reflection = st.text_area(
    "Document your reflections on recent experiences:",
    placeholder="What insights have you gained from your journey?",
    height=150
)

if reflection:
    st.success(f"Valuable insight recorded: '{reflection}'")
else:
    st.info("Reflection is a key step in personal growth. Please share your thoughts.")

# Achievements Section
st.header("🏆 Recognize Your Achievements")
achievement = st.text_input(
    "Share a recent accomplishment:",
    placeholder="Highlight a success you’re proud of"
)

if achievement:
    st.success(f"Congratulations on your accomplishment: '{achievement}'")
else:
    st.info("Acknowledging achievements, no matter the scale, fosters motivation. Share one today.")

# Sidebar
with st.sidebar:
    st.header("Application Overview")
    st.write("""
        This tool enables you to:
        - Monitor your challenges
        - Document reflective insights
        - Celebrate your accomplishments
    """)
    st.write("Developed by Ahmed Zai")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        Continue to believe in your potential. Growth is a continuous process, not a final endpoint.
        <br>
        <strong>Developed by Ahmed Zai</strong>
    </div>
""", unsafe_allow_html=True)

# Add some styling
st.markdown("""
    <style>
        .stApp {
            max-width: 1300px;
            margin: 0 auto;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
        }
        .stTextArea > div > div > textarea {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)
