pizzas = [
    ["onion", "pepper", "olive"],
    ["mushroom", "tomato", "basil"],
    ["chicken", "mushroom", "pepper"],
    ["tomato", "mushroom", "basil"],
    ["chicken", "basil"]
]


def sort_diff_pizzas(pizzas, num):
    def tall(i):
        return len(i)
    pivot = set(max(pizzas, key=tall))
    n = len(pizzas)
    # print(n)

    def diff(i):
        return len(pivot.difference(i))
    pizzas = sorted(pizzas, key=diff)
    # print(pizzas)
    desired_pizzas = []
    # print(int(n/num))
    for i in range(0, n, int(n/num)):
        # if len(desired_pizzas) < num:
        desired_pizzas.append(pizzas[i])
    desired_pizzas = desired_pizzas[:num]
    # print(desired_pizzas)
    return desired_pizzas


# sort_diff_pizzas(pizzas, 3)
