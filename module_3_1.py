calls = 0

def count_calls(func):
    """Декоратор для подсчета вызовов функций."""
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(string):
    """Возвращает кортеж из длины строки, строки в верхнем и нижнем регистре."""
    return (len(string), string.upper(), string.lower())

@count_calls
def is_contains(string, list_to_search):
    """Проверяет наличие строки в списке без учета регистра."""
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Вывод количества вызовов
print(calls)