import streamlit as st
from datetime import datetime
import pandas as pd
import os
import sys
import speech_recognition as sr

# ✅ FIXED: Add backend path before imports
sys.path.append(os.path.abspath(".."))

# ✅ FIXED: Now import
from backend.utils.mood_responder import get_response_by_mood, get_session_summary
from backend.utils.breakup_advice import check_breakup_keywords, get_breakup_response
from backend.utils.quote_utils import get_daily_quote, get_random_quote
from backend.utils.send_email import send_summary_email

# ✅ FIXED: Define log_file once globally
log_file = "../data/user_logs.csv"



st.set_page_config(page_title="BuddyWithin – You're Not Alone", layout="centered")

# --- State ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []
if "voice_input" not in st.session_state:
    st.session_state.voice_input = ""

# 🎤 Voice Transcription
def transcribe_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... please speak clearly.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.success("✅ Captured your voice.")
            return text
        except sr.UnknownValueError:
            st.warning("😕 Sorry, I couldn't understand.")
        except sr.RequestError:
            st.error("❌ Speech service error.")
    return ""

# --- UI Header ---
st.title("🤝 BuddyWithin")
st.subheader("Your Safe Space to Share")

# --- Motivation ---
st.markdown("#### 🌟 Today's Motivation")
st.info(get_daily_quote())

if st.button("🎈 Cheer Me Up"):
    st.success(get_random_quote())

st.markdown("---")

# --- Personality ---
st.markdown("### 👤 Choose Your Buddy's Personality")
personality = st.selectbox("Who do you want to talk to today?", ["🧘 Calm Listener", "👯‍♀️ Cheerful Bestie", "🧑‍🏫 Wise Elder"])
personality_key = {"🧘 Calm Listener": "calm", "👯‍♀️ Cheerful Bestie": "cheerful", "🧑‍🏫 Wise Elder": "wise"}[personality]

# --- Mood ---
mood = st.radio("How are you feeling today?", ["🙂 Happy", "😞 Sad", "😡 Angry", "😰 Anxious", "😶 Numb"])
mood_clean = mood.split(" ")[-1]

st.markdown("---")

# --- Chat Input ---
st.markdown("### 💬 Talk to Buddy Freely")
user_msg = st.text_input("Type anything you're feeling right now...", key="chat_input")

# 🎙 Voice Input Trigger
if st.button("🎙️ Use My Voice"):
    voice_text = transcribe_voice()
    if voice_text:
        user_msg = voice_text
        st.session_state.chat_log.append(("You", voice_text))
        st.session_state.voice_input = ""  # clear just in case

# --- Process Input ---
if user_msg:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = "../data/user_logs.csv"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    new_entry = pd.DataFrame([[timestamp, mood_clean, user_msg]], columns=["timestamp", "mood", "entry"])
    if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
        prev = pd.read_csv(log_file)
        updated = pd.concat([prev, new_entry], ignore_index=True)
    else:
        updated = new_entry
    updated.to_csv(log_file, index=False)

    if not st.session_state.chat_log or st.session_state.chat_log[-1][1] != user_msg:
        st.session_state.chat_log.append(("You", user_msg))

    reply = get_breakup_response() if check_breakup_keywords(user_msg) else get_response_by_mood(user_msg, mood_clean, personality_key)
    st.session_state.chat_log.append(("Buddy", reply))

# --- Chat Log ---
st.markdown("### 🗨️ Your Conversation")
for sender, msg in st.session_state.chat_log:
    color = "#2E7D32" if sender == "You" else "#B71C1C"
    icon = "🧍" if sender == "You" else "🤖"
    st.markdown(f"<div style='background-color:{color};padding:10px;border-radius:10px;margin-bottom:5px;color:white'><strong>{icon} {sender}:</strong> {msg}</div>", unsafe_allow_html=True)

# --- Clear Button ---
if st.button("🧹 Clear Conversation"):
    st.session_state.chat_log = []
    st.session_state.voice_input = ""

st.markdown("---")

# --- Mood History ---
st.markdown("## 📊 Mood History")
if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
    df = pd.read_csv(log_file)
    mood_scores = {"happy": 5, "anxious": 3, "numb": 2, "sad": 1, "angry": 0}
    df["mood_score"] = df["mood"].str.lower().map(mood_scores)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    st.line_chart(df.set_index("timestamp")[["mood_score"]])
    st.caption("Higher score = Happier mood 😊")
else:
    st.info("Mood graph will appear after you make some journal entries.")

# --- Session Summary ---
if st.button("🧠 Summarize My Session"):
    all_user_msgs = [msg for who, msg in st.session_state.chat_log if who == "You"]
    if len(all_user_msgs) < 2:
        st.info("Talk to me a bit more and I'll summarize your thoughts 💬")
    else:
        combined = " ".join(all_user_msgs).lower()
        summary = get_session_summary(combined)
        st.markdown("#### 🧠 Buddy's Reflection")
        st.success(summary)

# --- Weekly Reflection ---
st.markdown("## 🧠 Weekly Reflection")
if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
    df = pd.read_csv(log_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    last_7_days = df[df["timestamp"] >= pd.Timestamp.now() - pd.Timedelta(days=7)]

    if last_7_days.empty:
        st.info("Not enough data for reflection yet. Talk to me daily 💬")
    else:
        mood_scores = {"happy": 5, "anxious": 3, "numb": 2, "sad": 1, "angry": 0}
        last_7_days["mood_score"] = last_7_days["mood"].str.lower().map(mood_scores)
        avg_mood = round(last_7_days["mood_score"].mean(), 2)
        common_mood = last_7_days["mood"].value_counts().idxmax().capitalize()
        quote = get_daily_quote()

        st.success(f"🧮 Avg Mood Score: `{avg_mood}` / 5")
        st.info(f"🔁 Most frequent mood: **{common_mood}**")
        st.markdown(f"💡 *Quote of the Week:* **_{quote}_**")

# --- Email Summary ---
st.markdown("## 📬 Email My Summary")
with st.form("email_form"):
    user_email = st.text_input("Enter your email to receive your summary:")
    submit_email = st.form_submit_button("📨 Send Email")

    if submit_email:
        all_user_msgs = [msg for who, msg in st.session_state.chat_log if who == "You"]
        if len(all_user_msgs) < 2:
            st.warning("You need to chat a bit more before I can summarize.")
        elif not user_email or "@" not in user_email:
            st.warning("Please enter a valid email.")
        else:
            combined = " ".join(all_user_msgs).lower()
            summary = get_session_summary(combined)
            email_body = f"""Hi there 👋

Here’s your reflection summary from BuddyWithin 💙

🧠 Summary:
{summary}

Stay strong,
– BuddyWithin
"""
            result = send_summary_email(user_email, "🧠 Your BuddyWithin Summary", email_body)
            st.success(result)
