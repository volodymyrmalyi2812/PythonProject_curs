def get_full_time(experience):
    salary = 20000
    if 3 <= experience < 5:
        k = 1.5
    elif 5 <= experience < 7:
        k = 2
    elif experience >= 7:
        k = 3
    else:
        k = 1
    salary *= k
    return salary


def get_part_time(hours):
    per_hour = 800
    salary = hours * per_hour
    return salary
