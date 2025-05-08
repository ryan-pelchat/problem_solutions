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
    subInstances = [
        [0 for __ in range(len(items) + 1)] for _ in range(knapsackVolume + 1)
    ]  # init 2D array

    # base case already initialized
    for i in range(1, len(subInstances)):  # i is number of capacity
        for j in range(1, len(subInstances[0])):  # j is objects prefix considered
            # see if current item can fit in bag
            if items[j - 1][1] <= i:
                # there is space, take item!
                subInstances[i][j] = max(
                    subInstances[i][j - 1],
                    subInstances[i - items[j - 1][1]][j - 1] + items[j - 1][0],
                )
            else:
                # no space, don't take item
                subInstances[i][j] = subInstances[i][j - 1]

    # reconstruct the items taken
    currWeight = len(subInstances) - 1
    objectTaken = []
    for i in range(len(subInstances[0]) - 1, 0, -1):
        if subInstances[currWeight][i] != subInstances[currWeight][i - 1]:
            objectTaken.append(items[i - 1])
            currWeight -= items[i - 1][1]

    return objectTaken


if __name__ == "__main__":
    print(knapsack(7, [(2, 3), (2, 4), (4, 5), (1, 2)]))
