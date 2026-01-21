# main.py - главный файл программы
import os
import file_ops
import data_ops
import validation


def clear_screen():
    """Очищает экран терминала (кросс-платформенно)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_screen()
    print("=" * 60)
    print("      УЧЕТ РЕЗУЛЬТАТОВ ДИСПАНСЕРИЗАЦИИ")
    print("=" * 60)

    # Загрузка данных
    children = file_ops.load_data('database.txt')
    if not children:
        print("Не удалось загрузить данные. Программа завершена.")
        return

    while True:
        print("\n" + "=" * 40)
        print("ГЛАВНОЕ МЕНЮ:")
        print("1. Полный список (сортировка по здоровью)")
        print("2. Список по группе (сортировка по дате рождения)")
        print("3. Список нуждающихся в лечении")
        print("4. Выход")
        print("=" * 40)

        choice = input("Выберите пункт меню (1-4): ").strip()
        valid_choice = validation.validate_menu_choice(choice, 4)

        if valid_choice is None:
            clear_screen()
            continue

        if valid_choice == 1:
            clear_screen()
            # Отчёт 1
            sorted_children = data_ops.report_full(children)
            data_ops.display_children(sorted_children,
                                      "ПОЛНЫЙ СПИСОК (сортировка: здоровые → фамилия)")

        elif valid_choice == 2:
            clear_screen()
            # Отчёт 2
            group = validation.get_valid_group()
            if group:
                clear_screen()
                sorted_children = data_ops.report_by_group(children, group)
                data_ops.display_children(sorted_children,
                                          f"СПИСОК ГРУППЫ '{group.upper()}' (сортировка по дате рождения)")

        elif valid_choice == 3:
            clear_screen()
            # Отчёт 3
            sorted_children = data_ops.report_needing_treatment(children)
            data_ops.display_children(sorted_children,
                                      "СПИСОК НУЖДАЮЩИХСЯ В ЛЕЧЕНИИ (сортировка: группа → фамилия)")

        elif valid_choice == 4:
            clear_screen()
            print("Выход из программы. До свидания!")
            break

        input("\nНажмите Enter для возврата в меню...")
        clear_screen()


if __name__ == "__main__":
    main()