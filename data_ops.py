# data_ops.py - операции с данными и сортировки
def count_healthy(child):
    """Считает количество 'здоров' у специалистов для одного ребёнка."""
    specialists = ['neurologist', 'ent_specialist', 'orthopedist', 'ophthalmologist']
    return sum(1 for spec in specialists if child[spec] == 'здоров')


def quick_sort(arr, key_func, reverse=False):
    """
    Быстрая сортировка (Хоара).
    key_func - функция, возвращающая ключ для сравнения.
    reverse - по убыванию (True) или возрастанию (False).
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    pivot_key = key_func(pivot)

    left = []
    middle = []
    right = []

    for item in arr:
        item_key = key_func(item)

        if reverse:
            # Для убывающей сортировки
            if item_key > pivot_key:
                left.append(item)
            elif item_key < pivot_key:
                right.append(item)
            else:
                middle.append(item)
        else:
            # Для возрастающей сортировки
            if item_key < pivot_key:
                left.append(item)
            elif item_key > pivot_key:
                right.append(item)
            else:
                middle.append(item)

    return quick_sort(left, key_func, reverse) + middle + quick_sort(right, key_func, reverse)


# Функции для формирования отчётов
def report_full(children):
    """
    Отчёт 1: по убыванию количества здоровых специалистов,
    затем по возрастанию фамилии.
    """

    def key_func(child):
        # Возвращаем кортеж: (-количество_здоровых, фамилия)
        return (-count_healthy(child), child['last_name'])

    return quick_sort(children, key_func)


def report_by_group(children, group_name):
    """
    Отчёт 2: для заданной группы по дате рождения (год, месяц, день).
    """
    # Сначала фильтруем по группе
    filtered = [c for c in children if c['group'] == group_name]

    def key_func(child):
        return (child['birth_year'], child['birth_month'], child['birth_day'])

    return quick_sort(filtered, key_func)


def report_needing_treatment(children):
    """
    Отчёт 3: нуждающиеся в лечении, сортировка по группе и фамилии.
    """
    # Фильтруем тех, у кого хотя бы один специалист указал "нуждается в лечении"
    filtered = []
    for child in children:
        if ('нуждается в лечении' in child['neurologist'] or
                'нуждается в лечении' in child['ent_specialist'] or
                'нуждается в лечении' in child['orthopedist'] or
                'нуждается в лечении' in child['ophthalmologist']):
            filtered.append(child)

    def key_func(child):
        # Группы сортируем в порядке: младшая, средняя, старшая
        group_order = {'младшая': 1, 'средняя': 2, 'старшая': 3}
        return (group_order.get(child['group'], 4), child['last_name'])

    return quick_sort(filtered, key_func)


def display_children(children, title):
    """Красиво выводит список детей."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}")

    if not children:
        print("Нет данных для отображения.")
        return

    print(f"{'№':<3} {'Фамилия':<15} {'Имя':<15} {'Группа':<10} {'Год рожд.':<10} {'Здоровых спец.':<15}")
    print("-" * 60)

    for i, child in enumerate(children, 1):
        healthy = count_healthy(child)
        print(f"{i:<3} {child['last_name']:<15} {child['first_name']:<15} "
              f"{child['group']:<10} {child['birth_year']:<10} {healthy:<15}")
