# backend/utils/breakup_advice.py

def check_breakup_keywords(text: str) -> bool:
    text = text.lower()
    breakup_keywords = [
        "break up", "breakup", "broke up", "ended relationship", 
        "split up", "left me", "he left", "she left", "dumped", 
        "heartbreak", "heart broke", "relationship ended", "i had breakup",
        "mera breakup", "brekup", "brek up", "brekq up", "toot gaya", "chor diya"
    ]
    return any(kw in text for kw in breakup_keywords)



def get_breakup_response() -> str:
    return (
        "💔 It’s okay to feel broken. Healing doesn’t mean forgetting, it means learning to grow from the pain. "
        "You deserve love, including your own. One step at a time — I'm here with you."
    )
