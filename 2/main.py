file = open('./2/in', 'r')
rows = file.readlines()

colors = ["red", "green", "blue"]
bag = {"red": 12, "green": 13, "blue": 14}

valid_game_nums = []
min_cubes = []
products = []

for row in rows:
    [game_num, sets] = row.split(":")
    game_num = int(game_num.replace("Game ", ""))
    sets = [x.strip() for x in sets.split(";")]
    sets_result = []

    valid_sets = []
    for set in sets:
        colors_list = [x.strip() for x in set.split(",")]
        colors_map = {}
        for color in colors_list:
            for c in colors:
                if c in color:
                    colors_map[c] = int(color.replace(c, "").strip())
                    break

        if ((colors_map.get("red") or 0) <= bag["red"]
                and (colors_map.get("green") or 0) <= bag["green"]
                and (colors_map.get("blue") or 0) <= bag["blue"]):
            valid_sets.append(game_num)

        sets_result.append(colors_map)

    if len(valid_sets) == len(sets):
        valid_game_nums.append(game_num)

    min_red = max([x.get("red") or 0 for x in sets_result])
    min_green = max([x.get("green") or 0 for x in sets_result])
    min_blue = max([x.get("blue") or 0 for x in sets_result])
    min_cubes.append([min_red, min_green, min_blue])
    products.append(min_red * min_green * min_blue)

    # print(game_num, sets_result)

# print(sum(valid_game_nums))
print(min_cubes)
print(sum(products))
# print(game_num, sets)
