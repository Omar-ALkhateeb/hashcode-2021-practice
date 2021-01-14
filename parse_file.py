from teams import get_best_team_combo
from sort import sort_diff_pizzas


filename = "d_many_pizzas.in"
lines = []
with open(filename, "r") as splitfile:
    for line in [line.split() for line in splitfile]:
        # print(line)
        lines.append(line)


print("file parsed")


teams = []

for i in range(1, len(lines[0])):
    # print(lines[0][i])
    for j in range(int(lines[0][i])):
        teams.append(i+1)

# print(teams)

pizzas = []
all_pizzas = []
pizzas_num = int(lines[0][0])

for i in lines[1:]:
    pizzas.append(i[1:])


# jeep index of pizzas when they're deleted from array pizzas
all_pizzas = pizzas[:]

# print(pizzas)
# print(all_pizzas)


best_combo = sorted(get_best_team_combo(teams, pizzas_num))
# print(best_combo)
print("finished forming the teams")


delivered_pizzas = []
# removed = []


# makes the op slower but with better scores???
best_combo = best_combo[::-1]

for i in best_combo:
    best_pizzas = sort_diff_pizzas(pizzas, i)
    # print(i)
    delivered_pizzas.append(best_pizzas)
    for i in best_pizzas:
        # removed.append(all_pizzas.index(i))
        pizzas.remove(i)

# print(removed)
print("finished dividing pizza")

# print(delivered_pizzas)
# print(all_pizzas)

# write output
file = open('sol_'+filename, 'w')

# to ensure duplicate values-not-indeces are not confused
indeces = []
output = "{}\n".format(len(best_combo))

for i in range(len(best_combo)):
    output += "{}".format(best_combo[i])
    for j in delivered_pizzas[i]:
        index = all_pizzas.index(j)
        while index in indeces:
            # print(index, "changed to")
            index = all_pizzas.index(j, index+1)
            print(index)
        output += " {}".format(index)
        indeces.append(index)
        # all_pizzas.remove(j)
    output += "\n"
file.write(output)
