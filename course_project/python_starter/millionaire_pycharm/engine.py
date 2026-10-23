import random

from questions import QUESTIONS, QUESTIONS_BY_ID

PRIZES = [500, 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 125000, 250000, 375000, 500000, 750000, 1000000]
LETTERS = "ABCD"
HINT_NAMES = {"fifty": "50/50", "friend": "Дзвінок другу", "audience": "Допомога залу"}


def create_game():
    return {
        "level": 0,
        "question_id": None,
        "asked_ids": [],
        "used_hints": {name: False for name in HINT_NAMES},
        "hidden_choices": [],
    }


def current_prize(level):
    return PRIZES[level - 1] if level > 0 else 0


def guaranteed_prize(level):
    if level >= 10:
        return PRIZES[9]
    if level >= 5:
        return PRIZES[4]
    return 0


def difficulty_for_level(level):
    if level < 5:
        return "easy"
    if level < 10:
        return "medium"
    return "hard"


def current_question(state):
    question_id = state["question_id"]
    return QUESTIONS_BY_ID[question_id] if question_id is not None else None


def select_question(state, rng=None):
    if state["level"] >= len(PRIZES):
        return None
    existing = current_question(state)
    if existing is not None:
        return existing
    group = difficulty_for_level(state["level"])
    available = [q for q in QUESTIONS if q["difficulty"] == group and q["id"] not in state["asked_ids"]]
    if not available:
        raise ValueError("Для цього рівня закінчилися запитання")
    question = (rng or random).choice(available)
    state["question_id"] = question["id"]
    state["asked_ids"].append(question["id"])
    return question


def visible_choices(state):
    if current_question(state) is None:
        raise ValueError("Спочатку потрібно вибрати запитання")
    return [index for index in range(4) if index not in state["hidden_choices"]]


def use_fifty(state, rng=None):
    if state["used_hints"]["fifty"]:
        raise ValueError("Підказку 50/50 вже використано")
    question = current_question(state)
    if question is None:
        raise ValueError("Немає активного запитання")
    incorrect = [i for i in visible_choices(state) if i != question["correct"]]
    state["hidden_choices"] = sorted((rng or random).sample(incorrect, 2))
    state["used_hints"]["fifty"] = True
    return visible_choices(state)


def use_friend(state, rng=None):
    if state["used_hints"]["friend"]:
        raise ValueError("Підказку «Дзвінок другу» вже використано")
    choices = visible_choices(state)
    answer = (rng or random).choice(choices)
    state["used_hints"]["friend"] = True
    return LETTERS[answer]


def use_audience(state, rng=None):
    if state["used_hints"]["audience"]:
        raise ValueError("Підказку «Допомога залу» вже використано")
    question = current_question(state)
    if question is None:
        raise ValueError("Немає активного запитання")
    generator = rng or random
    choices = visible_choices(state)
    correct = question["correct"]
    percentages = [0, 0, 0, 0]
    correct_percent = generator.randint(50, 75) if len(choices) > 2 else generator.randint(65, 90)
    percentages[correct] = correct_percent
    other_choices = [i for i in choices if i != correct]
    remaining = 100 - correct_percent
    dividers = sorted([0, remaining] + [generator.randint(0, remaining) for _ in range(len(other_choices) - 1)])
    portions = [dividers[i + 1] - dividers[i] for i in range(len(other_choices))]
    generator.shuffle(portions)
    for i, portion in zip(other_choices, portions):
        percentages[i] = portion
    state["used_hints"]["audience"] = True
    return dict(zip(LETTERS, percentages))


def check_answer(state, answer):
    question = current_question(state)
    if question is None:
        raise ValueError("Немає активного запитання")
    letter = answer.strip().upper()
    if len(letter) != 1 or letter not in LETTERS:
        raise ValueError("Оберіть A, B, C або D")
    index = LETTERS.index(letter)
    if index in state["hidden_choices"]:
        raise ValueError("Цей варіант прибрано підказкою 50/50")
    correct = index == question["correct"]
    if correct:
        state["level"] += 1
        state["question_id"] = None
        state["hidden_choices"] = []
    return correct
