def greedy_algorithm(amount, calories, items):
    sorted_dict = dict(sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True))
    print(sorted_dict)
    res = []
    for item in sorted_dict:
        while amount >= items[item]["cost"] and calories >= items[item]["calories"]:
            amount -= items[item]["cost"]
            calories -= items[item]["calories"]
            res.append(item)

    return res, amount, calories


def dynamic_programming(items, amount):
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.keys())
    for i in range(1, len(items) + 1):
        for w in range(1, amount + 1):
            if items[item_list[i - 1]]['cost'] <= w:
                dp[i][w] = max(items[item_list[i - 1]]['calories'] + dp[i - 1][w - items[item_list[i - 1]]['cost']],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = amount
    n = len(items)
    chosen_items = []

    while n > 0:
        if dp[n][w] != dp[n - 1][w]:
            chosen_items.append(item_list[n - 1])
            w -= items[item_list[n - 1]]['cost']
        n -= 1

    return chosen_items, dp[-1][-1]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

res, balance_amount, balance_calories = greedy_algorithm(125, 1500, items)

print(f"Current amount balance: {balance_amount}")
print(f"Current calories balance: {balance_calories}")
print(res)

print(dynamic_programming(items, 50))
