from Objects import *
from task_class import *



def get_workers_older_than_x(user_list, x):
    result = []
    res = 0
    try:
        for user in user_list:
            if (2026 - user.year_of_birth) > x:
                res += 1
                result.append(user)
    except Exception as e:
        print(e)
    return res, result

def show_result(user_list):
    iter_list = iter(user_list)
    try:
        for user in user_list:
            print(next(iter_list))
    except Exception as e:
        print(e)

user_year = get_workers_older_than_x(workers_list, 60)

show_result(user_year)