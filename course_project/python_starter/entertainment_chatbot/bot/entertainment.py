
import random
import pyjokes

from bot.data import RECOMMENDATIONS, JOKES_UA, STORIES


def get_genres(category: str) -> list[str]:
    if category not in RECOMMENDATIONS:
        raise ValueError("Невідома категорія")
    return list(RECOMMENDATIONS[category])


def recommend_item(category: str, genre: str) -> str:
    if category not in RECOMMENDATIONS or genre not in RECOMMENDATIONS[category]:
        raise ValueError("Невідома категорія або жанр")
    return random.choice(RECOMMENDATIONS[category][genre])


def ukrainian_joke() -> str:
    return random.choice(JOKES_UA)


def english_programmer_joke() -> str:
    return pyjokes.get_joke(language="en", category="all")


def interesting_story() -> str:
    return random.choice(STORIES)
