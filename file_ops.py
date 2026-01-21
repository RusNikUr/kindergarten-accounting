# file_ops.py - операции с файлами
def load_data(filename):
    """
    Загружает данные из файла в список словарей.
    Каждый словарь представляет запись о ребёнке.
    """
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаем пустые строки

                parts = line.split(',')
                if len(parts) != 10:
                    print(f"Ошибка в строке: {line}")
                    continue

                child = {
                    'last_name': parts[0],
                    'first_name': parts[1],
                    'birth_year': int(parts[2]),
                    'birth_month': int(parts[3]),
                    'birth_day': int(parts[4]),
                    'group': parts[5],
                    'neurologist': parts[6],
                    'ent_specialist': parts[7],
                    'orthopedist': parts[8],
                    'ophthalmologist': parts[9]
                }
                data.append(child)

        print(f"Загружено записей: {len(data)}")
        return data

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
        return []
    except ValueError as e:
        print(f"Ошибка в данных файла: {e}")
        return []


def save_data(filename, data):
    """
    Сохраняет список словарей обратно в файл.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for child in data:
                line = (
                    f"{child['last_name']},"
                    f"{child['first_name']},"
                    f"{child['birth_year']},"
                    f"{child['birth_month']},"
                    f"{child['birth_day']},"
                    f"{child['group']},"
                    f"{child['neurologist']},"
                    f"{child['ent_specialist']},"
                    f"{child['orthopedist']},"
                    f"{child['ophthalmologist']}"
                )
                file.write(line + '\n')
        print(f"Данные сохранены в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False
