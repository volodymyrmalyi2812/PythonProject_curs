from ArraysOfObject import *
def best_forward(footbolist, amplua):
    best_f = None
    max_goal = -1
    for gravec in footbolist:
        # Тут gravec.amplua та gravec.count_of_goals викликають відповідні @property методи
        if gravec.amplua == amplua and gravec.count_of_goals > max_goal:
            max_goal = gravec.count_of_goals
            best_f = gravec
    return best_f

def print_footbolist(footbolist):
    for gravec in footbolist:
        print(gravec.count_of_goals)

def sort_footbolist(footbolist):
    pass

def filter_footbolist(footbolist):
    pass
def find_by_futbolist(footbolist):
    pass
