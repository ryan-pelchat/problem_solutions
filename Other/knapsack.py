"""
You have a knapsack with a maximum volume.
Given a list of items where each item has a price and a volume, 
maximize the price and minimize the volume taken in your knapsack

"""


def knapsack(knapsackVolume: int, items: list[tuple[int, int]]) -> list[int]:
    """
    in the items list, each item is a tuple of (price, volume)
    returns a list of items
    """
    subInstances = [[0 for __ in range(items + 1)] for _ in range(knapsackVolume + 1)]
    pass


if __self__ == "__main__":
    pass
