from lab_2 import Database  

import unittest

class TestDatabaseSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        """
        Перевіряє, чи створюється лише один екземпляр класу Database.
        """
        db1 = Database(host='example.com', port=5432, username='user1', password='password1')
        db2 = Database()
        self.assertIs(db1, db2)

    def test_database_connection(self):
        """
        Перевіряє, чи встановлюється з'єднання з базою даних.
        """
        db = Database(host='testhost', port=1234, username='testuser', password='testpassword')
        connection = db.connect()
        self.assertEqual(connection, "З'єднано з testhost:1234 як testuser")

    def test_query_execution(self):
        """
        Перевіряє виконання запиту до бази даних.
        """
        db = Database(host='testhost', port=1234, username='testuser', password='testpassword')
        db.connect()
        result = db.execute_query("SELECT * FROM test_table")
        self.assertEqual(result, "Результат запиту: SELECT * FROM test_table")

    def test_missing_connection(self):
        """
        Перевіряє, чи виникає виняток при спробі виконати запит без попереднього підключення до бази даних.
        """
        db = Database()  # Спеціально не викликаємо метод connect()
        try:
            db.execute_query("SELECT * FROM test_table")
        except Exception as e:
            print("Exception raised:", e)
            self.assertTrue("З'єднання з базою даних не встановлено." in str(e))

if __name__ == "__main__":
    unittest.main()
