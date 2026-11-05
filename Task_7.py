import random

import matplotlib.pyplot as plt


# Аналітичні ймовірності: кількість комбінацій для кожної суми / 36
analytical = {
    2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36,
    8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36
}


def simulate_dice_rolls(num_rolls: int) -> dict[int, float]:
    counts = {total: 0 for total in range(2, 13)}

    for _ in range(num_rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        counts[dice_sum] += 1

    probabilities = {total: count / num_rolls for total, count in counts.items()}
    return probabilities


if __name__ == "__main__":
    num_rolls = 100_000
    monte_carlo = simulate_dice_rolls(num_rolls)

    print(f"Кількість кидків: {num_rolls}\n")
    print("Сума | Монте-Карло | Аналітично | Різниця")
    print("-" * 44)

    for total in range(2, 13):
        mc = monte_carlo[total] * 100
        an = analytical[total] * 100
        print(f"{total:>4} | {mc:>10.2f}% | {an:>9.2f}% | {abs(mc - an):>6.2f}%")

    sums = list(range(2, 13))

    plt.bar(sums, [monte_carlo[s] for s in sums], label="Монте-Карло", alpha=0.7)
    plt.plot(sums, [analytical[s] for s in sums], "ro-", label="Аналітично")
    plt.xticks(sums)
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.legend()
    plt.show()