import re
import sys

def validate_password(password):
    # Перевірка довжини пароля (мінімум 8 символів)
    if len(password) < 8:
        print("Пароль повинен містити щонайменше 8 символів", file=sys.stderr)
        return 1

    # Перевірка наявності цифр
    if not re.search(r'\d', password):
        print("Пароль повинен містити щонайменше одну цифру", file=sys.stderr)
        return 1

    # Перевірка наявності великих та малих літер
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        print("Пароль повинен містити як мінімум одну велику і одну малу літеру", file=sys.stderr)
        return 1

    # Пароль відповідає всім критеріям
    print("OK")
    return 0

if __name__ == "__main__":
    # Отримання пароля з аргументів командного рядка
    password = input("Введіть пароль: ").strip()

    # Перевірка пароля та виведення результату
    exit_code = validate_password(password)
    sys.exit(exit_code)
