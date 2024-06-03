# test_dumb_code.py

from dumb_code import binary_exponentiation

# Проведення декількох тестових випадків
def test_binary_exponentiation():
    assert binary_exponentiation(2, 3) == 8
    assert binary_exponentiation(3, 4) == 81
    assert binary_exponentiation(5, 0) == 1
    assert binary_exponentiation(10, 5) == 100000

# Запуск тестів
if __name__ == "__main__":
    test_binary_exponentiation()
    print("All tests passed!")
    