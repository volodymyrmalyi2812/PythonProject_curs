from Object import *

def most_item_in_stock(products):
    product_with_most_items = products[0]

    for product in products:
        if product.in_stock > product_with_most_items.in_stock:
            product_with_most_items = product

    return product_with_most_items


