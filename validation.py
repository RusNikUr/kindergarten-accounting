# validation.py - проверки ввода
import os


def clear_screen():
    """Очищает экран терминала (кросс-платформенно)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_menu_choice(choice, max_option):
    """Проверяет выбор пункта меню."""
    try:
        num = int(choice)
        if 1 <= num <= max_option:
            return num
        else:
            print(f"Введите число от 1 до {max_option}!")
            return None
    except ValueError:
        print("Введите число!")
        return None


def validate_group_name(group):
    """Проверяет корректность названия группы."""
    valid_groups = ['младшая', 'средняя', 'старшая']
    if group.lower() in valid_groups:
        return group.lower()
    else:
        print("Ошибка: допустимые группы - 'младшая', 'средняя', 'старшая'")
        return None


def get_valid_group():
    """Запрашивает группу до получения корректного значения."""
    while True:
        group = input("Введите группу (младшая/средняя/старшая): ").strip().lower()
        validated = validate_group_name(group)
        if validated:
            return validated
        else:
            print("Попробуйте ещё раз...")