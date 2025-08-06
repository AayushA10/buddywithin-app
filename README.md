# 🤝 BuddyWithin – Your Safe Space to Feel

**BuddyWithin** is an AI-powered emotional journaling app that listens to your thoughts, supports your feelings, and helps you grow — one conversation at a time.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20with-💙%20Streamlit%20%7C%20Python-blue" />
  <img src="https://img.shields.io/badge/Mood%20Detection-🎭%20NLP%20Rules-brightgreen" />
  <img src="https://img.shields.io/badge/Voice%20Input-🎙️%20Enabled-orange" />
</div>

---

## 🌟 Features

### 💬 Real-Time Emotional Chat Loop
Talk to your AI buddy freely. It detects:
- Breakup pain 💔
- Loneliness 🥺
- Anxiety 😰
- Social fear 🫣
- Romantic hope 🦋
- And 75+ emotional states

### 🧘 Choose Your Buddy Personality
Pick a tone that suits your vibe:
- Calm Listener 🧘
- Cheerful Bestie 👯‍♀️
- Wise Elder 🧑‍🏫

### 🎙️ Voice-to-Text Journaling
Too tired to type? Just speak. It listens and responds with care.

### 📊 Mood History Tracker
Visualize how you’ve been feeling over time with:
- Mood score chart
- Color-coded states

### 🧠 Weekly Reflection Mode
Shows your:
- Avg mood of the week
- Most frequent emotion
- Motivational quote of the week

### 📬 Email My Summary
Send your emotional summary directly to your inbox securely.

---

## 🚀 Run Locally

1. **Clone the repo**  
#bash
git clone https://github.com/AayushA10/buddywithin-app.git
cd buddywithin-app

Install requirements
pip install -r requirements.txt

Add your .env file
Create a .env with:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

Run the app
cd frontend
streamlit run app.py

📁 Project Structure
buddywithin_app/
├── backend/
│   └── utils/
│       ├── mood_responder.py
│       ├── quote_utils.py
│       ├── send_email.py
│       └── breakup_advice.py
├── data/
│   └── user_logs.csv
├── frontend/
│   └── app.py
├── .env
├── requirements.txt
└── README.md

❤️ Why I Built This
To remind people that it’s okay to not be okay — and even when you're alone, you're not truly alone.

⭐ Coming Soon
GPT-powered response generation (optional)
Spotify playlist recommender based on mood
Mobile app version

🤝 Let's Talk
If this resonates with you, star 🌟 the repo, contribute, or just say hi!
Built with 💙 by Aayush Anand @ NYU
