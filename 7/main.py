import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls: int) -> dict:
    """Функція для симуляції кидків двох кубиків та обчислення ймовірностей кожної можливої суми."""
    probabilities = None

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        if probabilities is None:
            probabilities = {i: 0 for i in range(2, 13)}

        probabilities[total] += 1
    # Обчислення ймовірностей
    for total in probabilities:
        probabilities[total] /= num_rolls

    return probabilities

def get_theoretical_probabilities() -> dict:
    """Повертає аналітичні ймовірності для кожної суми при киданні 2 кубиків."""
    return {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36,
        6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36,
        10: 3/36, 11: 2/36, 12: 1/36
    }

def plot_comparison_probabilities(simulated: dict, theoretical: dict, rolls: int):
    """Порівнює симуляційні та аналітичні ймовірності."""
    sums = list(range(2, 13))
    sim_values = [simulated[s] for s in sums]
    theo_values = [theoretical[s] for s in sums]

    x = range(len(sums))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], sim_values, width=width, label='Монте-Карло', color='lightblue')
    plt.bar([i + width/2 for i in x], theo_values, width=width, label='Аналітична', color='pink')
    plt.xticks(x, sums)
    plt.xlabel('Сума двох кубиків')
    plt.ylabel('Ймовірність')
    plt.title(f'Порівняння ймовірностей (Монте-Карло vs Аналітика) для {rolls} кидків')
    plt.legend()

    for i in x:
        plt.text(i - width/2, sim_values[i], f'{sim_values[i]:.2%}', ha='center', va='bottom', fontsize=8)
        plt.text(i + width/2, theo_values[i], f'{theo_values[i]:.2%}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.show()

def print_probability_table(simulated: dict, theoretical: dict):
    """Виводить порівняльну таблицю ймовірностей у відсотках у форматі Markdown."""
    print("| Сума | Монте-Карло  | Аналітична  | Різниця |")
    print("|------|--------------|-------------|---------|")

    for total in range(2, 13):
        sim_p = simulated[total] * 100
        theo_p = theoretical[total] * 100
        diff = sim_p - theo_p
        sign = "+" if diff >= 0 else "−"
        print(f"| {total:<4} | {sim_p:>6.2f}%      | {theo_p:>6.2f}%     | {sign}{abs(diff):<5.2f}% |")

if __name__ == "__main__":
    for rolls in [1000, 10000, 100000]:
        print(f"\n🎯 Результати моделювання для {rolls} кидків:")
        simulated_probs = simulate_dice_rolls(rolls)
        theoretical_probs = get_theoretical_probabilities()
        print_probability_table(simulated_probs, theoretical_probs)
        plot_comparison_probabilities(simulated_probs, theoretical_probs, rolls)