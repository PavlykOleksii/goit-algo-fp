items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: dict[str, dict[str, int]], budget: int) -> list[str]:
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )

    chosen = []
    total_cost = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]

    return chosen


def dynamic_programming(items: dict[str, dict[str, int]], budget: int) -> list[str]:
    names = list(items.keys())
    n = len(names)

    # dp[i][b] - максимальні калорії з перших i страв при бюджеті b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    # Відновлюємо, які страви були вибрані
    chosen = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen.append(names[i - 1])
            b -= items[names[i - 1]]["cost"]

    return chosen


def print_result(title: str, chosen: list[str]) -> None:
    total_cost = sum(items[name]["cost"] for name in chosen)
    total_calories = sum(items[name]["calories"] for name in chosen)

    print(title)
    print("Страви:", chosen)
    print("Вартість:", total_cost)
    print("Калорії:", total_calories)
    print()


if __name__ == "__main__":
    budget = 100

    print_result("Жадібний алгоритм:", greedy_algorithm(items, budget))
    print_result("Динамічне програмування:", dynamic_programming(items, budget))
