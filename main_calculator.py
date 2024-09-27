from calculator_function import get_number, get_operator, calculate, save_to_memory, recall_memory, show_history, add_to_history
from constants import global_var_calculator

def calculator():
    while True:
        num1 = get_number("Введіть перше число (або 'm' для значення з пам'яті): ")

        operator = get_operator()

        if operator != '√':
            num2 = get_number("Введіть друге число (або 'm' для значення з пам'яті): ")
        else:
            num2 = None

        result = calculate(num1, num2, operator)

        if result is not None:
            print(f"Результат: {result}")
            add_to_history(num1, num2, operator, result)

        save = input("Зберегти результат в пам'ять? (y/n): ")
        if save.lower() == 'y':
            save_to_memory(result)

        again = input("Виконати ще одне обчислення? (y/n): ")
        if again.lower() != 'y':
            break

        show_hist = input("Показати історію обчислень? (y/n): ")
        if show_hist.lower() == 'y':
            show_history()

if __name__ == "__main__":
    print("Ласкаво просимо до калькулятора!")
    calculator()
    print("Програма завершена")