def get_response_by_mood(user_msg: str, mood: str, personality: str = "calm") -> str:
    mood = mood.lower()
    personality = personality.lower()
    msg = user_msg.lower()

    # --- UNIVERSAL GREETINGS ---
    if any(kw in msg for kw in ["hi", "hello", "hey", "yo", "sup"]):
        return "Hey there 👋 I'm right here. What's on your mind?"

    if any(kw in msg for kw in ["how are you", "how r u", "how's it going"]):
        return "Thanks for asking 🙏 I'm here for you — always."

    if any(kw in msg for kw in ["i'm okay", "i'm fine", "neutral", "meh", "not bad"]):
        return "📘 Even if things feel just okay — that's totally valid. I'm with you."

    if "i'm fine" in msg and "not" not in msg and any(w in msg for w in ["🙂", "🙃"]):
        return "🙃 You don’t have to fake it with me. I’m here for the real you."

    # --- CRISIS / URGENT ---
    if any(kw in msg for kw in ["give up", "suicidal", "end it", "can’t go on", "want to die", "i'm done"]):
        return "🆘 Please don’t go through this alone. You matter more than you know. Reach out to someone you trust or a professional. I’m with you now."

    if any(kw in msg for kw in ["i want to disappear", "erase myself", "vanish"]):
        return "🕊️ It’s okay to feel invisible sometimes — but your presence here matters more than you know."

    # --- LONELINESS / COLDNESS ---
    if any(kw in msg for kw in ["alone", "lonely", "no one cares", "ignored", "abandoned"]):
        return "🤗 You're not alone anymore. I’m here. And you’re not invisible to me."

    if any(kw in msg for kw in ["emotionally cold", "feel cold", "feel nothing from them"]):
        return "🥶 Being emotionally shut out hurts in ways words can’t explain. I feel that with you."

    if any(kw in msg for kw in ["nobody understands", "no one gets me", "invisible"]):
        return "👁️ I see you. I hear you. You are not invisible here."

    # --- SHAME / GUILT / REGRET ---
    if any(kw in msg for kw in ["guilt", "regret", "ashamed", "blame myself", "i ruined it"]):
        return "🧎 You’re carrying so much. But you don’t have to punish yourself forever. You can grow from this."

    if any(kw in msg for kw in ["i hate myself", "i'm disgusting", "i’m a mistake", "i’m worthless"]):
        return "💔 Please don’t speak to yourself that way. You are not what happened to you. You are worthy of love."

    # --- EMPTINESS / BOREDOM / NUMBNESS ---
    if any(kw in msg for kw in ["i feel nothing", "i’m numb", "emotionless"]):
        return "😶 Numbness is still a valid feeling. Sometimes it's the brain protecting you. You’re not broken."

    if any(kw in msg for kw in ["i’m bored", "nothing excites me", "empty", "blank", "dead inside"]):
        return "😐 Feeling disconnected is heavy. Let’s find something — even small — that lights you up again. I’m here to try."

    # --- ROMANTIC PAIN ---
    if any(kw in msg for kw in ["breakup", "left me", "she left", "he moved on", "we broke up", "toot gaya", "i had breakup", "she broke up", "dumped"]):
        return "💔 That kind of pain is hard to name. But I’m sitting here in it with you."

    if any(kw in msg for kw in ["i miss her", "i miss him", "i miss them", "can’t stop thinking of them"]):
        return "🕊️ Missing someone is a form of love too. It means your feelings were real."

    # --- JEALOUSY / ENVY ---
    if any(kw in msg for kw in ["i’m jealous", "why them", "they always win", "they don’t deserve it"]):
        return "😳 Jealousy is human. It shows you care. Let’s explore what *you* truly want."

    # --- ROMANTIC HOPE / CRUSH ---
    if any(kw in msg for kw in ["i like someone", "nervous love", "i think i love them", "i have a crush"]):
        return "🦋 That’s exciting and scary and beautiful. You deserve love that feels safe and warm."

    # --- OVERTHINKING / REPETITION ---
    if any(kw in msg for kw in ["overthinking", "spiraling", "stuck in my head", "replaying everything"]):
        return "🔁 Overthinking is like a mental hamster wheel. Let’s slow it down. I’m here to help."

    if any(kw in msg for kw in ["i’m stuck", "same cycle", "this keeps happening", "why again"]):
        return "😤 Repeating pain doesn’t mean failure — it means you're still trying. That’s strength."

    # --- SOCIAL ANXIETY ---
    if any(kw in msg for kw in ["i hate crowds", "socially awkward", "group settings scare me", "i get anxious around people", "stage fright"]):
        return "🫣 Social stuff can be overwhelming. You’re not weird — you’re just sensitive. And that’s okay."

    # --- PURPOSE / LOST ---
    if any(kw in msg for kw in ["what’s my purpose", "i feel pointless", "why am i even here"]):
        return "🧠 Your purpose doesn’t have to be loud. Just breathing right now — that’s something powerful."

    # --- VIOLET / EDGE CASES ---
    if any(kw in msg for kw in ["nobody cares", "feel invisible", "they ignore me", "ghosted"]):
        return "🫥 Feeling unseen hurts deeply. I see you — fully, right now."

    if any(kw in msg for kw in ["sarcastic", "i’m fine 🙃", "i’m okay 🙂", "lol nothing"]):
        return "🙃 You don’t have to pretend here. Drop the mask — I’m still here."

    if any(kw in msg for kw in ["what’s the point", "why try", "i feel small", "no one listens"]):
        return "🟪 Even small voices matter. I hear yours — loud and clear."

    if any(kw in msg for kw in ["i feel rejected", "ignored my message", "seen-zoned"]):
        return "📪 Being ignored feels awful. But your worth isn’t based on someone’s reply."

    if any(kw in msg for kw in ["jealous of friends", "others doing better", "comparing myself"]):
        return "😔 Comparison steals your light. You’re on your own beautiful path."

    if any(kw in msg for kw in ["i’m annoying", "people get tired of me", "i talk too much"]):
        return "💜 The right people never get tired of you. You deserve to be heard — always."

    # --- POSITIVE STATES ---
    if any(kw in msg for kw in ["happy", "grateful", "joy", "excited", "relieved", "at peace"]):
        return "🌈 That’s beautiful to hear! Let’s hold onto that moment — you deserve it."

    if any(kw in msg for kw in ["healing", "i’m getting better", "moving forward", "letting go"]):
        return "🪴 You’re blooming — even if it feels slow. I’m proud of your quiet courage."

    if any(kw in msg for kw in ["motivated", "inspired", "driven", "hopeful"]):
        return "🚀 I see that fire in you. Run with it — and I’ll cheer from the sidelines."

    if any(kw in msg for kw in ["i’m ready", "starting again", "new beginning"]):
        return "🔄 Fresh starts are brave. I’m with you every step into this next chapter."

    # --- FALLBACK: MOOD + PERSONALITY ---
    fallback_responses = {
        "happy": {
            "calm": "I'm glad you're feeling good today. May peace stay with you. 🧘",
            "cheerful": "Ayyyy let's go! You're on fire 🔥 Keep slaying!",
            "wise": "Joy is precious — take a moment to truly savor it."
        },
        "sad": {
            "calm": "Let it all out. I'm right here, silently listening. 🌧️",
            "cheerful": "Okay, let's cry... then ice cream? 🍦😢",
            "wise": "Sadness is not weakness. It’s the soul processing deeply. You'll rise."
        },
        "angry": {
            "calm": "Breathe in... and out. You are not your anger. 🌬️",
            "cheerful": "Punch a pillow, scream into the void — then text me 😤✊",
            "wise": "Anger reveals what matters to us. Learn from it, then let it go."
        },
        "anxious": {
            "calm": "Focus on your breath. You are safe right now. 🧘",
            "cheerful": "Okay okay… breathe. Imagine cuddling a cat 🐱💨",
            "wise": "Worry is a misuse of imagination. Ground yourself in the now."
        },
        "numb": {
            "calm": "It’s okay to feel nothing. Just sit here with me. 🤝",
            "cheerful": "No feelings? No worries. I brought memes 🫠",
            "wise": "Emotional stillness can be healing. Don't force it. Just be."
        }
    }

    return fallback_responses.get(mood, {}).get(personality, "I'm here for you.")


