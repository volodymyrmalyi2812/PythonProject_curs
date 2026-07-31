from Objects import *
from task_class import *


'''Визначити найдорожчий товар на складі та надрукувати всі відомості про нього'''
def max_price_product(products):
    most_expensive_product = None
    max_price = products[0].price
    for product in products:
        if product.price > max_price:
            max_price = product.price
            most_expensive_product = product

    return most_expensive_product

print(max_price_product(products))