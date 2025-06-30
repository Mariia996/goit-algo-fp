from timeit import Timer
from tabulate import tabulate

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict, budget: int):
    """Жадібний алгоритм для вибору страв з найбільшою калорійністю в межах бюджету."""
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )
    selected = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected, total_calories, total_cost

def dynamic_programming(items: dict, budget: int):
    """Алгоритм динамічного програмування для вибору страв з найбільшою калорійністю в межах бюджету."""
    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + cal)
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected = []
    total_cost = 0
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]
            total_cost += items[name]["cost"]

    selected.reverse()
    return selected, total_calories, total_cost

budget = 100

greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
t_greedy = Timer(lambda: greedy_algorithm(items, budget)).timeit(number=1) * 1e5
t_dp = Timer(lambda: dynamic_programming(items, budget)).timeit(number=1) * 1e5

table = [
    ["Вибрані страви", ", ".join(greedy_items), ", ".join(dp_items)],
    ["Загальна калорійність", greedy_calories, dp_calories],
    ["Загальна вартість", greedy_cost, dp_cost],
    ["Час виконання (ms)", f"{t_greedy:.2f}", f"{t_dp:.2f}"],
]
headers = ["Параметр", "Жадібний алгоритм", "Динамічне програмування"]

print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

if t_greedy < t_dp:
    print("Жадібний алгоритм працює швидше.")
elif t_greedy > t_dp:
    print("Динамічне програмування працює швидше.")
else:
    print("Обидва алгоритми мають однаковий час виконання.")

# Вивід: Жадібний алгоритм працює швидше.
