from functools import reduce

teams = [2, 3, 3, 4]
pizzas = 5


# first half

# returns best combo
def get_best_team_combo(teams, pizzas):
    comps = []

    for i in range(len(teams)-1, 1, -1):
        # print(i)
        comp = 0
        compl = []
        j = i

        while j >= 0:
            if (comp+teams[j]) <= pizzas:
                # print("comp is ", comp, teams[j])
                comp += teams[j]
                compl.append(teams[j])
            j -= 1
        # comp = reduce(lambda a,b : a+b, teams[i:])
        if comp <= pizzas:
            comps.append(compl)

    def tall(i):
        return len(i)

    # print("all comps", comps)
    best_combo = max(comps, key=tall)
    # print(best_combo)
    return best_combo


# print(get_best_team_combo(teams, pizzas))
