import unittest
from unittest.mock import patch
import io
from password_validator import validate_password

class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        test_input = "TestPassword123"
        expected_output = "OK\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            validate_password(test_input)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_short_password(self):
        test_input = "Short1"
        expected_output = "Пароль повинен містити щонайменше 8 символів\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            validate_password(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_no_digit_password(self):
        test_input = "NoDigitPassword"
        expected_output = "Пароль повинен містити щонайменше одну цифру\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            validate_password(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_no_uppercase_password(self):
        test_input = "nopassword123"
        expected_output = "Пароль повинен містити як мінімум одну велику і одну малу літеру\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            validate_password(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

    def test_no_lowercase_password(self):
        test_input = "NOPASSWORD123"
        expected_output = "Пароль повинен містити як мінімум одну велику і одну малу літеру\n"
        with patch('builtins.input', return_value=test_input), \
             patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
            validate_password(test_input)
            self.assertEqual(mock_stderr.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
