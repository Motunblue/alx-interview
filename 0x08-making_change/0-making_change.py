#!/usr/in/python3
""" Make change module
"""


def makeChange(coins, total):
    """  determine the fewest number of coins needed to meet a total
    """
    if total == 0:
        return 0
    if total < 0:
        return -1
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
    if total == 0:
        return num_coins
    return -1
