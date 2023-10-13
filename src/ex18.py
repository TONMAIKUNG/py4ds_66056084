"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(cup, price):
    promotion_pack = 8+1
    amount_packs = cup // promotion_pack
    amount_cup = cup % promotion_pack
    total = (amount_packs * 8 * price) + (amount_cup * price)
    return total


def get_cost_of_coffee_2(cup, price):
    promotion_pack = 8+1
    amount_packs = cup // promotion_pack
    amount_cup = cup % promotion_pack
    total = (amount_packs * 8 * price) + (amount_cup * price)
    return total