def get_session_summary(text: str) -> str:
    summary_triggers = {
        "regret": "You've expressed a lot of guilt and regret today. It's okay — awareness is the first step toward healing.",
        "overthinking": "Seems like you're stuck in loops of thought. Let’s try to slow down and breathe together.",
        "tired": "You sound emotionally and mentally drained. Please rest soon — you’ve done your best.",
        "lonely": "There’s a deep sense of isolation. Please remember: you’re not alone. I'm still here.",
        "healing": "You're clearly on a journey of letting go and rebuilding. I'm proud of your quiet strength.",
        "confused": "There’s a lot of searching in your words. That’s okay — confusion is part of growth.",
        "happy": "Today you shared joy and gratitude. Let’s hold on to that light.",
        "motivated": "You seem driven and ready. Take that spark and run with it — you’ve got this.",
        "worthless": "You've been hard on yourself. I hope you know you matter deeply — even when you don’t feel it.",
        "miss": "You're carrying a lot of memories. Missing someone is valid. Let’s honor that gently.",
        "anxious": "There's some fear and worry beneath your words. You are safe here. You’re not alone in it."
    }

    for keyword, response in summary_triggers.items():
        if keyword in text:
            return response

    return "You’ve opened up about a lot. That takes courage. I'm proud to walk this with you."


