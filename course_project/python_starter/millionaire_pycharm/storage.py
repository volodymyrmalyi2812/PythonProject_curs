import json
from pathlib import Path

from engine import HINT_NAMES, PRIZES
from questions import QUESTIONS_BY_ID

BASE_DIR = Path(__file__).resolve().parent
SAVE_FILE = BASE_DIR / "savegame.json"
STATS_FILE = BASE_DIR / "statistics.json"


def save_game(state, path=SAVE_FILE):
    Path(path).write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def load_game(path=SAVE_FILE):
    source = Path(path)
    if not source.exists():
        return None
    try:
        state = json.loads(source.read_text(encoding="utf-8"))
        level = state["level"]
        question_id = state["question_id"]
        asked = state["asked_ids"]
        hints = state["used_hints"]
        hidden = state["hidden_choices"]
        if type(level) is not int or not 0 <= level < len(PRIZES):
            return None
        if not isinstance(asked, list) or len(asked) != len(set(asked)):
            return None
        if any(q not in QUESTIONS_BY_ID for q in asked):
            return None
        if not isinstance(question_id, (str, type(None))) or (question_id is not None and (question_id not in QUESTIONS_BY_ID or question_id not in asked)):
            return None
        if not isinstance(hints, dict) or any(type(hints.get(name)) is not bool for name in HINT_NAMES):
            return None
        if not isinstance(hidden, list) or any(type(i) is not int or i not in range(4) for i in hidden):
            return None
        if len(hidden) != len(set(hidden)) or (hidden and (not hints["fifty"] or question_id is None)):
            return None
        if question_id is not None and QUESTIONS_BY_ID[question_id]["correct"] in hidden:
            return None
        return state
    except (ValueError, TypeError, KeyError, OSError):
        return None


def delete_save(path=SAVE_FILE):
    Path(path).unlink(missing_ok=True)


def empty_stats():
    return {"games": 0, "victories": 0, "correct": 0, "wrong": 0, "earned": 0, "best": 0, "history": []}


def load_stats(path=STATS_FILE):
    source = Path(path)
    if not source.exists():
        return empty_stats()
    try:
        stats = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(stats, dict) or any(name not in stats for name in empty_stats()):
            return empty_stats()
        return stats
    except (ValueError, OSError):
        return empty_stats()


def record_result(correct, wrong, prize, path=STATS_FILE):
    stats = load_stats(path)
    stats["games"] += 1
    stats["victories"] += int(correct == len(PRIZES))
    stats["correct"] += correct
    stats["wrong"] += int(wrong)
    stats["earned"] += prize
    stats["best"] = max(stats["best"], prize)
    stats["history"].append({"correct": correct, "wrong": bool(wrong), "prize": prize})
    stats["history"] = stats["history"][-10:]
    Path(path).write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    return stats
