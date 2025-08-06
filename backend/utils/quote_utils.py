import random
import os
from datetime import date

def get_daily_quote() -> str:
    filepath = os.path.abspath("../assets/quotes/quotes.txt")
    with open(filepath, "r") as f:
        quotes = f.readlines()

    today_index = date.today().toordinal() % len(quotes)
    return quotes[today_index].strip()


def get_random_quote() -> str:
    filepath = os.path.abspath("../assets/quotes/quotes.txt")
    with open(filepath, "r") as f:
        quotes = f.readlines()

    return random.choice(quotes).strip()
