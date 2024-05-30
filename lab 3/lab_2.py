import threading

class SingletonMeta(type):
    """
    Метаклас Singleton для забезпечення потокобезпечного створення лише одного екземпляру класу.
    """
    _instances = {}  # Словник для збереження екземплярів класів
    _lock = threading.Lock()  # Замок для потокобезпечності

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    """
    Клас Database, що реалізує Singleton підключення до бази даних з можливістю параметризації.
    """
    def __init__(self, host='localhost', port=3306, username='root', password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """
        Підключення до бази даних.
        """
        if not self.connection:
            print("З'єднання з базою даних...")
            # Симулюємо підключення до бази даних
            self.connection = f"З'єднано з {self.host}:{self.port} як {self.username}"
        return self.connection

    def execute_query(self, query):
        """
        Виконання запиту до бази даних.
        """
        if self.connection:
            print(f"Виконуємо запит: {query}")
            # Симулюємо виконання запиту
            return f"Результат запиту: {query}"
        else:
            raise Exception("З'єднання з базою даних не встановлено.")

# Приклад використання
if __name__ == "__main__":
    db1 = Database(host='example.com', port=5432, username='user1', password='password1')
    print(db1.connect())  # Вивід: З'єднання з базою даних... З'єднано з example.com:5432 як user1
    print(db1.execute_query("SELECT * FROM users"))

    db2 = Database()  # Повторне використання існуючого екземпляру
    print(db2.connect())  # Вивід: З'єднано з example.com:5432 як user1
